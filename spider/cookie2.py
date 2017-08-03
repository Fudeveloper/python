#-*-coding:utf-8-*-
import urllib
import urllib2
import cookielib

postdata=urllib.urlencode({
    'username':'1178981326@qq.com',
    'password':'wo951127',
})
url='http://www.yb3.cc/login.php?action=login&usecookie=120&jumpurl='


cookiejar=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookiejar)
opener=urllib2.build_opener(handler)

request=urllib2.Request(url=url,data=postdata)
response=opener.open(request)

# print response.read()
# print cookiejar

url2='http://www.yb3.cc/my_favorite.php'
request=urllib2.Request(url=url2)
# print urllib2.urlopen(request).read()
response=opener.open('http://www.yb3.cc/my_favorite.php')
print response.read()
# cookiejar=cookielib.MozillaCookieJar('123.txt')
# handler=urllib2.HTTPCookieProcessor(cookiejar)
# openner=urllib2.build_opener(handler)
# openner.open('http://www.baidu.com')
# cookiejar.save(ignore_discard=True,ignore_expires=True)
# print cookiejar



