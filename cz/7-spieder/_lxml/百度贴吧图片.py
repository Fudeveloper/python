#coding:utf-8-*-

import urllib2
import urllib
from lxml import etree

def load_page():
    name=raw_input('请输入贴吧名\n')
    url='https://tieba.baidu.com/f?ie=utf-8&'
    data={'kw':name}
    fullurl=url+urllib.urlencode(data)
    # print fullurl
    headrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    #尝试加载页面：
    try:
        request = urllib2.Request(fullurl,headers=headrs)
        response = urllib2.urlopen(request)
        html=response.read()
        # print html
        #解析html文档为HTML DOM模型
        content=etree.HTML(html)
        #返回一个列表（类似正则findall）
        res= content.xpath("//div[@class='threadlist_lz clearfix']/div/a[@class='j_th_tit ']/@href")
        return res
    except urllib2.URLError,e:
        print e.code

#获得每个帖子中图片的链接
def get_image_link(url):
    headrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    fullurl='https://tieba.baidu.com{0}'.format(url)
    print fullurl
    try:
        request=urllib2.Request(fullurl,headers=headrs)
        response=urllib2.urlopen(request)
        html=response.read()
        content=etree.HTML(html)
        img_list=content.xpath("//img[@class='BDE_Image']/@src")
        return img_list
    except urllib2.URLError,e:
        print e.code
        return None

#下载图片的方法
def download_img(img_url):

    # print fullurl
    headrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    # 尝试加载页面：
    try:
        request = urllib2.Request(img_url, headers=headrs)
        response = urllib2.urlopen(request)
        img = response.read()
        img_name = img_url[-15:]
    except urllib2.URLError,e:
        print '打开网页出错'+e.code
    try:
        with open(img_name,'wb') as f:
            f.write(img)
    except IOError,e:
        print '写入错误'


res=load_page()
for i in res:
    img_link_list=get_image_link(i)
    for link in img_link_list:
        download_img(link)
# download_img('https://imgsa.baidu.com/forum/w%3D580/sign=340975f472f0f736d8fe4c093a54b382/41ee3d6d55fbb2fbdc7b1b99454a20a44723dced.jpg')


