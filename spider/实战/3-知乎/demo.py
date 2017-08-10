# -*-coding:utf-8-*-
import time
# Unix 时间戳
# print time.time()       # 1501931376.42

# 标准时间
# print time.ctime()      # Sat Aug 05 19:09:36 2017


from bs4 import BeautifulSoup
import requests
import json
import urllib
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
# 创建一个可以处理cookie的requests对象
sess=requests.Session()
# 第一次获取该网页的源码
source=requests.get('https://www.zhihu.com/#signin',headers=headers).text
# print source
# 创建一个beautifulsoup对象，并使用lxml解析器
soup=BeautifulSoup(source,'lxml')
#获取网页中_xsrf的值
_xsrf=soup.find(name='input',attrs={'name':'_xsrf'}).get('value')

#登陆方法
def Zhihu_login(phone_num,passwd):

    post_data={
        '_xsrf':_xsrf,
        'password': passwd,
        'phone_num':phone_num,
        'captcha_type': 'cn'
    }
    post_url='https://www.zhihu.com/login/phone_num'
    r=requests.post(post_url,data=post_data,headers=headers)
    return r.text
print Zhihu_login('13960942437','wo951127')

# print u"\u767b\u5f55\u8fc7\u4e8e\u9891\u7e41\uff0c\u8bf7\u7a0d\u540e\u91cd\u8bd5"
# print u'\u9a8c\u8bc1\u7801\u9519\u8bef'