import MySQLdb
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from pandas import DataFrame


class plotThread(QtCore.QThread):
    _signal = pyqtSignal(DataFrame)

    def __init__(self):
        super(plotThread, self).__init__()

    def run(self):
        db = MySQLdb.connect(host='106.54.212.47',
                             port=3306,
                             user='liyuanjinglyj',
                             passwd='mmqqscaini1314',
                             db='yxlr_database',
                             charset='utf8')
        cursor = db.cursor()
        df = pd.read_sql_query('SELECT * FROM mtable_yxlr', con=db)
        cursor.close()  # 关闭Cursor
        db.close()  # 关闭数据库
        self._signal.emit(df)