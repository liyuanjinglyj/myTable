import gc
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from pandas import DataFrame

from hander.DatabaseHandle import DataBaseHandle


class queryThread(QtCore.QThread):
    _signal = pyqtSignal(DataFrame)

    def __init__(self):
        super(queryThread, self).__init__()

    def setValue(self,s_nameId,s_title,s_device,year,month):
        self.queryPar = [s_nameId, s_title,s_device, year, month]

    def run(self):
        self.databasehandler = DataBaseHandle()
        datalist=DataFrame()
        datalist = self.databasehandler.select_table(self.queryPar[0], self.queryPar[1], self.queryPar[2], self.queryPar[3],
                                               self.queryPar[4])
        self.databasehandler.close_database()
        self._signal.emit(datalist)
        del datalist, self.queryPar, self.databasehandler
        gc.collect()
