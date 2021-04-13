# coding=utf-8
import requests
from lxml import etree
import json
import time
import pandas as pd
import re
import pymysql
import random
db = pymysql.connect(host='localhost', user='root', password='zxc123456', port=3306,db='taobao',charset='utf8')
cursor = db.cursor()
sql = 'INSERT INTO too(ALI_ID,省份,城市,行政区,标的物类型,标的物名称,拍卖次数,竞价周期,延时周期,保证金,优先购买权人,变卖预缴款,变卖价,变卖周期,监督单位,成交时间,交易类型,报名人数,出价次数,是否限购,抵押物名称,评估价格,信用,当前价格,延时次数,处置单位,结束时间,成交价格,初始价格,itemURL,经度,纬度,市场价格,加价幅度,sellOff,起拍价格,开始时间,支持贷款,围观人数,交易状态,采集时间) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
a10 = []
a11 = []
a12 = []
a13 = []
a14 = []
a15 = []
a16 = []
a17 = []
a18 = []
a19 = []
a20 = []
a21 = []
a22 = []
a23 = []
a24 = []
a25 = []
a26 = []
a27 = []
a28 = []
a29 = []
a30 = []
a31 = []
a32 = []
a33 = []
a34 = []
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    # 'referer':'https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.50.111b7ddaCAkvlS&location_code=440304&auction_source=0&city=&province=&sorder=2&st_param=ppp&auction_start_seg=ppp',
    'cookie':'enc=K33Bnjyg5lxFs7ONNAP2Y7SuUfLtAdJe3aOud9MoyqkQM900ffLKKL3Jke6jLdnz1UMrM96ZGtOdE%2BBjo79hGg%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; t=ffff8315a790b80c1367b4e4092f67f1; _uab_collina=160942154893772949208428; _m_h5_tk=d41356c6e91150171171a2ee374ff3a6_1609479116285; _m_h5_tk_enc=f7ab7fbcf738755436752aab5a937fb5; xlly_s=1; cna=Ki9WF6Po63sCAXjmyIkbgKhF; mt=ci=41_1; _samesite_flag_=true; cookie2=29615c60d2b1495489efc2f4b3746565; _tb_token_=716335f11b403; sgcookie=E100qeHY9RQcipjJGBpc0xrTM3lRchUIJD1UG1sJHY38%2BOo3lwlHLo0uR%2F7LVHqRthe6DlfQadBd1pzrHUUlU1gUOA%3D%3D; unb=4201607589; uc1=existShop=false&cookie14=Uoe0ZNHBlVjNcQ%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&pas=0&cookie15=URm48syIIVrSKA%3D%3D&cookie21=V32FPkk%2FgPzW; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dCuAAmef9ASoxZhl8%3D&id2=Vy64MHc652zmCg%3D%3D&nk2=F5RBxEvyGEteGuw%3D; csg=31614cc7; lgc=tb419516608; cookie17=Vy64MHc652zmCg%3D%3D; dnk=tb419516608; skt=8a2afdee41ad54a3; existShop=MTYwOTc2MzMwOQ%3D%3D; uc4=nk4=0%40FY4KoeysZvXhz8XusHkgn10QyF3WKQ%3D%3D&id4=0%40VXkfhEAyXmG2aXL2HVU1lOuzmoSD; tracknick=tb419516608; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=89f; _nk_=tb419516608; cookie1=W8CNutpfKjAz0ZpQ4tnQaHMW8R2FOeOf42DA3C6ieDs%3D; l=eBxZzgQqQ9_a988oBOfZhurza77TMIRfguPzaNbMiOCPOUfp5gghWZ8DhSL9CnGVns36R3uKcXmQBb8gqyUBh-VvSDTmaHACQdTh.; tfstk=cDuVB7spgELquuz6vraNfuLoFFaAZQegdaPUmcOef-d1FWEciIWTZQ6Ta5yprof..; isg=BPb2HLfftbKeBkBFyF2eGnEoRyz4FzpRzUaCv2DfY1l1o5c9yKTzYd1Ru3_PCzJp; x5sec=7b22617365727665723b32223a223632363066383161623330316266373063643762613837343037363439663464434d76467a5038464550473972595364672f726479674561445451794d4445324d4463314f446b374d54513d227d'}
proxy={
    'http':'106.54.172.70:16819'
}
df = pd.read_csv('拍卖地址3(1).csv',encoding='gbk')
df1 = df['城市'].values.tolist()
df2 = df['地区'].values.tolist()
df3 = df['url'].values.tolist()
df4 = df['页码'].values.tolist()
for k in range(len(df1)):
    for kj in range(1,int(df4[k])+1):

        urll = "https:"+df3[k].strip()+'&page={}'.format(kj)

        print(urll)
        headers['user-agent'] = MY_USER_AGENT[random.randint(0,34)]

        response = requests.get(urll,headers=headers,proxies=proxy)

        content =response.content
        html = etree.HTML(content)
        a = html.xpath('//script[@id="sf-item-list-data"]/text()')
        for i in a:
            item_json = json.loads(i)
            data = item_json['data']
            for g in data:
                timeArray = time.localtime(int(g['start']) / 1000)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                a1.append(g['id'])
                a2.append(g['title'])
                a11.append(g['applyCount'])
                a12.append(g['bidCount'])
                a13.append(g['buyRestrictions'])
                a15.append(g['credit'])
                a16.append(g['currentPrice'])
                a17.append(g['delayCount'])
                a21.append(g['initialPrice'])
                a22.append(g['itemUrl'])
                a25.append(g['marketPrice'])
                a27.append(g['sellOff'])
                a29.append(otherStyleTime)
                a30.append(g["supportOrgLoan"])
                a31.append(g['viewerCount'])
                a32.append(g['status'])
                timeend = time.localtime(int(g['end']) / 1000)
                Timeend = time.strftime("%Y-%m-%d %H:%M:%S", timeend)
                a19.append(Timeend)
                a33.append(df1[k])
                a34.append(df2[k])

        for p in a22:

            url = 'https:' + p
            headers['user-agent'] = MY_USER_AGENT[random.randint(0, 34)]
            res = requests.get(url, headers=headers,proxies=proxy)

            cont = res.content
            ht = etree.HTML(cont)
            all = ht.xpath('//tbody[@id="J_HoverShow"]//text()')
            l = str(all)
            ao = l.replace(r'\n', '').replace('[', '').replace(']', '').replace(' ', '').replace(',', '')
            o = re.sub("'", "", ao)
            baozheng = re.findall(r'保证金:¥(.*?)\D', o)  # 保证金
            youxian = re.findall(r'优先购买权人:(.*?)\D', o)  # 优先购买权人
            yanshi = re.findall(r'延时周期:(.*?)\D', o)  # 延时周期
            qipaijia = re.findall(r'起拍价:¥(.*?)\D', o)  # 起拍价
            jinjia = re.findall(r'竞价周期:(.*?)\D', o)  # 竞价周期
            pingu = re.findall(r'评估价:(.*?)\D', o)  # 评估
            print(baozheng)

            chengjiao = ht.xpath('//span[@class="pm-current-price J_Price"]/em/text()')  # 成交价
            chengjiaotime = ht.xpath('//span[@class="countdown J_TimeLeft"]/text()')  # 成交时间
            jin = ht.xpath('//input[@id="J_Coordinate"]/@value')  # 经纬度
            fudu = re.findall(r'加价幅度:¥(.*?)\D', o)  # 加价幅度

            chuzhi = ht.xpath('//span[@class="unit-txt unit-name item-announcement"]/a/text()')  # 处置单位
            cishu = ht.xpath('//div[@class = "pm-main clearfix"]/h1/span/text()')  # 拍卖次数

            if len(cishu):
                a3.append(cishu[0])
            else:
                a3.append('')
            jinjiag = ht.xpath('//tbody[@id="J_HoverShow"]/tr[1]/td[3]/span[2]/text()')  # 竞价周期

            # timeend = time.localtime(int(g['end']) / 1000)
            # Timeend = time.strftime("%Y-%m-%d %H:%M:%S", timeend)

            if len(jinjiag):
                a4.append(jinjiag[0].replace(':', ''))
            else:
                a4.append('')

            # a5.append(yanshi)
            if len(yanshi):
                a5.append(yanshi[0])
            else:
                a5.append('')

            if len(baozheng):
                a6.append(baozheng[0])
            else:
                a6.append('')
            # a6.append(baozheng)
            # a7.append(youxian)
            if len(youxian):
                a7.append(youxian[0])
            else:
                a7.append('')
            if len(chengjiaotime):
                a10.append(chengjiaotime[0])
            else:
                a10.append('')
            # a10.append(chengjiaotime)
            if len(pingu):
                a14.append(pingu[0])
            else:
                a14.append('')

            # a14.append(pingu)
            # a18.append(chuzhi)
            if len(chuzhi):
                a18.append(chuzhi[0])
            else:
                a18.append('')
            # a19.append(Timeend)
            if len(chengjiao):
                a20.append(chengjiao[0])
            else:
                a20.append('')
            # a20.append(chengjiao)
            if len(jin):

                a23.append(jin[0].split(',')[1])
                a24.append(jin[0].split(',')[0])
            else:
                a23.append('')
                a24.append('')

            # a26.append(fudu)
            # a28.append(qipaijia)
            if len(fudu):
                a26.append(fudu[0])
            else:
                a26.append('')
            if len(qipaijia):
                a28.append(qipaijia[0])
            else:
                a28.append('')

        for ppp in range(len(a16)):
            cursor.execute(sql, (
            a1[ppp], '河北', a33[ppp], a34[ppp],"住宅用房", a2[ppp], a3[ppp], a4[ppp], a5[ppp], a6[ppp], a7[ppp], '', '', '','', a10[ppp], '拍卖人数', a11[ppp], a12[ppp], a13[ppp], a2[ppp], a14[ppp], a15[ppp], a16[ppp], a17[ppp], a18[ppp], a19[ppp], a20[ppp], a21[ppp], a22[ppp],
            a23[ppp], a24[ppp], a25[ppp], a26[ppp], a27[ppp], a28[ppp], a29[ppp], a30[ppp], a31[ppp], a32[ppp], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        db.commit()
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []
        a9 = []
        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []
        a16 = []
        a17 = []
        a18 = []
        a19 = []
        a20 = []
        a21 = []
        a22 = []
        a23 = []
        a24 = []
        a25 = []
        a26 = []
        a27 = []
        a28 = []
        a29 = []
        a30 = []
        a31 = []
        a32 = []
        a33 = []
        a34 = []
            
            

# ccc = pd.DataFrame({"ALI_ID":a1,"省份":'广东',"城市":a33,"行政区":a34,"标的物类型":"住宅用房","标的物名称":a2,"拍卖次数":a3,"竞价周期":a4,"延时周期":a5,"保证金":a6,"优先购买权人":a7,
#                     "变卖预缴款":"","变卖价":"","变卖周期":'',"监督单位":'',"成交时间":a10,"交易类型":"拍卖","报名人数":a11,
#                     '出价次数':a12,'是否限购':a13,'抵押物名称':a2,"评估价格":a14,"信用":a15,'当前价格':a16,'延时次数':a17,'处置单位':a18,'结束时间':a19,"成交价格":a20,"初始价格":a21,'itemURL':a22,'经度':a23,"纬度":a24,"市场价格":a25,"加价幅度":a26,"sellOff":a27,"起拍价格":a28,"开始时间":a29,"支持贷款":a30,
#                     "围观人数":a31,"交易状态":a32,"采集时间":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#                     })
# ccc.to_csv('拍卖.csv',encoding='gbk')