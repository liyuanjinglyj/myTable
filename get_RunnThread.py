import datetime

import requests
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from pyquery import PyQuery as py

from LYJMethod import getTimePage


class getRunnThread(QtCore.QThread):
    _signal = pyqtSignal(list)
    _flagnal = pyqtSignal(bool)

    def __init__(self):
        super(getRunnThread, self).__init__()
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Host': 'club.huawei.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }

    def setValue(self, urlList):
        self.urlList = urlList

    def run(self):
        for index, urlHtml in enumerate(self.urlList):
            list = []
            req = requests.get(url=urlHtml, headers=self.header)
            pageDoc = py(req.text)
            s_nameId = pageDoc('.authi').children('.xi2').eq(1).text().strip()  # 用户昵称
            s_title = pageDoc('#thread_subject').text()  # 帖子标题
            s_date = pageDoc('.authi').children('em').eq(1).children('span').attr('title')  # 帖子发表时间
            if s_date is None:
                s_date = getTimePage(pageDoc('.authi').children('em').eq(1).text()).strip()  # 发表时间
            if len(s_date) > 15:
                s_date = datetime.datetime.strptime(s_date, '%Y-%m-%d %H:%M:%S')
            else:
                s_date = datetime.datetime.strptime(s_date, '%Y-%m-%d')
            s_date = s_date.strftime('%Y-%m-%d')
            s_count = pageDoc('.hbw-ico.hbwi-view14')('span').text()  # 浏览量
            s_comment = pageDoc('.hbw-ico.hbwi-reply14')('span').text()  # 评论数
            s_gaizhang = pageDoc('#threadstamp')
            if s_gaizhang is not None:
                s_gaizhang = pageDoc('#threadstamp').children('img').eq(0).attr('title')  # 盖章
                if s_gaizhang == '' or s_gaizhang is None:
                    s_gaizhang = '没有盖章'
            else:
                s_gaizhang = '没有盖章'
            list.append(index)
            list.append(s_date)
            list.append(s_nameId)
            list.append(s_title)
            list.append(urlHtml)
            list.append(s_count)
            list.append(s_comment)
            list.append(s_gaizhang)
            self._signal.emit(list)
        self._flagnal.emit(True)
