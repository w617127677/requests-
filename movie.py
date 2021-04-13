# -*- coding: UTF-8 -*-
import requests
import re
import os,shutil
from urllib.request import urlretrieve
from multiprocessing import Pool

def cbk(a,b,c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)

def get_api_data(QQ_film_url): #正则匹配获取api返回的index.m3u8链接地址
    api_url='http://p.p40.top/api.php'
    user_agent={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    get_url=api_url+'?url='+QQ_film_url
    print(get_url)
    response=requests.get(get_url,headers=user_agent).text
    pattern=re.compile('url.*?m3u8')
    get_data=pattern.findall(response)[0][6:].replace('\\','')
    return get_data


def m3u8_download(m3u8_url):#获取下载m3u8文件
    if os.path.exists('F:\\vip电影\\index.m3u8')!=True:#判断文件是否已经存在，存在则不操作。不存在才下载。
        urlretrieve(url=m3u8_url, filename=path, reporthook=cbk)
    else:
        print(path+'已存在')


def get_ts():#通过m3u8文件，正则匹配需要的ts流
    with open(path)as f:
        data=f.read()
    pattern=re.compile('.*.ts')
    get_ts_data=re.findall(pattern,data)
    return get_ts_data


def ts_download(ts_list):#下载ts流
    try:
        ts_url = m3u8_url[:-10]+'{}'.format(ts_list)#获取ts流 url地址
        urlretrieve(url=ts_url, filename=path[:-10] + r'\\' + '{}'.format(ts_url[-8:]))
    except Exception:
        print(ts_url+'保存文件错误')



def pool(ts_list):#多进程爬取所有的ts流到文件夹中,参考的那个py脚本，没用过pool进程池
    print('经过计算，需要下载%s个文件'%len(ts_list))
    print(ts_list[0])
    pool=Pool(16)
    pool.map(ts_download,[i for i in ts_list])
    pool.close()
    pool.join()
    print('下载完成')
    ts_to_mp4()


def ts_to_mp4():
    print('dos实现ts合并为mp4')
    str = 'copy /b ' + r'F:\vip电影' + '\*.ts ' + ' '+ r'F:\vip电影\gogogo' + '\jingqi.mp4'
    os.system(str)
    if os.path.exists('F:\\vip电影\\gogogo\\jingqi.mp4')==True:
        print('good job')



path = 'F:\\vip电影\\index.m3u8'
url = 'https://v.qq.com/x/cover/xyne4253g35nak3/m0031od9ekb.html'
m3u8_url = get_api_data(url)[:-10] + '1000k/hls/index.m3u8'
print(m3u8_url)
m3u8_download(m3u8_url)
ts_list = get_ts()
if __name__ == '__main__':
    pool(ts_list)
# https://apd-e9f6869ab4779b65281c6ec7a303b82b.v.smtcdns.com/vipts.tc.qq.com/AUSKMmfL0jaho0uA88site8DCNVCRoRfXO8J52eihWsM/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/atTA67MWjNvGRplQDx9_IoB_vFWNiBPyOOXjwJ7FOxvAbKF9ySAG9TR-k73Wqx5RslAUjWLq1VJodfD3rsX_vvmL_PrrW0duwiLYeJsMC8j61kSegRhx6jvR3fA0U7vE2nBnUy2itFnSRMn6i_SiGDwkJtbUKx3FcXJ3XDTBL7I/0310_v00344knoym.321002.ts.m3u8?
# https://apd-e9f6869ab4779b65281c6ec7a303b82b.v.smtcdns.com/vipts.tc.qq.com/AUSKMmfL0jaho0uA88site8DCNVCRoRfXO8J52eihWsM/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/atTA67MWjNvGRplQDx9_IoB_vFWNiBPyOOXjwJ7FOxvAbKF9ySAG9TR-k73Wqx5RslAUjWLq1VJodfD3rsX_vvmL_PrrW0duwiLYeJsMC8j61kSegRhx6jvR3fA0U7vE2nBnUy2itFnSRMn6i_SiGDwkJtbUKx3FcXJ3XDTBL7I/013_v00344knoym.321002.1.ts?index=13&start=127125&end=137166&brs=13590144&bre=14553831&ver=4&token=ba8b5b27738a8274870ca472112245cb