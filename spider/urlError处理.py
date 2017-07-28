#-*-coding:utf-8-*-

import urllib2
request=urllib2.Request('http://www.safhhghasrhwh.com')
try:
    response=urllib2.urlopen(request)
    # print response.read()
    print 'ok'
except urllib2.URLError,e:
    print e.reason

request=urllib2.Request('http://blog.csdn.net/error/403.html?from=http%3a%2f%2fblog.csdn.net%2fcqcresaf')
try:
    response=urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code        #403
    print hasattr(e,'reason')


#如果捕获到了HTTPError，则输出code，不会再处理URLError异常。
# 如果发生的不是HTTPError，则会去捕获URLError异常，输出错误原因。



import urllib2

request=urllib2.Request('http://blog.csdn.net/error/403.html?from=http%3a%2f%2fblog.csdn.net%2fcqcresaf')
try:
    response=urllib2.urlopen(request)
#先抓子类
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason