# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querywidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from querywidget.queryThread import queryThread


class queryWidget(QtWidgets.QWidget):
    flag = True
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1380, 394)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 180, 1310, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1000)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(310, 0, 710, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.thread = queryThread()
        self.thread._signal.connect(self.pushButton_callbacklog)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询"))
        self.label_5.setText(_translate("Form", "标题："))
        self.label.setText(_translate("Form", "昵称："))
        self.label_2.setText(_translate("Form", "设备："))
        self.label_3.setText(_translate("Form", "年："))
        self.label_4.setText(_translate("Form", "月"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.comboBox.activated.connect(self.comboBox_clicked)
        self.comboBox_2.setEnabled(False)
        self.init_view()
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def comboBox_clicked(self):
        if self.comboBox.currentText()=='不选':
            self.comboBox_2.setEnabled(False)
            self.comboBox_2.clear()
            self.comboBox_2.addItem("不选")
            for month in range(1, 13):
                self.comboBox_2.addItem(str(month))
        else:
            self.comboBox_2.setEnabled(True)

    def pushButton_clicked(self):
        if len(self.lineEdit.text()) > 0 or len(self.lineEdit_2.text()) > 0 or len(self.lineEdit_3.text()) > 0 or self.comboBox.currentText().find(
            '不选') != 0 or self.comboBox_2.currentText().find('不选') != 0:
            oneValue = None#昵称
            threeValue = None#设备
            fourValue = None#年
            fiveValue = None#月
            twoValue = None#标题
            if len(self.lineEdit.text()) > 0:#昵称
                oneValue = self.lineEdit.text()
            if len(self.lineEdit_2.text()) > 0:#设备
                threeValue = self.lineEdit_2.text()
            if len(self.lineEdit_3.text()) > 0:#标题
                twoValue = self.lineEdit_3.text()
            if self.comboBox.currentText().find('不选'):
                fourValue = self.comboBox.currentText()
            if self.comboBox_2.currentText().find('不选'):
                fiveValue = self.comboBox_2.currentText()
            self.thread.setValue(oneValue, twoValue, threeValue, fourValue, fiveValue)
            self.thread.start()
        else:
            reply = QMessageBox.question(self.centralwidget, '消息', '需要输入一个查询条件',
                                         QMessageBox.Yes)

    def init_view(self):
        now = datetime.datetime.now()
        self.comboBox_2.addItem("不选")
        self.comboBox.addItem("不选")
        for year in range(2017, now.year + 1):
            self.comboBox.addItem(str(year))
        for month in range(1, 13):
            self.comboBox_2.addItem(str(month))
        self.tableWidget.setHorizontalHeaderLabels(['发布时间', '论坛ID', '帖子标题', '链接', '阅读量', '评论量', '盖章', '设备'])  # 设置表头信息
        self.tableWidget.setColumnWidth(0, 120)  # 设置第一列宽
        self.tableWidget.setColumnWidth(1, 120)  # 设置第二列宽
        self.tableWidget.setColumnWidth(2, 300)  # 设置第三列宽
        self.tableWidget.setColumnWidth(3, 300)  # 设置第四列宽
        self.tableWidget.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortActionToolbar)

    # 设置排序的方法
    def sortActionToolbar(self, index):
        if self.flag:  # 升序
            self.tableWidget.sortItems(index, QtCore.Qt.AscendingOrder)
            self.flag = False
        else:  # 降序
            self.tableWidget.sortItems(index, QtCore.Qt.DescendingOrder)
            self.flag = True

    def pushButton_callbacklog(self, msg):
        self.tableWidget.clear()
        if len(msg) <= 0:
            QMessageBox.question(self, '消息', '没有符合查询条件的数据',
                                         QMessageBox.Yes)
            self.tableWidget.setHorizontalHeaderLabels(
                ['发布时间', '论坛ID', '帖子标题', '链接', '阅读量', '评论量', '盖章', '设备'])  # 设置表头信息
        else:
            self.tableWidget.setHorizontalHeaderLabels(
                ['发布时间', '论坛ID', '帖子标题', '链接', '阅读量', '评论量', '盖章', '设备'])  # 设置表头信息
            for index, row in msg.iterrows():
                newItem = QTableWidgetItem(row['s_date'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row['s_nameId'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(row['s_title'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(row['s_url'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem()
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                newItem.setData(Qt.DisplayRole, row['s_count'])
                self.tableWidget.setItem(index, 4, newItem)
                newItem = QTableWidgetItem()
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                newItem.setData(Qt.DisplayRole, row['s_comment'])
                self.tableWidget.setItem(index, 5, newItem)
                newItem = QTableWidgetItem(row['s_gaizhang'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 6, newItem)
                newItem = QTableWidgetItem(row['s_device'])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(index, 7, newItem)