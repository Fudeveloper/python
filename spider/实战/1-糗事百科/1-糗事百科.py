#-*-coding:utf-8

'''
目标：
1.抓取糗事百科热门段子
2.过滤带有图片的段子
3.实现每按一次回车显示一个段子的发布时间，发布人，段子内容，点赞数。
'''


#先构造最基本的页面抓取方法

import urllib
import urllib2
import re

#声明url和heards
url='https://www.qiushibaike.com/8hr/page/1'
headrs={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36 Name'}
#创建request
request=urllib2.Request(url,headers=headrs)
try:
    #尝试打开页面
    response=urllib2.urlopen(request)
    content= response.read()
    # print content
    #预编译正则字符串
    pattern=re.compile('<div class="article block untagged.*?<h2>(.*?)</h2>[\s\S]*?</a>[\s\S]<div class="articleGender.*?<span>(.*?)</span>.*?<!-- 图片(.*?)<div class="stats.*?number">(.*?)</i>.*?">.*?</i>.*?',re.S)
    items=re.findall(pattern,content)
    print len(items)        #25 ok
#下面开始筛选出没有图片的段子：
    #创建一个list来存放不含图片的段子：
    list_noimg=[]
    for item in items:
        have_img=re.search('img',item[2])
        if not have_img:
            list_noimg.append(item)
            print len(list_noimg)
            print item[0],item[1],item[2]
except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason

