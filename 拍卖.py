import requests
from lxml import etree
import json
import time
import pandas as pd
import re
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'referer': 'https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.28.2f59564ejE6s4P&category=50025969&auction_source=0&city=&province=%C9%BD%CE%F7&sorder=2&st_param=-1&auction_start_seg=-1',
    'cookie':'enc=K33Bnjyg5lxFs7ONNAP2Y7SuUfLtAdJe3aOud9MoyqkQM900ffLKKL3Jke6jLdnz1UMrM96ZGtOdE%2BBjo79hGg%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; t=ffff8315a790b80c1367b4e4092f67f1; _uab_collina=160942154893772949208428; cna=Ki9WF6Po63sCAXjmyIkbgKhF; mt=ci=41_1; lgc=tb419516608; tracknick=tb419516608; xlly_s=1; cookie2=1ecfea62f684e9d09e2fe0a273e0434f; _tb_token_=e7eeeeebe7698; _samesite_flag_=true; sgcookie=E1006efcv2OQWkPEKhokdLc03J0epWASNm4p8na9AGhcJJy3V2xdBYTY9yYpVdmQUJ90jBxPcf%2F5UKyubTfzRjTj%2BA%3D%3D; unb=4201607589; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie14=Uoe1gql7ko7jyg%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&existShop=false; uc3=nk2=F5RBxEvyGEteGuw%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=Vy64MHc652zmCg%3D%3D&vt3=F8dCuAAiZymoul875gI%3D; csg=b1bd2b8b; cookie17=Vy64MHc652zmCg%3D%3D; dnk=tb419516608; skt=845057b4aec065ea; existShop=MTYxMDE5MTk4Mw%3D%3D; uc4=id4=0%40VXkfhEAyXmG2aXL2HVS8xrxWVqWp&nk4=0%40FY4KoeysZvXhz8XusHkhbWGilBz3nQ%3D%3D; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=89f; _nk_=tb419516608; cookie1=W8CNutpfKjAz0ZpQ4tnQaHMW8R2FOeOf42DA3C6ieDs%3D; tfstk=cHRRByjahmmoSqbv7LH0duEqQ2ucZsaRxzsL9VozBjAiLwNdiHRM6d6iFwrRMqC..; l=eBxZzgQqQ9_a9wRtBO5wlurza77OoIOf1sPzaNbMiInca6dO9FyebNQ25ki9WdtjgtfjyetrJmGnARHySGzpg-bMpDxOdT3FnY9M-; isg=BGBg3qOcK1oCmJZH0nNQuGv-MW4yaUQzp1B0PdpwKHsB1QP_gnp9w3rnbX3V5fwL; x5sec=7b22617365727665723b32223a226666363636633735643732383731353561643264323437343465343936303833434b47703576384645505761696561657474572b53526f4e4e4449774d5459774e7a55344f5473344d413d3d227d'




}
proxy={
    'http':'106.54.172.70:16819'
}
s = requests.session()
response = s.get('https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.59.337a54b3heTnOp&category=50025969&auction_source=0&city=&province=%B0%B2%BB%D5&st_param=-1&auction_start_seg=-1',headers=headers,proxies=proxy)
# with open ('房产.html','w',encoding='utf-8')as f:
#     f.write(response.text)
content = response.content
html = etree.HTML(content)

# print(a)
c1 = []
c2 = []
c3 = []
a1 = []
a2 = []
c4 = []

b = html.xpath('//li[@class="triggle unfold "]/div/ul/li')
for o in b:
    name = o.xpath('./em/a/text()')
    url = o.xpath('./em/a/@href')
    a1.append(name[0])
    a2.append(url[0])
    print(name[0])

for p in range(len(a2)):
    new_url = 'https:'+a2[p].strip()


    res = s.get(new_url,headers=headers)
    con = res.content
    ht = etree.HTML(con)
    a = ht.xpath('//div[@class="sub-condition J_SubCondition  small-subcondion"]/ul/li')
    # hj = ht.xpath('//span[@class="page-skip"]/em/text()')


    for i in a :
        c = i.xpath('./em/a/text()')
        d = i.xpath('./em/a/@href')
        c1.append(c[0])
        c2.append(d[0])
        c3.append(a1[p])
for y in c2:

    ne_url ='https:'+y.strip()

    ro = s.get(ne_url,headers=headers)

    con_ = ro.content
    html_ = etree.HTML(con_)
    hj = html_.xpath('//span[@class="page-skip"]/em/text()')
    if hj:
        c4.append(hj[0])
    else:
        c4.append(' ')



lk = pd.DataFrame({"城市":c3,"地区":c1,"url":c2,'页码':c4})
lk.to_csv('拍卖地址安徽2.csv',encoding='gbk')


# for i in a :
#     c = i.xpath('./em/a/text()')
#     d = i.xpath('./em/a/@href')
#
#     c1.append(c[0])
#     c2.append(d[0])
#     print(c[0],d[0])
