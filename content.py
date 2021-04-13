import requests
from pyquery import PyQuery as pq
import json
from lxml import etree
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',

}
r=requests.get('https://music.163.com/m/discover/toplist?id=19723756',headers=headers)
doc = pq(r.text)
content=r.content
html=etree.HTML(content)
a=html.xpath('//textarea/text()')
c=json.loads(a[0])
g={}
q={}
for item in range(len(c)):




    g[item]= c[item].get("id")
    q[item]=c[item].get("name")
print(g,q)

# print(c)
# for i in c:
#     for key,value in i.items():
#         print(key,value)

# print(a)
# g=[]
# for i in a:
#     g.append(i)

# print(g)
# for q in g:
#     print(q)
# with open('tt.html','w',encoding='utf-8')as f:
#
#     f.write(r.text)
# print(doc)
# result = doc("#song-list-pre-data").text()
# print(json.loads(result))
# for item in range(len(json_data)):
#     yield {"name": json_data[item].get("name"),
#            "singer": json_data[item].get("artists")[0].get("name"),
#            "url": "https://music.163.com/#/song?id=" + str(json_data[item].get("id")),
#            "ID": json_data[item].get("id")
#            }
# f.write(result)
