from selenium import webdriver

from bs4 import BeautifulSoup

import urllib.request

from selenium.webdriver.common.action_chains import ActionChains

input_string = input('输入你要下载的歌曲名字:')


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get('http://www.kugou.com/')

a = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[1]/div[1]/input')

a.send_keys(input_string)

driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[1]/div[1]/div/i').click()

for handle in driver.window_handles:

    driver.switch_to.window(handle)

# result_url = driver.current_url


# driver = webdriver.Firefox()

# driver.maximize_window()

# driver.get(result_url)

# j=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul[2]/li[2]/div[1]/a').get_attribute('title')测试

# print(j)

soup = BeautifulSoup(driver.page_source, 'lxml')

PageAll = len(soup.select('ul.list_content.clearfix > li'))

print(PageAll)

for i in range(1, PageAll + 1):
    j = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul[2]/li[%d]/div[1]/a' % i).get_attribute('title')

    print('%d.' % i + j)

choice = input("请输入你要下载的歌曲（输入序号）：")

# global mname

# mname=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul[2]/li[%d]/div[1]/a'%choice).get_attribute('title')#歌曲名

a = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul[2]/li[%s]/div[1]/a' % choice)

b = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul[2]/li[%s]/div[1]/a' % choice).get_attribute(
    'title')

actions = ActionChains(driver)

actions.move_to_element(a)

actions.click(a)

actions.perform()

# wait(driver)?

# driver = webdriver.Firefox()

# driver.maximize_window()

# driver.get(result_url)

# windows = driver.window_handles

# driver.switch_to.window(windows[-1])

# handles = driver.window_handles

for handle in driver.window_handles:  #

    driver.switch_to.window(handle)

Local = driver.find_element_by_xpath('//*[@id="myAudio"]').get_attribute('src')

print(driver.find_element_by_xpath('//*[@id="myAudio"]').get_attribute('src'))


def cbk(a, b, c):
    per = 100.0 * a * b / c

    if per > 100:
        per = 100

    print('%.2f%%' % per)


soup = BeautifulSoup(b)

name = soup.get_text()

path = '%s.mp3' % name

urllib.request.urlretrieve(Local, path, cbk)

print('finish downloading %s.mp3' % name + '\n\n')