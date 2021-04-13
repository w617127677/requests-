import requests
from lxml import etree
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',

}
data = {

            'TAB_QuerySubmitPagerData': 2

            }
response = requests.post('https://www.landchina.com/default.aspx?tabid=263',data=data,headers=headers)
# print(response.text)
content =response.content
html =etree.HTML(content)
a = html.xpath('//table[@id="TAB_contentTable"]/tbody/tr/td[3]/a/@href')
print(a)