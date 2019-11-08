import calendar
import numpy as np
import pandas  as pd
import MySQLdb
import matplotlib
import matplotlib.pyplot as plt
'''
flaglist=calendar.monthrange(2019,8)
print(str(2017)+'-'+str(flaglist[0])+'-'+str(flaglist[1]))
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
df = pd.read_excel(r'E:\Projects\PyCharmProjects\myTable\shuju.xlsx')
df['s_date'] = pd.to_datetime(df['s_date'])
df = df.set_index('s_date')
sum_df = df.groupby('s_device', as_index=False)
print(sum_df)
x = []
y = []
for name, group in sum_df:
    data = group.resample('M').count().reset_index(drop=False)
    data2 = data[data['s_date'] == '2018-8-31']
    if len(data2.values.tolist()) <= 0 or data2.values.tolist()[0][3] <= 0:
        continue
    else:
        x.append(data2.values.tolist()[0][3])
        y.append(name)
plt.pie(x, labels=y, autopct='%1.1f%%',textprops={'fontsize': 8, 'color': 'blue'})
plt.legend( loc = 'upper right',bbox_to_anchor=(1.1, 1.05), fontsize=14, borderaxespad=0.3)
plt.show()
'''
'''
plt.pie(x,labels=y, autopct='%1.1f%%')
plt.show()

'''
print('------------------------------------------')
'''
#根据每月帖子输出总数，占比画pie图
data = df.resample('M').count().reset_index(drop=False)  # 每个月总帖子数
data2 = df[df['s_nameId'] == '云月静'].resample('M').count().reset_index(drop=False)  # 每个月云月静总帖子数
data3 = data2[data2['s_date'] == '2018-3-31']
print(data3)
x = [100 - int(data3['id']), int(data3['id'])]
y = [u'其他', u'云月静']
df = pd.read_excel(r'E:\Projects\PyCharmProjects\myTable\shuju.xlsx')
df['s_date'] = pd.to_datetime(df['s_date'])
df = df.set_index('s_date')
sum_df = df.groupby('s_nameId', as_index=False)
print(sum_df)
x = []
y = []
for name, group in sum_df:
    data = group.resample('M').count().reset_index(drop=False)  # 每个总帖子数
    data2 = data[data['s_date'] == '2018-3-31']
    print(data2.values.tolist())
    if len(data2.values.tolist()) <= 0 or data2.values.tolist()[0][3]<=2:
        continue
    else:
        x.append(data2.values.tolist()[0][3])
        y.append(name)
print(x)
print(len(x))
print(y)
print(len(y))
fig = plt.figure()
axes = fig.add_subplot(111)
axes.pie(x, labels=y, autopct='%1.1f%%',textprops={'fontsize': 8, 'color': 'blue'})
axes.legend( loc = 'upper right',bbox_to_anchor=(1.1, 1.05), fontsize=14, borderaxespad=0.3)
axes.suptitle('当月输出占比', fontsize=20)
axes.show()
'''
'''
data=group.resample('M').count().reset_index(drop=False)#每个月总帖子数
    data2=df[df['s_nameId']==name].resample('M').count().reset_index(drop=False)#每个月云月静总帖子数
    data3=data[data['s_date']=='2018-3-31']

df = pd.read_excel(r'E:\Projects\PyCharmProjects\myTable\shuju.xlsx')
df['日期'] = pd.to_datetime(df['日期'])
print(df['日期'][0].year)
df=df.set_index('日期',drop=True, append=False, inplace=False, verify_integrity=False)
data = df[df['昵称'] == '云月静'].resample('M').sum().reset_index(drop=False)
print('---------------------------')
data=df[df['昵称'] == '云月静'].resample('M')['浏览量'].max().reset_index(drop=False)
for index, row in data.iterrows():
    print(pd.isnull(row['浏览量']))
#print(df[df['昵称'] == '云月静'].resample('M').count())
#data=df[('2019-01-01'):('2019-01-31')]['昵称']=='欢乐的小机友'
#print(df[('2019-01-01'):('2019-01-31')][data])
'''
'''
df['year'], df['month']= df['日期'].dt.year, df['日期'].dt.month
print(df.loc[(df['year'] == 2019) & (df['month'] == 2)])
'''
'''
a=np.loadtxt('D:\\测试专用.txt',dtype=str)
print(a.tolist())
print(len(a.tolist()))

conn=sqlite3.connect(r'E:\Projects\Django\auction\yxlr_database')
cursor=conn.cursor()
cursor.execute("select * from yxlr")
result=cursor.fetchall()
df=pd.DataFrame(list(result))
df.to_excel('shuju.xlsx')
f = open(fileName_choose, "r")
            for list in f.readlines():
                if re.match(r'^https?:/{2}\w.+$', list.strip('\n')) and list.strip('\n').find(
                        'club.huawei.com') >= 0:
                    urlList.append(list.strip('\n'))
'''
'''
conn = sqlite3.connect(r'D:\游戏猎人\yxlr_database')  # 连接到SQLite数据库
cursor = conn.cursor()  # 创建一个Cursor
sql='create table yxlr (id integer primary key autoincrement,' \
    's_date VARCHAR(100) NOT NULL ,' \
    's_nameId VARCHAR(50) NOT NULL,' \
    's_title VARCHAR(255) NOT NULL,' \
    's_url VARCHAR(255) NOT NULL,' \
    's_count integer NOT NULL,' \
    's_comment integer NOT NULL,' \
    's_gaizhang VARCHAR(20) NOT NULL,' \
    's_device VARCHAR(20) NOT NULL)'
cursor.execute(sql)
conn.commit()  # 提交操作
cursor.close()  # 关闭Cursor
conn.close()  # 关闭数据库

conn=sqlite3.connect(r'E:\Projects\PyCharmProjects\myTable\lyj\yxlr_database')
cursor=conn.cursor()
cursor.execute("select * from yxlr")
result=cursor.fetchall()
df=pd.DataFrame(list(result))
df.to_excel('shuju.xlsx')
'''

db = MySQLdb.connect(host='106.54.212.47',
       port = 3306,
       user='liyuanjinglyj',
       passwd='mmqqscaini1314',
       db ='yxlr_database',
       charset='utf8')
cursor = db.cursor()
sql='create table mtable_yxlr (id integer primary key Auto_increment,' \
    's_date VARCHAR(100) NOT NULL ,' \
    's_nameId VARCHAR(50) NOT NULL,' \
    's_title VARCHAR(255) NOT NULL,' \
    's_url VARCHAR(255) NOT NULL,' \
    's_count integer NOT NULL,' \
    's_comment integer NOT NULL,' \
    's_gaizhang VARCHAR(20) NOT NULL,' \
    's_device VARCHAR(255) NOT NULL)engine=InnoDB DEFAULT CHARSET=utf8'
cursor.execute(sql)
db.close()

'''
db = MySQLdb.connect(host='cdb-qmdxisun.gz.tencentcdb.com',
       port = 10029,
       user='root',
       passwd='mmqqscaini1314',
       db ='yxlr_database',
       charset='utf8')
cursor = db.cursor()
wb = openpyxl.load_workbook(r'E:\Projects\PyCharmProjects\myTable\shuju.xlsx')
sheet = wb.worksheets[0]
for htmlUrl in range(2, sheet.max_row + 1):
    sql = "INSERT INTO yxlr (s_date,s_nameId,s_title,s_url,s_count,s_comment,s_gaizhang,s_device) VALUES ('%s', '%s','%s','%s',%d,%d,'%s','%s')"
    value = (sheet['C' + str(htmlUrl)].value,
         sheet['D' + str(htmlUrl)].value,
         sheet['E' + str(htmlUrl)].value,
         sheet['F' + str(htmlUrl)].value,
         int(sheet['G' + str(htmlUrl)].value),
         int(sheet['H' + str(htmlUrl)].value),
         sheet['I' + str(htmlUrl)].value,
         sheet['J' + str(htmlUrl)].value)
    cursor.execute(sql % value)  # 使用SQL语句对数据库进行操作
db.commit()  # 提交操作
cursor.close()  # 关闭Cursor
db.close()  # 关闭数据库



db = MySQLdb.connect(host='cdb-qmdxisun.gz.tencentcdb.com',
                     port=10029,
                     user='root',
                     passwd='mmqqscaini1314',
                     db='yxlr_database',
                     charset='utf8')
cursor = db.cursor()
df = pd.read_sql_query('SELECT * FROM yxlr',con=db)
print(df)
cursor.close()  # 关闭Cursor
db.close()  # 关闭数据库
'''
