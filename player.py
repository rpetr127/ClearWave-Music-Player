import time
from threading import Thread

import pyglet

pyglet.options['audio'] = ('directsound', 'silent')
pyglet.options['search_local_libs'] = True


class Player:
    def __init__(self):
        super().__init__()
        self.state = 'started'
        self.count = 0
        self.source_duration = float()

    def counter(self):
        self.count += 1
        if self.count == 11:
            self.count = 3

    def start_playing(self, file):
        self.state = 'playing'
        self.player = pyglet.media.Player()
        self.source = pyglet.media.load(file)
        self.source_duration = self.source.duration
        self.player.queue(self.source)
        self.player.play()
        pyglet.app.run()

    def play_song(self, file):
        pyglet.app.event_loop.exit_blocking()
        self.state = 'playing'
        self.player = pyglet.media.Player()
        self.source = pyglet.media.load(file)
        self.source_duration = self.source.duration
        self.player.queue(self.source)
        self.player.play()
        # pyglet.app.event_loop.enter_blocking()

    def seek(self, pts):
        self.player.seek(pts)

    def get_duration(self):
        pyglet.app.event_loop.exit_blocking()
        current_duration = int(self.player.time / self.source_duration * 500)
        return current_duration

    def pause(self):
        self.state = "paused"
        self.player.pause()
        pyglet.app.event_loop.exit_blocking()

    def resume(self):
        self.state = 'playing'
        pyglet.app.event_loop.enter_blocking()
        self.player.play()

    def change_song(self):
        if self.count == 0:
            self.state = 'started'
        else:
            self.state = "item_changed"

    def is_next_song(self):
        pts = round(self.player.time)
        duration = round(self.source_duration)
        print(pts, duration)
        if pts == duration - 1:
            # if self.count > 0:
            #     self.state = "item_changed"
            return True
        else:
            return False

    def stop(self):
        self.state = "stop"
        self.player.seek(0)
        self.player.delete()
        pyglet.app.event_loop.exit_blocking()