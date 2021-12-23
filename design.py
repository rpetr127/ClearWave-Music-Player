# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainJNhnRx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from path import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 495)
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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 80, 271, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.playlistWidget = QListWidget(self.centralwidget)
        self.playlistWidget.setObjectName(u"playlistWidget")
        self.playlistWidget.setGeometry(QRect(290, 80, 241, 371))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(190, 10, 191, 41))
        self.mLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.mLayout.setObjectName(u"mLayout")
        self.mLayout.setContentsMargins(0, 0, 0, 0)
        self.imgWidget = QLabel(self.horizontalLayoutWidget)
        self.imgWidget.setObjectName(u"imgWidget")

        self.mLayout.addWidget(self.imgWidget)

        self.metadataWidget = QLabel(self.horizontalLayoutWidget)
        self.metadataWidget.setObjectName(u"metadataWidget")

        self.mLayout.addWidget(self.metadataWidget, 1, Qt.AlignLeft)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 50))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prev_button = QLabel(self.layoutWidget)
        self.prev_button.setObjectName(u"prev_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_button.sizePolicy().hasHeightForWidth())
        self.prev_button.setSizePolicy(sizePolicy)
        self.prev_button.setPixmap(QPixmap(prev_icon))

        self.horizontalLayout.addWidget(self.prev_button)

        self.play_button = QLabel(self.layoutWidget)
        self.play_button.setObjectName(u"play_button")
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setPixmap(QPixmap(play_icon))

        self.horizontalLayout.addWidget(self.play_button)

        self.forward_button = QLabel(self.layoutWidget)
        self.forward_button.setObjectName(u"forward_button")
        sizePolicy.setHeightForWidth(self.forward_button.sizePolicy().hasHeightForWidth())
        self.forward_button.setSizePolicy(sizePolicy)
        self.forward_button.setPixmap(QPixmap(forward_icon))

        self.horizontalLayout.addWidget(self.forward_button)

        self.stop_button = QLabel(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setPixmap(QPixmap(stop_icon))

        self.horizontalLayout.addWidget(self.stop_button)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 50, 521, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(499)
        self.horizontalSlider.setTickInterval(500)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("ClearWave Music Player", u"ClearWave Music Player", None))
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
        self.stop_button.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

