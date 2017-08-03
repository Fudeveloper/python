#-*-coding:utf-8-*-

# # #获取cookie保存到变量
# # import urllib2
# # import cookielib
# # #创建一个CookieJar对象来存储将要获得的cookie
# # cookie=cookielib.CookieJar()
# # #利用urllib2的HTTPCookieProcessor 对象创建cookie处理器
# # handler=urllib2.HTTPCookieProcessor(cookiejar=cookie)
# # #利用handler来构建opener
# # opener=urllib2.build_opener(handler)
# # #此处的opener和urlopen一样，也可以传入Request
# # response=opener.open('http://www.baidu.com')
# #
# # for item in cookie:
# #     print 'name={0}'.format(item.name)
# #     print 'value={0}'.format(item.value)
# #
# # # name=BAIDUID
# # # value=CE9EE0FF8B1B8533E20AEF93F43E80B3:FG=1
# # # name=BIDUPSID
# # # value=CE9EE0FF8B1B8533E20AEF93F43E80B3
# # # name=H_PS_PSSID
# # # value=23931_1468_18195_21081_18559_17001_20718
# # # name=PSTM
# # # value=1501153924
# # # name=BDSVRTM
# # # value=0
# # # name=BD_HOME
# # # value=0
# #
# #
# # '''
# # 在上面的方法中，我们将cookie保存到了cookie这个变量中，
# # 如果我们想将cookie保存到文件中该怎么做呢？这时，我们就要用到
# # FileCookieJar这个对象了，
# # 在这里我们使用它的子类MozillaCookieJar来实现Cookie的保存
# # '''
# # #保存cookie到文件
# # import urllib2
# # import cookielib
# #
# # #设置保存cookie的文本，同级目录下的cookie.txt
# # filename='cookie.txt'
# # #声明一个MozillaCookieJar对象来保存cookie，后写入文件
# # cookiejar=cookielib.MozillaCookieJar(filename=filename)
# # handler=urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
# # opener=urllib2.build_opener(handler)
# # response=opener.open('http://www.baidu.com')
# # cookiejar.save(ignore_discard=True,ignore_expires=True)
# # # ignore_discard: save even cookies set to be discarded.
# # # ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
#
#
# #利用cookie来模拟登陆
# import urllib
# import urllib2
# import cookielib
#
#
# filename='cookie.txt'
# #构建data字符串
# url='http://www.yb3.cc/login.php?action=login&usecookie=120&jumpurl='
# postdata=urllib.urlencode({
#     'username':'likliklik',
#     'password':'wo951127'
# })
# print postdata
# #声明一个cookiejar对象来保存cookie
# cookiejar=cookielib.MozillaCookieJar(filename)
# #创建handler
# handler=urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
# #构建opener
# opener=urllib2.build_opener(handler)
# #创建一个request
# request=urllib2.Request(url,postdata)
# #打开网址
# response=opener.open(request)
# #保存cookie到文件
# cookiejar.save(ignore_expires=True,ignore_discard=True)
# print response.read()




##从文件中读取cookie
import urllib2
import cookielib
#创建cookiejar对象
cookiejar=cookielib.MozillaCookieJar()
#从文件中加载cookie对象
cookiejar.load('cookie.txt',ignore_discard=True,ignore_expires=True)
#创建handler
handler=urllib2.HTTPCookieProcessor(cookiejar)
#构建一个opener
opener=urllib2.build_opener(handler)
#创建请求request
request=urllib2.Request('http://www.yb3.cc/my_favorite.php')
#得到响应结果
response=opener.open(request)
if '清空书架' in response.read():
    print 'login successed'
else:
    print 'no cookie'


