# import requests
# import ssl  # ssl免验证
# import urllib.request
#
# # ssl._create_default_https_context = ssl._create_unverified_context  # ssl免验证
# headers = {
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
#
# }
# response=requests.get('https://music.163.com/m/playlist?id=2978156400',headers=headers)
# with open ('platlist.html','w',encoding='utf-8')as f:
#     f.write(response.text)
from selenium import webdriver
from lxml import etree
import json
import time
import random
from selenium.webdriver.chrome.options import Options

class Netease_spider:
    # 初始化数据（需要修改）
    def __init__(self):

        # 无头启动 selenium
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('blink-settings=imagesEnabled=false')
        # opt = webdriver.Chrome(options=options)
        # opt.set_headless()
        self.browser = webdriver.Chrome(chrome_options=options)
        self.originURL = 'https://music.163.com/#/discover/playlist?id=2978156400'
        self.data = list()

    # 获取网页源代码（需要修改）
    def get_page(self,url):
        self.browser.get(url)
        self.browser.switch_to.frame('g_iframe')
        html = self.browser.page_source
        return html

    # 解析网页源代码，获取数据
    def parse4data(self,html):
        html_elem = etree.HTML(html)
        play_num = html_elem.xpath('//ul[@id="m-pl-container"]/li/div/div/span[@class="nb"]/text()')
        song_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@title')
        song_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@href')
        song_link = ['https://music.163.com/#'+item for item in song_href]
        user_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@title')
        user_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@href')
        user_link = ['https://music.163.com/#'+item for item in user_href]
        data = list(map(lambda a,b,c,d,e:{'播放量':a,'歌单名称':b,'歌单链接':c,'用户名称':d,'用户链接':e},play_num,song_title,song_link,user_title,user_link))
        return data

    # 解析网页源代码，获取下一页链接
    def parse4link(self,html):
        html_elem = etree.HTML(html)
        href = html_elem.xpath('//div[@id="m-pl-pager"]/div[@class="u-page"]/a[@class="zbtn znxt"]/@href')
        if not href:
            return None
        else:
            return 'https://music.163.com/#' + href[0]

    # 开始爬取网页
    def crawl(self):
        # 爬取数据
        print('爬取数据')
        html = self.get_page(self.originURL)
        data = self.parse4data(html)
        self.data.extend(data)
        link = self.parse4link(html)
        while(link):
            html = self.get_page(link)
            data = self.parse4data(html)
            self.data.extend(data)
            link = self.parse4link(html)
            time.sleep(random.random())
        # 处理数据，按播放量进行排序
        print('处理数据')
        data_after_sort = sorted(self.data,key=lambda item:int(item['播放量'].replace('万','0000')),reverse=True)
        # 写入文件
        print('写入文件')
        with open('netease.json','w',encoding='utf-8') as f:
            for item in data_after_sort:
                json.dump(item,f,ensure_ascii=False)

if __name__ == '__main__':
    spider = Netease_spider()
    spider.crawl()
    print('Finished')