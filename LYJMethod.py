import datetime
import re
import os
def getTimePage(timepage):
    drawDigit=re.sub("\D", "", timepage)
    if len(drawDigit)==1:
        return getDayTime(-int(drawDigit))
    elif timepage.find('前天')>=0:
        return getDayTime(-2)
    elif timepage.find('昨天')>=0:
        return getDayTime(-1)
    elif timepage.find('小时前')>=0:
        f1 = re.findall('(\d+)', drawDigit)
        return (datetime.datetime.now()-datetime.timedelta(minutes=int(f1[0])*60)).strftime("%Y-%m-%d");
    else:
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", timepage)
        dt = datetime.datetime.strptime(mat.group(0), '%Y-%m-%d')
        return dt.strftime('%Y-%m-%d')
    return timepage

def getDayTime(days):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days)
    n_days = now + delta
    return n_days.strftime('%Y-%m-%d')

def isNetwork():
    exit_code=os.system('ping www.baidu.com')
    if exit_code:
        return False
    else:
        return True