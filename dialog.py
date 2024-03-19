# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogfifDif.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_StreamInputDialog(object):
    def setupUi(self, StreamInputDialog):
        if not StreamInputDialog.objectName():
            StreamInputDialog.setObjectName(u"StreamInputDialog")
        StreamInputDialog.resize(312, 115)
        self.verticalLayoutWidget = QWidget(StreamInputDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 291, 94))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.suggestionLabel = QLabel(self.verticalLayoutWidget)
        self.suggestionLabel.setObjectName(u"suggestionLabel")

        self.verticalLayout.addWidget(self.suggestionLabel)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(StreamInputDialog)
        self.buttonBox.accepted.connect(StreamInputDialog.accept)
        self.buttonBox.rejected.connect(StreamInputDialog.reject)

        QMetaObject.connectSlotsByName(StreamInputDialog)
    # setupUi

    def retranslateUi(self, StreamInputDialog):
        StreamInputDialog.setWindowTitle(QCoreApplication.translate("StreamInputDialog", u"Dialog", None))
        self.suggestionLabel.setText(QCoreApplication.translate("StreamInputDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 URL \u0440\u0430\u0434\u0438\u043e\u0441\u0442\u0430\u043d\u0446\u0438\u0438:", None))
    # retranslateUi

