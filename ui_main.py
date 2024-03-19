# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainfECmmA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from path import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(512, 545)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionOpen_folder = QAction(MainWindow)
        self.actionOpen_folder.setObjectName(u"actionOpen_folder")
        self.actionOpen_URL = QAction(MainWindow)
        self.actionOpen_URL.setObjectName(u"actionOpen_URL")
        self.actionCreate_playlist = QAction(MainWindow)
        self.actionCreate_playlist.setObjectName(u"actionCreate_playlist")
        self.actionSave_playlist = QAction(MainWindow)
        self.actionSave_playlist.setObjectName(u"actionSave_playlist")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen_playlist = QAction(MainWindow)
        self.actionOpen_playlist.setObjectName(u"actionOpen_playlist")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(10)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.mLayout = QHBoxLayout()
        self.mLayout.setObjectName(u"mLayout")
        self.imgWidget = QLabel(self.centralwidget)
        self.imgWidget.setObjectName(u"imgWidget")

        self.mLayout.addWidget(self.imgWidget)

        self.metadataWidget = QLabel(self.centralwidget)
        self.metadataWidget.setObjectName(u"metadataWidget")

        self.mLayout.addWidget(self.metadataWidget)

        self.verticalLayout.addLayout(self.mLayout)

        self.cLayout = QHBoxLayout()
        self.cLayout.setObjectName(u"horizontalLayout")
        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")
        icon = QIcon()
        icon.addFile(prev_icon, QSize(), QIcon.Normal, QIcon.On)
        self.prev_button.setIcon(icon)

        self.cLayout.addWidget(self.prev_button)

        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        icon1 = QIcon()
        icon1.addFile(play_icon, QSize(), QIcon.Normal, QIcon.On)
        self.play_button.setIcon(icon1)

        self.cLayout.addWidget(self.play_button)

        self.forward_button = QPushButton(self.centralwidget)
        self.forward_button.setObjectName(u"forward_button")
        self.forward_button.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(forward_icon, QSize(), QIcon.Normal, QIcon.On)
        self.forward_button.setIcon(icon2)
        self.forward_button.setFlat(False)

        self.cLayout.addWidget(self.forward_button)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"pushButton")
        icon3 = QIcon()
        icon3.addFile(stop_icon, QSize(), QIcon.Normal, QIcon.On)
        self.stopButton.setIcon(icon3)

        self.cLayout.addWidget(self.stopButton)

        self.verticalLayout.addLayout(self.cLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.playlistWidget = QListWidget(self.centralwidget)
        self.playlistWidget.setObjectName(u"playlistWidget")

        self.horizontalLayout.addWidget(self.playlistWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 546, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionOpen_folder)
        self.menu.addAction(self.actionOpen_URL)
        self.menu.addSeparator()
        self.menu.addAction(self.actionOpen_playlist)
        self.menu.addAction(self.actionSave_playlist)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ClearWave Music Player", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.actionOpen_folder.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.actionOpen_URL.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c URL", None))
        self.actionCreate_playlist.setText(QCoreApplication.translate("MainWindow", u"Create playlist", None))
        self.actionSave_playlist.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438", None))
        self.actionOpen_playlist.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.imgWidget.setText("")
        self.metadataWidget.setText("")
        self.prev_button.setText("")
        self.play_button.setText("")
        self.forward_button.setText("")
        self.stopButton.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

