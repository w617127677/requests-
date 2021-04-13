import requests
import ssl  # ssl免验证
import urllib.request

# ssl._create_default_https_context = ssl._create_unverified_context  # ssl免验证
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',

}
# requests.get('http://httpbin.org/ip', proxies={'http': 'https':'218.22.7.62:53281'})
# http://music.163.com/song/media/outer/url?id=29004400.mp3
# def url(url):
#     r=requests.get()
a=input('输入音乐名称:')
b=input('输入音乐id:')

r=requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(b),headers=headers)

with open('{}.mp3'.format(a),'wb')as f:
    f.write(r.content)
# https://link.hhtjim.com/163/{}.mp3
# def geturl(url):
#
#     r = requests.get('http://music.163.com/song/media/outer/url?id=29004400.mp3', headers=headers).content
#     with open('烟火里的尘埃4.mp3', 'wb')as fb:
#         fb.write(r)