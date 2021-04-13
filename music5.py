from selenium import webdriver
from lxml import etree
import json
import time
import random
import requests
o=input('歌单的id是:')
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',

}
options = webdriver.ChromeOptions()
# 添加无界面参数
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://music.163.com/#/playlist?id={}'.format(o))
# browser.save_screenshot('baidu.png')
# driver.get(url)
driver.switch_to.frame("g_iframe")

a=[]
b=[]
info=driver.find_element_by_xpath('//table[@class="m-table "]/tbody').find_elements_by_tag_name("tr")
for i in range(len(info)):
    musicName=info[i].find_element_by_tag_name("b").get_attribute('title').replace('\xa0','')
    hf = info[i].find_element_by_tag_name("a").get_attribute('href')
    a.append(musicName)
    b.append(hf)




# print(a,b)
try:
    for q in range(len(a)):
        name=a[q]
        id=b[q].split('?')[1]
        r = requests.get('http://music.163.com/song/media/outer/url?{}.mp3'.format(id), headers=headers)

        with open('{}.mp3'.format(name), 'wb')as f:
            f.write(r.content)
    print('下载成功')
except:
    print('下载失败的歌曲是'+name)
