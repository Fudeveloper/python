#-*-coding:utf-8-*-

import urllib2
#代理开关标识
enable_proxy=True

proxy_handler=urllib2.ProxyHandler({'http':'180.168.179.193:8080'})
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
response=opener.open('http://www.baidu.com')
print response.read()
