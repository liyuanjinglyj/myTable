import datetime
import sqlite3
import MySQLdb
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as py

webPage = {
    '择城终老': 'https://club.huawei.com/home.php?mod=space&uid=12609418&do=thread&view=me&order=dateline&from=space&page=',
    '落风水': 'https://club.huawei.com/home.php?mod=space&uid=88627444&do=thread&view=me&order=dateline&from=space&page=',
    '云月静': 'https://club.huawei.com/home.php?mod=space&uid=33931338&do=thread&view=me&order=dateline&from=space&page=',
    '欢乐的小机友': 'https://club.huawei.com/home.php?mod=space&uid=8227262&do=thread&view=me&order=dateline&from=space&page=',
    'Alex爱小白': 'https://club.huawei.com/home.php?mod=space&uid=46128556&do=thread&view=me&order=dateline&from=space&page=',
    '鹏飞小哥': 'https://club.huawei.com/home.php?mod=space&uid=17612241&do=thread&view=me&order=dateline&from=space&page=',
    '云谷-旅行者': 'https://club.huawei.com/home.php?mod=space&uid=40560468&do=thread&view=me&order=dateline&from=space&page=',
    '云谷择城': 'https://club.huawei.com/home.php?mod=space&uid=89132582&do=thread&view=me&order=dateline&from=space&page=',
    '彧幃': 'https://club.huawei.com/home.php?mod=space&uid=13565151&do=thread&view=me&order=dateline&from=space&page=',
    '北方有小麓': 'https://club.huawei.com/home.php?mod=space&uid=59742397&do=thread&view=me&order=dateline&from=space&page=',
    '政哥哥呦': 'https://club.huawei.com/home.php?mod=space&uid=8387250&do=thread&view=me&order=dateline&from=space&page=',
    '中箭地吴起': 'https://club.huawei.com/home.php?mod=space&uid=76954097&do=thread&view=me&order=dateline&from=space&page=',
    '海力布i': 'https://club.huawei.com/home.php?mod=space&uid=89203913&do=thread&view=me&order=dateline&from=space&page=',
    '熊猫play': 'https://club.huawei.com/home.php?mod=space&uid=87710958&do=thread&view=me&order=dateline&from=space&page=',
    'elpooo': 'https://club.huawei.com/home.php?mod=space&uid=7466695&do=thread&view=me&order=dateline&from=space&page=',
    'zhunwuzhe888': 'https://club.huawei.com/home.php?mod=space&uid=83471316&do=thread&view=me&order=dateline&from=space&page=',
    '八百斤的猫': 'https://club.huawei.com/home.php?mod=space&uid=45336777&do=thread&view=me&order=dateline&from=space&page=',
    '醉里寻魂': 'https://club.huawei.com/home.php?mod=space&uid=12023883&do=thread&view=me&order=dateline&from=space&page=',
    'EVIL丶SEN': 'https://club.huawei.com/home.php?mod=space&uid=14668381&do=thread&view=me&order=dateline&from=space&page=',
    '爱花人202': 'https://club.huawei.com/home.php?mod=space&uid=14868122&do=thread&view=me&order=dateline&from=space&page=',
    '简单比什么都好': 'https://club.huawei.com/home.php?mod=space&uid=15074419&do=thread&view=me&order=dateline&from=space&page=',
    '爱の不离弃': 'https://club.huawei.com/home.php?mod=space&uid=48394683&do=thread&view=me&order=dateline&from=space&page=',
    '帅橘稚哈': 'https://club.huawei.com/home.php?mod=space&uid=51986235&do=thread&view=me&order=dateline&from=space&page=',
    '泡椒不好吃': 'https://club.huawei.com/home.php?mod=space&uid=83062279&do=thread&view=me&order=dateline&from=space&page=',
    '沙漠跳舞仙人掌': 'https://club.huawei.com/home.php?mod=space&uid=73523180&do=thread&view=me&order=dateline&from=space&page=',
    '开心_1314': 'https://club.huawei.com/home.php?mod=space&uid=44066394&do=thread&view=me&order=dateline&from=space&page=',
    '我有一个大太阳': 'https://club.huawei.com/home.php?mod=space&uid=49273593&do=thread&view=me&order=dateline&from=space&page=',
    '荣耀mote': 'https://club.huawei.com/home.php?mod=space&uid=16174969&do=thread&view=me&order=dateline&from=space&page=',
    '孤调': 'https://club.huawei.com/home.php?mod=space&uid=17455785&do=thread&view=me&order=dateline&from=space&page=',
    '敏感一生': 'https://club.huawei.com/home.php?mod=space&uid=43537432&do=thread&view=me&order=dateline&from=space&page=',
    '路滨': 'https://club.huawei.com/home.php?mod=space&uid=12582702&do=thread&view=me&order=dateline&from=space&page=',
    '小小磊哥': 'https://club.huawei.com/home.php?mod=space&uid=43417068&do=thread&view=me&order=dateline&from=space&page=',
    '安安安大大': 'https://club.huawei.com/home.php?mod=space&uid=17463190&do=thread&view=me&order=dateline&from=space&page=',
    '花粉小白是大神': 'https://club.huawei.com/home.php?mod=space&uid=44144333&do=thread&view=me&order=dateline&from=space&page=',
    '喵呜一口吓死你': 'https://club.huawei.com/home.php?mod=space&uid=104296589&do=thread&view=me&order=dateline&from=space&page=',
    '可爱的小疯子': 'https://club.huawei.com/home.php?mod=space&uid=62734382&do=thread&view=me&order=dateline&from=space&page=',
    '随风小达': 'https://club.huawei.com/home.php?mod=space&uid=95342990&do=thread&view=me&order=dateline&from=space&page=',
    '落风水': 'https://club.huawei.com/home.php?mod=space&uid=88627444&do=thread&view=me&order=dateline&from=space&page=',
    '顾凉辞': 'https://club.huawei.com/home.php?mod=space&uid=36850026&do=thread&view=me&order=dateline&from=space&page=',
    'Allen_Ding': 'https://club.huawei.com/home.php?mod=space&uid=37236333&do=thread&view=me&order=dateline&from=space&page=',
    '月夜独步的凡星': 'https://club.huawei.com/home.php?mod=space&uid=89362394&do=thread&view=me&order=dateline&from=space&page=',
    '起个名字唉': 'https://club.huawei.com/home.php?mod=space&uid=112355102&do=thread&view=me&order=dateline&from=space&page=',
    '孙诗语': 'https://club.huawei.com/home.php?mod=space&uid=32728576&do=thread&view=me&order=dateline&from=space&page='
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Cookie': 'HWWAFSESID=224f482bd8dc17336d; HWWAFSESTIME=1572429260867; a3ps_2132_saltkey=nIy2wJ1sEJh0NDP369f40z66FcqymHRqA88qVUx0z14tUvV%2BR6Opg4WRCpbpf0%2FH7O07fKeLYY27LF4DhBhzMuMoVhcnRvwrMWiwfzMTV%2BjGXS551jkTm%2FDm9aczV11JYXV0aGtleQ%3D%3D; a3ps_2132_lastvisit=1572425662; a3ps_2132_lastact=1572429276%09portal.php%09ajax; a3ps_2132_currentHwLoginUrl=http%3A%2F%2Fcn.club.vmall.com%2F; Hm_lvt_ac495a6d816d7387c803953f3a2637d0=1572429261,1572429275; Hm_lpvt_ac495a6d816d7387c803953f3a2637d0=1572429275; _gscu_1109330234=72429261ks5mo514; _gscs_1109330234=72429261ef0c8e14|pv:2; _gscbrs_1109330234=1; _dmpa_id=32237a36d9ed0952c4043991200011572429264120.1572429262.0.1572429262..; _dmpa_ref=%5B%22%22%2C%22%22%2C1572429262%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DkVYENlN5_cgvtmXsG5EZFSm7HZJsQPaJlXAEOK-0MZqhD8DuX0tB_1t_joDcc0cv%26wd%3D%26eqid%3Df29e415f0008b128000000065db95dcb%22%5D; _dmpa_ses_time=1572431062423; _dmpa_ses=b7cbe3c671852788aec7a0621ffb5af729b6ed2c; HuaweiID_CAS_ISCASLOGIN=true; CASLOGINSITE=1; LOGINACCSITE=1; a3ps_2132_auth=zj8nT59i9QWbXp1fg5KhHnbeEvbpco5JeqKgD6RU8z%2Foy7Rcx9LfaVIhG8OrewrIFqkjPc2XmNzmy529dJ6whPqvn2%2Bn6ppq22Vsc1Rk1Lr%2B5aPJN%2FdlGrSeyGih3Ak0kSFB8rNyjU76YX9YuQxM5stNYar9%2FU6rs9F1Y3uS5PfEO5owFvmCkZC0If4lmyU9dffSbFN1htyACzBKDLtnpJ8jIK9OKRCywXjUwSKOaVRhdXRoY29kZQ%3D%3D; a3ps_2132_sid=u_89132582; a3ps_2132_checkpm=1; udmp_cm_sign_1109330234=1'
}#cookie值记得更换
db = MySQLdb.connect(host='106.54.212.47',
                     port=3306,
                     user='liyuanjinglyj',
                     passwd='mmqqscaini1314',
                     db='yxlr_database',
                     charset='utf8')
cursor = db.cursor()
pageFlag = False  # 判断页面是否为最后一页
breakFlag = True  # 为True表示一次没有执行过
pageIndex = 1  # 记录每个用户的访问页面
days_time = datetime.datetime.strptime('2017-10-1', "%Y-%m-%d")  # 比较时间
for key, webValue in webPage.items():
    print(webValue)
    breakFlag = True
    pageFlag = False
    pageIndex = 1
    url = webValue + str(1)
    req = requests.get(url=url, headers=header)
    soup = BeautifulSoup(req.text, 'lxml')
    cardFlag = soup.select_one('.pgs.cl.mtm')  # 最后一页问题没有解决
    if cardFlag is not None:
        cardFlag = cardFlag.select_one('span').text.split(' ')[2]
        pageFlag = True
    while pageFlag or breakFlag:
        breakFlag = False
        print(webValue, pageIndex)
        url = webValue + str(pageIndex)
        print(url)
        req = requests.get(url=url, headers=header)
        soup = BeautifulSoup(req.text, 'lxml')
        cardTable = soup.select_one('.ebm_c').select_one('.etl').select_one('#delform').select('tr')
        for card in cardTable:
            s_title = card.select_one('.ethtit').select_one('a').text  # 帖子标题
            s_url = 'https://club.huawei.com/' + card.select_one('.ethtit').select_one('a')['href']  # 贴子URL
            s_date = card.select_one('.pcm-t').select_one('p').text  # 帖子发表时间
            cardReq = requests.get(url=s_url, headers=header)
            pageDoc = py(cardReq.text)
            s_nameId = pageDoc('.authi').children('.xi2').eq(1).text().strip()  # 用户昵称
            s_count = pageDoc('.hbw-ico.hbwi-view14')('span').text()  # 浏览量
            s_comment = pageDoc('.hbw-ico.hbwi-reply14')('span').text()  # 评论数
            s_device = pageDoc('#pt')('.z').children('a').eq(3).text()  # 设备板块
            s_gaizhang = pageDoc('#threadstamp')  # 盖章
            if s_gaizhang is not None:
                s_gaizhang = pageDoc('#threadstamp').children('img').eq(0).attr('title')
                if s_gaizhang == '' or s_gaizhang is None:
                    s_gaizhang = '没有盖章'
            else:
                s_gaizhang = '没有盖章'
            if s_count is None or '' == s_count:
                continue
            if (datetime.datetime.strptime(s_date, "%Y-%m-%d") - days_time).days < 0 or s_nameId.strip()=="开心_1314":
                pageFlag = False
                break
            s_date=datetime.datetime.strptime(s_date, "%Y-%m-%d").strftime("%Y-%m-%d")
            sql = "REPLACE INTO mtable_yxlr (s_date,s_nameId,s_title,s_url,s_count,s_comment,s_gaizhang,s_device) VALUES ('%s', '%s','%s','%s',%d,%d,'%s','%s')"
            print(s_date, s_nameId, s_title.replace("'", '"'), s_url, int(s_count), int(s_comment), s_gaizhang,
                  s_device)
            value = (
                s_date.strip(), s_nameId.strip(), s_title.strip().replace("'", '"').strip(), s_url.strip(), int(s_count), int(s_comment), s_gaizhang.strip(), s_device.strip())
            cursor.execute(sql % value)  # 使用SQL语句对数据库进行操作

        pageIndex += 1
        if cardFlag is not None:
            if pageIndex == int(cardFlag):
                pageFlag = False
db.commit()  # 提交操作
cursor.close()  # 关闭Cursor
db.close()  # 关闭数据库
