#-*-coding:utf-8-*-
import urllib2
import urllib
values={'username':'usr','password':'xxxx'}
#拼接字符串
data=urllib.urlencode(values)
print data      #username=usr&password=xxxx
url='https://passport.baidu.com/v2/?login&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F'
request=urllib2.Request(url,data=data)

response=urllib2.urlopen(request)
print response.read()