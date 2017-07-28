#-*-coding:utf-8-*-

import urllib2
res=urllib2.urlopen('http://www.baidu.com')
# print res.read()
print res       #<addinfourl at 46355720L whose fp = <socket._fileobject object at 0x0000000002C3D840>>

#推荐写法：这么写（res）为Request的一个构造：

request=urllib2.Request('http://www.baidu.com')
response=urllib2.urlopen(request)
# print response.read()
print response      #<addinfourl at 47708680L whose fp = <socket._fileobject object at 0x0000000002D27480>>


#需要构造的geturl

import urllib2
import urllib
values={}
values['username']='abc'
values['password']='xxxx'
data=urllib.urlencode(values)
url='http://passport.csdn.net/account/login'
geturl=url+"?"+data
request=urllib2.Request(geturl)
response=urllib2.urlopen(request)
# print   response.read()
print geturl        #http://passport.csdn.net/account/login?username=abc&password=xxxx