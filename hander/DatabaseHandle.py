import MySQLdb
import gc

import pandas as pd


class DataBaseHandle(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host='106.54.212.47',
                                    port=3306,
                                    user='liyuanjinglyj',
                                    passwd='mmqqscaini1314',
                                    db='yxlr_database',
                                    charset='utf8')
        self.cursor = self.conn.cursor()  # 创建一个Cursor

    def get_dataFrame(self):
        self.df = pd.read_sql_query('SELECT * FROM mtable_yxlr', con=self.conn)
        return self.df

    def select_table(self, name, title, device, year, month):
        whereStr = ''
        s_date=None
        if year is not None:
            s_date=str(year)
        if month is not None:
            if int(month) < 10:
                s_date+='-0'+str(month)
            else:
                s_date+='-'+str(month)
        if title is not None:  # 如果标题查询不为空
            whereStr += 's_title like "%' + title + '%"  '
        if name is not None:  # 如果昵称查询不为空
            if title is None:  # 如果标题查询为空
                whereStr += 's_nameId like "%' + name + '%"  '
            else:
                whereStr += 'and s_nameId like "%' + name + '%"  '
        if device is not None:  # 如果浏览量查询不为空
            if title is None and name is None:  # 如果前两个条件都为空
                whereStr += 's_device like "%' + device + '%"  '
            else:
                whereStr += 'and s_device like "%' + device + '%"  '
        if s_date is not None:  # 如果浏览量查询不为空
            if title is None and name is None and device is None:  # 如果前两个条件都为空
                whereStr += 's_date like "%' + s_date + '%"  '
            else:
                whereStr += 'and s_date like "%' + s_date + '%"  '
        sql = 'SELECT * FROM mtable_yxlr WHERE {whereStr}'.format(whereStr=whereStr)
        df = pd.read_sql_query(sql, con=self.conn)
        return df

    def close_database(self):
        self.cursor.close()  # 关闭Cursor
        self.conn.close()  # 关闭数据库
        del self.cursor
        del self.conn
        gc.collect()
