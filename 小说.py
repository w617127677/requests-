import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get('http://www.yetianlian.com/heyishengxiaomo/',headers=headers)

content = response.content
html = etree.HTML(content)
a = html.xpath('//div[@class="listmain"]/dl/dd')

for i in a:
    url = i.xpath('./a/@href')
    name = i.xpath('./a/text()')
    new_respone = requests.get(url[0])
    new_content = new_respone.content
    new_html = etree.HTML(new_content)
    chater = new_html.xpath('//div[@id="content"]//text()')
    try:
        with open(r'{}.txt'.format(name[0]),'w',encoding='utf-8')as fs:
            for o in chater:

                fs.write(o.replace(r'\xa0','').replace(r'\n',''))
    except:
        pass



