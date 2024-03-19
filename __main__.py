# -*- coding: utf-8 -*-
import csv
import json
import logging
import os
import re
import subprocess
import sys
import time
import traceback
from io import BytesIO
from threading import Lock, Thread, Timer
import tempfile
sys.coinit_flags = 2

import requests
import tinytag
from tinytag import TinyTag
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QListWidget, QLabel
import pyglet
from player import Player

from design import Ui_MainWindow
from dialog import *
from path import (dirpath, ffprobe, ffplay, app_icon, logo_icon, play_icon, pause_icon, music_icon, logo_urls)
import m3u_parser

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = os.open(os.devnull, os.O_RDWR)


# sys.stderr = open('D:\\output.txt', 'w')


class PlayerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PlayerApp, self).__init__()
        self.setWindowIcon(QIcon(app_icon))
        self.my_thread = Thread(target=self.start_playing)
        self.my_thread2 = Thread(target=self.start_streaming)
        self.song_timer = QTimer()
        self.song_timer.setInterval(10)
        self.song_timer.timeout.connect(self.start_timer)
        self.stream_timer = Timer(3.5, self.start_stream_timer)
        self.player = Player()
        self.state = self.player.state
        self.setupUi(self)
        self.dialog = SelectStreamDialog(self)
        self.play_button.mouseReleaseEvent = self.play_event
        self.play_icon = QIcon(play_icon)
        self.play_icon_2 = QIcon(pause_icon)
        self.prev_button.mouseReleaseEvent = self.prev_song
        self.forward_button.mouseReleaseEvent = self.forward_song
        self.stop_button.mouseReleaseEvent = self.stop
        self.horizontalSlider.setStyleSheet('''QSlider{
            }
            QSlider::groove:horizontal {
                height: 3px;
                margin: 0px;
                border-radius: 5px;
                background: #B0AEB1;
            }
            QSlider::handle:horizontal {
                background: #fff;
                border: 1px solid #E3DEE2;
                width: 10px;
                height: 10px;
                margin: -5px 0;
                border-radius: 5px;
            }
            QSlider::sub-page:qlineargradient {
                border-radius: 5px;
            }''')
        self.horizontalSlider.valueChanged[int].connect(self.changeSliderValue)
        self.action.triggered.connect(self.open_file)
        self.actionOpen_folder.triggered.connect(self.open_folder)
        self.actionOpen_URL.triggered.connect(self.dialog.exec)
        self.actionAbout.triggered.connect(lambda: QMessageBox.about(
            self, 'ClearWave Music Player', "ClearWave Music Player version 1.4.2"))
        files = os.listdir(dirpath)
        for i in files:
            match = re.search(r'\.m3u', i)
            if match:
                self.playlistWidget.addItem(i)
        self.listWidget.clicked.connect(self.select_item)
        self.listWidget.itemSelectionChanged.connect(self.changed_item)
        self.playlistWidget.clicked.connect(self.add_items)
        self.count = 0
        self.timer_count = 0
        self.actionOpen_playlist.triggered.connect(self.open_playlist)
        self.actionSave_playlist.triggered.connect(self.save_playlist)
        urls_file = open(logo_urls, 'r', encoding='utf-8')
        reader = csv.DictReader(urls_file)
        self.rs_data = [self.format_name(row) for row in reader]
        self.radio_names: list = [i['radio_name'] for i in self.rs_data]
        urls_file.close()

    def open_file(self):
        self.fpathlist = []
        self.files = QFileDialog(directory=dirpath).getOpenFileUrls()[0]
        if self.files:
            for i in self.files:
                Data.filelist.append(i.path()[1:])
                self.listWidget.addItem(i.fileName())
        else:
            pass

    def open_folder(self):
        self.dir = QFileDialog(directory=dirpath).getExistingDirectoryUrl()
        print(self.dir)
        if self.dir.path() != '':
            fp = self.dir.path()[1:]
            self.listWidget.clear()
            Data.filelist.clear()
            self.filenames = os.listdir(fp)
            for i in self.filenames:
                path = f'{fp}\\{i}'
                if TinyTag.is_supported(path):
                    tag = TinyTag.get(path, image=True)
                    if tag.title != '' and tag.artist != '':
                        temp_file = tempfile.NamedTemporaryFile("w+b", prefix="image", suffix=".png",
                                                                delete=False)
                        title = f'{tag.artist} - {tag.title}'
                        image = tag.get_image()
                        if image:
                            temp_file.write(image)
                            temp_file.seek(0)
                            image_src = temp_file.name
                            print(image_src)
                            temp_file.close()
                            item = QListWidgetItem(QIcon(image_src), title)
                        else:
                            item = QListWidgetItem(QIcon(music_icon), title)
                        item.setSizeHint(QSize(25, 25))
                        self.listWidget.addItem(item)
                    elif tag.title and tag.artist == '':
                        item = QListWidgetItem(QIcon(music_icon), i)
                        self.listWidget.addItem(item)
                    Data.filelist.append('{0}/{1}'.format(fp, i))
        else:
            pass

    def open_playlist(self):
        filepath = QFileDialog(directory=dirpath).getOpenFileUrl()
        if filepath[0].path() != '':
            fp = filepath[0].path()[1:]
            filename = filepath[0].fileName()
            self.playlistWidget.addItem(filename)
            self.add_items(fp)
        else:
            pass

    def add_items(self, value):
        if isinstance(value, str):
            fp = value
        else:
            fp = f'{dirpath}\\{self.playlistWidget.itemFromIndex(value).text()}'
        playlist = m3u_parser.load(filepath=fp)
        self.listWidget.clear()
        Data.filelist = []
        Data.streamlist = []
        if playlist.files:
            for i in playlist.files:
                if TinyTag.is_supported(i.file):
                    tag = TinyTag.get(i.file, image=True)
                    Data.filelist.append(i.file)
                    if tag.title != '' and tag.artist != '':
                        title = f'{tag.artist} - {tag.title}'
                        art = tag.get_image()
                        temp_file = tempfile.NamedTemporaryFile("w+b", prefix="image", suffix=".png",
                                                                delete=False, delete_on_close=False)
                        if art:
                            image = Image.open(art)
                            image.save(temp_file.name, format="png")
                            temp_file.close()
                            item = QListWidgetItem(QIcon(temp_file.name), title)
                        else:
                            item = QListWidgetItem(QIcon(music_icon), title)
                        item.setSizeHint(QSize(25, 25))
                        self.listWidget.addItem(item)
                    elif tag.title and tag.artist == '':
                        self.listWidget.addItem(i.file)
                else:
                    self.listWidget.addItem(i)
        if playlist.urls:
            for i in playlist.urls:
                Data.streamlist.append(i.url)
                Data.pics.append(i.picture)
                self.listWidget.addItem(i.title)
        self.listWidget.setCurrentRow(0)

    def save_playlist(self):
        self.playlist = QFileDialog(directory=dirpath).getSaveFileUrl()
        if self.playlist[0].path() != '':
            file = self.playlist[0].path()[1:]
            with open(file, 'w', encoding='utf-8', errors='ignore') as file:
                if Data.filelist:
                    file.writelines(('#EXTM3U', '\n'))
                    for i in Data.filelist:
                        tag = TinyTag.get(i)
                        desc = f'#EXTINF:{str(tag.duration)[:3]},{tag.artist} - {tag.title}'
                        filepath = str(i)
                        file.writelines((desc, '\n', filepath, '\n'))
                if Data.pls_content != '':
                    file.write(Data.pls_content)
        else:
            pass

    @staticmethod
    def is_stream():
        if not Data.filelist:
            return True
        else:
            return False

    def select_item(self, value):
        self.listWidget.setCurrentIndex(value)
        if self.listWidget.currentRow() == 0:
            self.state = 'stop'
        else:
            pass

    def changed_item(self):
        if self.is_stream():
            try:
                self.stream_url = Data.streamlist[self.listWidget.currentRow()]
                requests.get(self.stream_url, timeout=0.75, stream=True)
            except:
                radio_name = self.listWidget.currentItem().text()
                self.metadataWidget.setText(radio_name)
                self.load_img_data()
            else:
                self.radio_name = self.listWidget.currentItem().text().strip()
                self.metadataWidget.setText(self.radio_name)
                if self.timer_count == 0:
                    self.stream_timer.start()
                if self.listWidget.SelectedClicked:
                    img_url = Data.pics[self.listWidget.currentRow()]
                    if img_url:
                        self.resize_image(img_url=img_url)
                    else:
                        my_thread = Thread(target=self.load_img_data)
                        my_thread.start()
                    my_thread = Thread(target=self.get_stream_metadata)
                    my_thread.start()
        else:
            pass
        self.player.change_song()

    def play_event(self, event):
        self.player.counter()
        if self.player.count == 1:
            if self.is_stream():

                self.play_button.setIcon(self.play_icon_2)
                self.player.state = 'playing'
                self.start_streaming()
            else:
                self.play_button.setIcon(self.play_icon_2)
                if self.player.state in ("started", "stop", "paused"):
                    self.start_playing()
                    time.sleep(0.5)
                    self.song_timer.start()
        elif self.player.count > 1:
            if self.is_stream():
                self.proc.terminate()
                self.my_thread2.join(0.03)
                if self.player.state == 'playing':
                    self.play_button.setIcon(self.play_icon)
                    self.player.state = 'stop'
                else:
                    self.play_button.setIcon(self.play_icon_2)
                    self.player.state = 'playing'
                    self.start_streaming()
            else:
                if self.player.state == "stop":
                    self.song_timer.start()
                    my_event = Thread(target=self.play_song)
                    my_event.start()
                else:
                    if self.player.state == "item_changed":
                        my_thread = Thread(target=self.changeIcon)
                        my_thread.start()
                        filepath = Data.filelist[self.listWidget.currentRow()]
                        self.player.play_song(filepath)
                    else:
                        if self.player.state == "playing":
                            self.play_button.setIcon(self.play_icon)
                            my_thread = Thread(target=self.player.pause)
                            my_thread.start()
                        else:
                            self.play_button.setIcon(self.play_icon_2)
                            my_thread = Thread(target=self.player.resume)
                            my_thread.start()

    def playback_event(self):
        if self.player.is_next_song():
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)
            file = Data.filelist[self.listWidget.currentRow()]
            self.play_song(file)

    def start_timer(self):
        self.setSliderPos()
        self.playback_event()


    def start_playing(self):
        file = Data.filelist[self.listWidget.currentRow()]
        my_thread = Thread(target=self.player.start_playing, args=(file,))
        my_thread.start()
        self.get_song_metadata()

    def start_streaming(self):
        try:
            self.my_thread2 = Thread(target=self.play_stream)
            self.my_thread2.start()
        except subprocess.CalledProcessError:
            traceback.print_exc()
            show_alert()

    def start_stream_timer(self):
        while True:
            self.get_stream_metadata()
            time.sleep(3.5)
            if re.search(r'stop|close_app', self.state):
                break

    mutex = Lock()

    def play_song(self, file, *args):
        self.player.play_song(file)
        self.get_song_metadata()

    def play_stream(self):
        if self.state == 'item_changed':
            self.play_button.setPixmap(self.pixmap)
            time.sleep(0.5)
        self.state = "playing"
        self.play_button.setPixmap(self.pixmap_2)
        stream_file = Data.streamlist[self.listWidget.currentRow()]
        self.proc = subprocess.Popen(f'{ffplay} -nodisp -i {stream_file}',
                                     creationflags=subprocess.CREATE_NO_WINDOW)
        self.proc.communicate()



    def get_song_metadata(self):
        row = self.listWidget.currentRow()
        file = Data.filelist[row]
        try:
            self.tag = TinyTag.get(file, image=True)
            tag_img = self.tag.get_image()
            if tag_img:
                self.resize_image(img_data=tag_img)
            self.metadataWidget.setText(f'{self.tag.title}\n{self.tag.artist} - {self.tag.album}')
        except tinytag.TinyTagException:
            self.forward_song()


    @staticmethod
    def format_name(i):
        i['radio_name'] = i['radio_name'].lower()
        return i

    def get_stream_metadata(self):
        self.timer_count += 1
        print(self.timer_count)
        self.stream_url = Data.streamlist[self.listWidget.currentRow()]
        row = self.listWidget.currentRow()
        cmd = f'{ffprobe} -v quiet -show_entries format_tags=StreamTitle -of json {Data.streamlist[row]}'
        stdout = subprocess.check_output(cmd, stdin=DEVNULL, stderr=DEVNULL,
                                         creationflags=subprocess.CREATE_NO_WINDOW)
        if stdout:
            data = json.loads(stdout)
            stream_title = data.get('format').get('tags').get('StreamTitle')
            if not re.search('\w', stream_title):
                pass
            else:
                stream_title = stream_title.strip()
                self.metadataWidget.setText(f'{self.radio_name}\n{stream_title}')

    def load_img_data(self):
        item = re.sub(r'^[\d.\-_ ]+', '', self.listWidget.currentItem().text().lower())
        item = item.strip()
        q = False
        for index, i in enumerate(self.radio_names):
            if (item.startswith('радио ') and i.startswith('радио ') and
                    i.startswith(item)):
                q = True
            elif ((i.replace('радио ', '').startswith(item) or
                   item.replace('радио ', '').startswith(i))):
                q = True
            if q:
                img_url = self.rs_data[index]['radio_logo']
                self.resize_image(img_url=img_url)
                break
        if not q:
            pixmap = QPixmap()
            pixmap.load(logo_icon)
            self.imgWidget.setPixmap(pixmap)

    def resize_image(self, **kwargs):
        # try:
        img_url = str()
        im_resized = Image.Image()
        if kwargs:
            if kwargs.get('img_data'):
                # pixmap = QPixmap()
                byte_array = BytesIO(kwargs['img_data'])
                image = Image.open(byte_array)
                im_resized = image.resize((30, 30))
            elif kwargs.get('img_url'):
                if 'https://' not in kwargs['img_url']:
                    img_url = 'https://' + kwargs['img_url']
                response = requests.get(img_url, stream=True)
                byte_array = BytesIO(response.content)
                image = Image.open(byte_array)
                if image.height <= 100:
                    (w, h) = (image.width // 2.8, image.height // 2.8)
                    im_resized = image.resize((int(w), int(h)))
                else:
                    im_resized = image.resize((30, 30))
            byte_array = BytesIO()
            im_resized.save(byte_array, format='PNG')
            self.imgWidget.clear()
            pixmap = QPixmap()
            img_bytes = byte_array.getvalue()
            pixmap.loadFromData(QByteArray(img_bytes))
            self.imgWidget.setPixmap(pixmap)
        else:
            pass
            # except:
        #     pixmap = QPixmap()
        #     pixmap.load(logo_icon)
        #     self.imgWidget.setPixmap(pixmap)

    def setSliderPos(self, value=0):
        value = int(value)
        current_duration = self.player.get_duration()
        if value != 0 and (value - current_duration > 3 or value < current_duration):
            pts = self.player.source_duration / 500 * value
            pts = round(pts, 2)
            self.player.seek(pts)
        self.horizontalSlider.setValue(self.player.get_duration())

    def changeSliderValue(self, value):
        self.setSliderPos(value)

    def changeIcon(self):
        self.play_button.setIcon(self.play_icon)
        time.sleep(0.3)
        self.play_button.setIcon(self.play_icon_2)

    def prev_song(self, event):
        self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)
        file = Data.filelist[self.listWidget.currentRow()]
        print("previous song")
        self.play_song(file)

    def forward_song(self, event=None):
        self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)
        file = Data.filelist[self.listWidget.currentRow()]
        print("next song")
        self.play_song(file)

    def stop(self, event):
        self.play_button.setPixmap(self.pixmap)
        self.player.stop()

    def closeEvent(self, event):
        self.state = 'close_app'
        try:
            self.proc.terminate()
            self.destroy(True, True)
        except:
            pass
        if self.my_thread.is_alive():
            pyglet.app.exit()
        if self.my_thread2.is_alive():
            self.my_thread2.join()
        if self.song_timer.isActive():
            self.song_timer.stop()
        if self.stream_timer.is_alive():
            self.stream_timer.cancel()



def show_alert():
    msgBox = QMessageBox()
    msgBox.setText('Stream is not available')
    msgBox.exec()


class SelectStreamDialog(QDialog, Ui_StreamInputDialog):
    def __init__(self, root):
        super(SelectStreamDialog, self).__init__()
        self.setupUi(self)
        self.main = root
        self.buttonBox.accepted.connect(self.add_stream)
        self.buttonBox.rejected.connect(self.close)
        self.number = 1

    def add_stream(self):
        Data.filelist = []
        self.main.listWidget.clear()
        stream = self.lineEdit.text()
        playlist = m3u_parser.load(stream)
        Data.pls_content = playlist.content
        if self.main.song_timer.isActive():
            self.main.song_timer.stop()
        if self.main.playlistWidget.currentItem():
            file = f'{self.main.dirpath}/{self.main.playlistWidget.currentItem().text()}'
            if file != stream:
                self.main.playlistWidget.currentItem().setSelected(False)
        for i in playlist.urls:
            self.main.listWidget.addItem(i.title)
            Data.streamlist.append(i.url)
            Data.pics.append(i.picture)


lock = Lock()


class Data:
    row = None
    filelist = []
    pics = []
    streamlist = []
    pls_content = str()
    state = str()


threadlock = Lock


class MyThread(Thread):
    def __init__(self, player):
        super(MyThread, self).__init__()
        self.player = player

    def run(self):
        # time.sleep(10)
        self.player.play()


def main():
    app = QApplication(sys.argv)
    window = PlayerApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
