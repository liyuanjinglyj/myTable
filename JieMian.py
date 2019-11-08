import re
import sys
import os
import openpyxl
import qdarkstyle
import apprcc_rc
import numpy as np
import LYJMethod
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QTableWidget, QApplication, QHBoxLayout, QMenu, \
    QAbstractItemView, QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, QInputDialog
from qtpy import QtWidgets, QtCore
from openpyxl.styles import Font
from ExcelHandle import ExcelHandle
from get_RunnThread import getRunnThread
from oneAction import Ui_widget
from piewidget.pieWidget import pieWidget
from plotwidget.plotWidget import Ui_Form
from querywidget.querywidget import queryWidget


class MyFrom(QMainWindow):
    colList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    flag = True

    def __init__(self, parent=None):
        super(MyFrom, self).__init__(parent=parent)
        self.setWindowTitle('鹏飞小哥专用')
        self.resize(1210, 320)
        self.init_Action()
        self.init_toolbar()
        self.init()

    # 初始化tableWidget
    def init(self):
        self.setWindowIcon(QIcon(':/pic/images/title.ico'))
        self.conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget(100, 7)
        self.myWidget = QWidget()
        self.conLayout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['发布时间', '论坛ID', '帖子标题', '链接', '阅读量', '评论量', '盖章'])  # 设置表头信息
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)  # 设置tableWidget右键菜单的响应方法
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置tableWidget不可编辑
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 设置tableWidget可以自己拉伸列宽
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选中只能选中一列
        self.tableWidget.setColumnWidth(0, 120)  # 设置第一列宽
        self.tableWidget.setColumnWidth(1, 120)  # 设置第二列宽
        self.tableWidget.setColumnWidth(2, 300)  # 设置第三列宽
        self.tableWidget.setColumnWidth(3, 300)  # 设置第四列宽
        # 设置tableWidget点击表头排序
        self.tableWidget.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortActionToolbar)
        self.myWidget.setLayout(self.conLayout)
        self.setCentralWidget(self.myWidget)

    # 添加工具栏
    def init_toolbar(self):
        oneToolbar = self.addToolBar('菜单')
        deleteAction = QAction(QIcon(':/pic/images/delete.png'), '清空所有数据', self)
        oneToolbar.addAction(deleteAction)
        inputAction = QAction(QIcon(':/pic/images/input.png'), '手动输入', self)
        oneToolbar.addAction(inputAction)
        importAction = QAction(QIcon(':/pic/images/import.png'), '批量导入', self)
        oneToolbar.addAction(importAction)
        deleteOneRowAction = QAction(QIcon(':/pic/images/deleteOneRow.png'), '删除某行', self)
        oneToolbar.addAction(deleteOneRowAction)
        getInfoAction = QAction(QIcon(':/pic/images/getInfo.png'), '获取信息', self)
        oneToolbar.addAction(getInfoAction)
        exportAction = QAction(QIcon(':/pic/images/export.png'), '批量导出', self)
        oneToolbar.addAction(exportAction)
        oneToolbar.actionTriggered[QAction].connect(self.toolbtnpressed)
        oneToolbar.setMovable(False)

        twoToolbar = self.addToolBar('列表操作')
        firstAction = QAction(QIcon(':/pic/images/firstPage.ico'), '定位到第一行', self)  # 定位到第一行
        twoToolbar.addAction(firstAction)
        lastAction = QAction(QIcon(':/pic/images/lastPage.ico'), '定位到最后一行', self)  # 定位到最后一行
        twoToolbar.addAction(lastAction)
        findAction = QAction(QIcon(':/pic/images/find.ico'), '查找', self)  # 查找
        twoToolbar.addAction(findAction)
        plotAction = QAction(QIcon(':/pic/images/plot.ico'), '图表功能', self)  # 查找
        twoToolbar.addAction(plotAction)
        pieAction = QAction(QIcon(':/pic/images/pie.ico'), '百分比图表', self)  # 查找
        twoToolbar.addAction(pieAction)
        twoToolbar.actionTriggered[QAction].connect(self.toolbtnpressed)
        twoToolbar.setMovable(False)

    # 设置排序的方法
    def sortActionToolbar(self, index):
        if self.flag:  # 升序
            self.tableWidget.sortItems(index, QtCore.Qt.AscendingOrder)
            self.flag = False
        else:  # 降序
            self.tableWidget.sortItems(index, QtCore.Qt.DescendingOrder)
            self.flag = True

    # 设置查找的方法
    def findAction(self):
        if not LYJMethod.isNetwork():
            QMessageBox.question(self, '消息', '没有网络，请先开启网络，才能使用查询功能',
                                 QMessageBox.Yes)
            return
        self.inputView = QtWidgets.QDialog()
        self.oneUi = queryWidget()
        self.oneUi.setupUi(self.inputView)
        self.inputView.show()
        self.inputView.exec()
        '''
        text, ok = QInputDialog.getText(self, '查找某个数据', '请输入查找的内容：')
        if ok:
            item = self.tableWidget.findItems(text, Qt.MatchExactly)
            if len(item) > 0:
                row = item[0].row()
                self.tableWidget.verticalScrollBar().setSliderPosition(row)
                self.tableWidget.selectRow(row)
            else:
                QMessageBox.question(self, '消息', '查找不到与信息有关的数据',
                                     QMessageBox.Yes)
                                     '''

    # 定位到第一行
    def onePageAction(self):
        self.tableWidget.verticalScrollBar().setSliderPosition(0)

    # 等位到最后一行
    def lastPageAction(self):
        tableData = self.tableWidget.item(0, 3)
        if '' == tableData or tableData is None:
            QMessageBox.question(self, '消息', '已经是最后一行',
                                 QMessageBox.Yes)
        else:
            rows = self.tableWidget.rowCount()
            for rows_index in range(rows):
                tableData = self.tableWidget.item(rows_index, 3)
                if '' == tableData or tableData is None:
                    self.tableWidget.verticalScrollBar().setSliderPosition(rows_index - 1)
                    break

    def plotAction(self):
        if not LYJMethod.isNetwork():
            QMessageBox.question(self, '消息', '没有网络，请先开启网络，才能使用图表功能',
                                 QMessageBox.Yes)
            return
        self.inputView = QtWidgets.QDialog()
        self.oneUi = Ui_Form()
        self.oneUi.setupUi(self.inputView)
        self.inputView.show()
        self.inputView.exec()

    def pieAction(self):
        if not LYJMethod.isNetwork():
            QMessageBox.question(self, '消息', '没有网络，请先开启网络，才能使用百分比图表功能',
                                 QMessageBox.Yes)
            return
        self.inputView = QtWidgets.QDialog()
        self.oneUi = pieWidget()
        self.oneUi.setupUi(self.inputView)
        self.inputView.show()
        self.inputView.exec()

    # 工具栏事件
    def toolbtnpressed(self, a):
        flag = True
        if a.text() == '手动输入':
            self.oneAction()
        elif a.text() == '批量导入':
            self.twoAction()
        elif a.text() == '删除某行':
            self.threeAction()
        elif a.text() == '获取信息':
            self.fourAction()
        elif a.text() == '批量导出':
            self.fiveAction()
        elif a.text() == '清空所有数据':
            self.sixAction()
        if a.text() == '定位到第一行':
            self.onePageAction()
        elif a.text() == '定位到最后一行':
            self.lastPageAction()
        elif a.text() == '查找':
            self.findAction()
        elif a.text() == '图表功能':
            self.plotAction()
        elif a.text() == '百分比图表':
            self.pieAction()
        else:
            return

    # tableWidget右键菜单
    def generateMenu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 1000:
            menu = QMenu()
            item1 = menu.addAction('手动输入')
            item2 = menu.addAction('批量导入')
            item3 = menu.addAction('删除链接')
            item4 = menu.addAction('获取信息')
            item5 = menu.addAction('批量导出')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1:
            self.oneAction()
        elif action == item2:
            self.twoAction()
        elif action == item3:
            self.threeAction()
        elif action == item4:
            self.fourAction()
        elif action == item5:
            self.fiveAction()
        else:
            return

    # 初始化标题栏
    def init_Action(self):
        bar = self.menuBar()
        file = bar.addMenu('菜单')

        inputURL = QAction('手动输入', self)
        inputURL.setShortcut("Ctrl+Z")
        file.addAction(inputURL)

        batchImport = QAction('批量导入', self)
        batchImport.setShortcut("Ctrl+C")
        file.addAction(batchImport)

        deleteURL = QAction('删除链接', self)
        deleteURL.setShortcut("Ctrl+X")
        file.addAction(deleteURL)

        getInfor = QAction('获取信息', self)
        getInfor.setShortcut("Ctrl+V")
        file.addAction(getInfor)

        batchExport = QAction('批量导出', self)
        batchExport.setShortcut("Ctrl+S")
        file.addAction(batchExport)

        deleteData = QAction('清空数据', self)
        deleteData.setShortcut("Ctrl+D")
        file.addAction(deleteData)
        file.triggered[QAction].connect(self.qaction_clicked)

        twoAction = bar.addMenu('列表操作')
        firstAction = QAction('定位到第一行', self)
        firstAction.setShortcut("Ctrl+R")
        twoAction.addAction(firstAction)
        lastAction = QAction('定位到最后一行', self)
        lastAction.setShortcut("Ctrl+T")
        twoAction.addAction(lastAction)
        findAction = QAction('查找', self)
        findAction.setShortcut("Ctrl+F")
        twoAction.addAction(findAction)
        twoAction.triggered[QAction].connect(self.qaction_clicked)

    # 标题栏事件
    def qaction_clicked(self, q):
        if q.text() == '手动输入':
            self.oneAction()
        elif q.text() == '批量导入':
            self.twoAction()
        elif q.text() == '删除链接':
            self.threeAction()
        elif q.text() == '获取信息':
            self.fourAction()
        elif q.text() == '批量导出':
            self.fiveAction()
        elif q.text() == '清空数据':
            self.sixAction()
        elif q.text() == '定位到第一行':
            self.onePageAction()
        elif q.text() == '定位到最后一行':
            self.lastPageAction()
        elif q.text() == '查找':
            self.findAction()
        else:
            return

    # 清空数据
    def sixAction(self):
        tableData = self.tableWidget.item(0, 3)
        if '' == tableData or tableData is None:
            QMessageBox.question(self, '消息', '表格位空，不需要清除',
                                 QMessageBox.Yes)
        else:
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['发布时间', '论坛ID', '帖子标题', '链接', '阅读量', '评论量', '盖章'])

    # 批量导出
    def fiveAction(self):
        tableData = self.tableWidget.item(0, 1)
        if '' == tableData or tableData is None:
            QMessageBox.question(self, '消息', '没有输入数据或者没有完整数据，无法导出Excel',
                                 QMessageBox.Yes)
        else:
            excelHandle = ExcelHandle()
            excelHandle.create_excel()
            rows = self.tableWidget.rowCount()
            cols = self.tableWidget.columnCount()
            for row_index in range(rows):
                for col_index in range(cols):
                    tableData = self.tableWidget.item(row_index, col_index)
                    if tableData is not None:
                        if col_index == 3:
                            excelHandle.add_excle(self.colList[col_index] + str(row_index + 2),
                                                  '=HYPERLINK("%s","%s")' % (tableData.text(), tableData.text()))
                            font = Font(name='微软雅黑', size=10, bold=False, italic=False, vertAlign=None,
                                        underline='none', strike=False, color='FF000000')
                            excelHandle.setFont(self.colList[col_index] + str(row_index + 2), font)
                        else:
                            excelHandle.add_excle(self.colList[col_index] + str(row_index + 2), tableData.text())
                            font = Font(name='微软雅黑', size=10, bold=False, italic=False, vertAlign=None,
                                        underline='none', strike=False, color='FF000000')
                            excelHandle.setFont(self.colList[col_index] + str(row_index + 2), font)
                    else:
                        break
            excelHandle.save_excel(os.getcwd())
            excelHandle.close_excel()
            QMessageBox.question(self, '消息', '导出成功，请前往程序所在目录下查看',
                                 QMessageBox.Yes)

    # 获取信息
    def fourAction(self):
        tableData = self.tableWidget.item(0, 3)
        if '' == tableData or tableData is None:
            QMessageBox.question(self, '消息', '没有输入数据，无法获取',
                                 QMessageBox.Yes)
        elif not LYJMethod.isNetwork():
            QMessageBox.question(self, '消息', '没有网络，无法获取信息',
                                 QMessageBox.Yes)
        else:
            urlList = []
            rows = self.tableWidget.rowCount()
            for rows_index in range(rows):
                tableData = self.tableWidget.item(rows_index, 3)
                if '' == tableData or tableData is None:
                    break
                else:
                    urlList.append(tableData.text())
            self.thread = getRunnThread()
            self.thread.setValue(urlList)
            self.thread._signal.connect(self.getRunnThread_callbacklog)
            self.thread._flagnal.connect(self.getRunThread_flagnal_callbacklog)
            self.thread.start()

    # 获取信息回调函数
    def getRunThread_flagnal_callbacklog(self):
        QMessageBox.question(self, '消息', '数据全部获取成功',
                             QMessageBox.Yes)

    # 获取信息回调函数
    def getRunnThread_callbacklog(self, urlList):
        for j in range(0, 7):
            if j == 4 or j == 5:
                newItem = QTableWidgetItem()
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                newItem.setData(Qt.DisplayRole, int(urlList[j + 1]))
                self.tableWidget.setItem(int(urlList[0]), j, newItem)
            else:
                newItem = QTableWidgetItem(urlList[j + 1])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(int(urlList[0]), j, newItem)
        self.tableWidget.verticalScrollBar().setSliderPosition(urlList[0])

    # 删除选中行数据
    def threeAction(self):
        row_index = self.tableWidget.currentRow()
        if row_index < 0 or row_index is None:
            return
        else:
            self.tableWidget.removeRow(row_index)

    # 批量导入链接
    def twoAction(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, '选择文件', 'C:/',
                                                                'Text Files (*.txt);;Excel files(*.xlsx , *.xls)')
        if fileName_choose == '' or fileName_choose is None:
            return
        urlList = []
        if fileName_choose.endswith('.txt'):
            a = np.loadtxt('D:\\测试专用.txt', dtype=str).tolist()
            for list in a:
                if re.match(r'^https?:/{2}\w.+$', list) and list.find(
                        'club.huawei.com') >= 0:
                    urlList.append(list)
        elif fileName_choose.endswith('.xlsx') or fileName_choose.endswith('.xls'):
            wb = openpyxl.load_workbook(fileName_choose)
            sheet = wb.worksheets[0]
            for list in range(1, sheet.max_row + 1):
                if re.match(r'^https?:/{2}\w.+$', sheet['A' + str(list)].value) and sheet['A' + str(list)].value.find(
                        'club.huawei.com') >= 0:
                    urlList.append(sheet['A' + str(list)].value)
            wb.close()
        rows = self.tableWidget.rowCount()
        # cols = self.tableWidget.columnCount()
        i = 0
        for rows_index in range(rows):
            tableData = self.tableWidget.item(rows_index, 3)
            if '' == tableData or tableData is None and i < len(urlList):
                newItem = QTableWidgetItem(urlList[i])
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(rows_index, 3, newItem)
                i += 1
            elif i >= len(urlList):
                break
            else:
                continue
        QMessageBox.question(self, '消息', '获取数据成功',
                             QMessageBox.Yes)

    # 手动输入链接
    def oneAction(self):
        self.inputView = QtWidgets.QDialog()
        self.oneUi = Ui_widget()
        self.oneUi.setupUi(self.inputView)
        self.inputView.show()
        self.oneUi.mySignal.connect(self.shoudongshuruSignal)
        self.inputView.exec()

    # 手动输入链接回调函数
    def shoudongshuruSignal(self, connect):
        rows = self.tableWidget.rowCount()
        # cols = self.tableWidget.columnCount()
        for rows_index in range(rows):
            tableData = self.tableWidget.item(rows_index, 3)
            if '' == tableData or tableData is None:
                newItem = QTableWidgetItem(connect)
                newItem.setForeground(QBrush(QColor(255, 215, 0)))
                self.tableWidget.setItem(rows_index, 3, newItem)
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myUI = MyFrom()
    myUI.show()
    sys.exit(app.exec_())
