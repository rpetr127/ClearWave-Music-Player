# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 287)
        self.TableWidget = QtWidgets.QTabWidget(Form)
        self.TableWidget.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.TableWidget.setObjectName("TableWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.TableWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TableWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.TableWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TableWidget.setTabText(self.TableWidget.indexOf(self.tab1), _translate("Form", "Интерфейс"))
        self.TableWidget.setTabText(self.TableWidget.indexOf(self.tab_2), _translate("Form", "Музыка"))
