# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oneAction.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QCoreApplication
import re

from PyQt5.QtWidgets import QMessageBox


class Ui_widget(QtWidgets.QWidget):
    mySignal = pyqtSignal(str)

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(443, 134)
        self.groupBox = QtWidgets.QGroupBox(widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 421, 91))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 401, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.login = widget
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "手动输入"))
        self.groupBox.setTitle(_translate("widget", "添加俱乐部数据"))
        self.checkBox.setText(_translate("widget", "是否连续输入"))
        self.pushButton.setText(_translate("widget", "添加"))
        self.pushButton_2.setText(_translate("widget", "退出"))
        self.pushButton.clicked.connect(self.pushButton_1_clicked)
        self.pushButton_2.clicked.connect(self.login.close)

    def setValue(self, num):
        self.index = num

    def pushButton_1_clicked(self):
        if re.match(r'^https?:/{2}\w.+$', self.lineEdit.text()) and self.lineEdit.text().find('club.huawei.com')>=0:
            print("Ok.")
        else:
            QMessageBox.question(self, '消息', '网页格式错误',
                                 QMessageBox.Yes)
            return
        if self.checkBox.isChecked():
            self.mySignal.emit(self.lineEdit.text())
        else:
            self.mySignal.emit(self.lineEdit.text())
            self.login.close()
