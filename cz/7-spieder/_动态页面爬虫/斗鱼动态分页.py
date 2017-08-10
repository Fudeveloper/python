# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import lxml
# 创建PhantomJS浏览器对象
webdriver=webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# 打开页面
webdriver.get('https://www.douyu.com/directory/all')

old_page_source=''

# def get_next_page():

while True:
    # 获得网页源码
    page_source=webdriver.page_source

    if old_page_source!=page_source or old_page_source == '':


        old_page_source = page_source
        # 初始化beautifuSoup对象
        soup = bs(page_source, 'lxml')
        # 匹配所有房间名
        rooms = soup.find_all('h3', {'class': 'ellipsis'})
        # 匹配观众人数
        numbers = soup.find_all('span', {'class': 'dy-num fr'})

        for room, number in zip(rooms, numbers):
            print u'房间名:{0}\t观众数:{1}'.format(room.text.strip(), number.text.strip())

        # 如果找到结束标识，退出循环
        if page_source.find('shark-pager-next shark-pager-disable shark-pager-disable-next') != -1:
            webdriver.quit()
            break
        else:
            webdriver.find_element_by_class_name('shark-pager-next').click()
        # 向下翻页





