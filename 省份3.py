# coding=utf-8
import requests
from lxml import etree
import json
import time
import pandas as pd
import re
import pymysql
db = pymysql.connect(host='localhost', user='root', password='zxc123456', port=3306,db='taobao',charset='utf8')
cursor = db.cursor()
sql = 'INSERT INTO taobao(ALI_ID,省份,城市,行政区,标的物类型,标的物名称,拍卖次数,竞价周期,延时周期,保证金,优先购买权人,变卖预缴款,变卖价,变卖周期,监督单位,成交时间,交易类型,报名人数,出价次数,是否限购,抵押物名称,评估价格,信用,当前价格,延时次数,处置单位,结束时间,成交价格,初始价格,itemURL,经度,纬度,市场价格,加价幅度,sellOff,起拍价格,开始时间,支持贷款,围观人数,交易状态,采集时间) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    # 'referer': 'https://sf.taobao.com/item_list.htm?location_code=440803&category=50025969&auction_source=0&city=&province=&sorder=2&st_param=-1&auction_start_seg=-1&page=2',
    'cookie': 'enc=K33Bnjyg5lxFs7ONNAP2Y7SuUfLtAdJe3aOud9MoyqkQM900ffLKKL3Jke6jLdnz1UMrM96ZGtOdE%2BBjo79hGg%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; t=ffff8315a790b80c1367b4e4092f67f1; _uab_collina=160942154893772949208428; xlly_s=1; cna=Ki9WF6Po63sCAXjmyIkbgKhF; mt=ci=88_1; _m_h5_tk=d41356c6e91150171171a2ee374ff3a6_1609479116285; _m_h5_tk_enc=f7ab7fbcf738755436752aab5a937fb5; lgc=tb419516608; tracknick=tb419516608; _samesite_flag_=true; cookie2=19033af9f47d881a5bb74abce1dfd714; _tb_token_=e5654315e603a; sgcookie=E100IM2PVqQiorxUc%2FrxXiSv1I6Tz35Od7zEo3xiXB%2BE3LfzmhxXqGz22euKNeBdL1rTVTmHH%2Bze2cBJ0HwrOzVX%2Bg%3D%3D; unb=4201607589; uc1=cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=Uoe0ZNJkBDm12Q%3D%3D&cookie21=UtASsssme%2BBq&pas=0; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCuAAlg9937I6SsnM%3D&nk2=F5RBxEvyGEteGuw%3D&id2=Vy64MHc652zmCg%3D%3D; csg=dfb14fd7; cookie17=Vy64MHc652zmCg%3D%3D; dnk=tb419516608; skt=acf8aad477b475fc; existShop=MTYwOTQ4NjMxOQ%3D%3D; uc4=nk4=0%40FY4KoeysZvXhz8XusHkgn14S%2BUtzSw%3D%3D&id4=0%40VXkfhEAyXmG2aXL2HVU1lxtBPr%2BL; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=89f; _nk_=tb419516608; cookie1=W8CNutpfKjAz0ZpQ4tnQaHMW8R2FOeOf42DA3C6ieDs%3D; x5sec=7b22617365727665723b32223a22353931323961343631383433633865316637313239356435383631316364323143504366752f3846454b4c6d78502b416934622b48526f4d4e4449774d5459774e7a55344f547332227d; tfstk=cnAcB7bKTKWbEXBkdj1X-4WdcJDRZYkVcCRyaQi3MwgBS6RPiiezLxaxriKD6R1..; l=eBxZzgQqQ9_a9BmtBO5Bnurza77TFIRb8lVzaNbMiInca6gf9FNRoNQ2YVkDWdtjgt5YTetrJmGnAdnXz5438xGjL77kob-HOB968e1..; isg=BF5e5DkljWcwzdiNYEV2whmgr_SgHyKZ9f46dwjnZ6GcK_8FcKqsqKmJJzcnKBqx'
              }
df = pd.read_csv('adress3.csv',encoding='gbk')
df1 = df['城市'].values.tolist()
df2 = df['地区'].values.tolist()
df3 = df['url'].values.tolist()
df4 = df['页码'].values.tolist()
for k in range(len(df1)):
    for kj in range(1,int(df4[k])+1):

        urll = "https:"+df3[k].strip()+'&page={}'.format(kj)

        print(urll)

        response = requests.get(urll,headers=headers)

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
            res = requests.get(url, headers=headers)

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
            a1[ppp], '广东', a33[ppp], a34[ppp],"住宅用房", a2[ppp], a3[ppp], a4[ppp], a5[ppp], a6[ppp], a7[ppp], '', '', '','', a10[ppp], '拍卖人数', a11[ppp], a12[ppp], a13[ppp], a2[ppp], a14[ppp], a15[ppp], a16[ppp], a17[ppp], a18[ppp], a19[ppp], a20[ppp], a21[ppp], a22[ppp],
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