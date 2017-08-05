#-*-coding:utf-8-*-

import urllib2
#代理开关标识
url='http://www.baidu.com/'
request=urllib2.Request(url=url)


enable_proxy=True
headrs = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36 Name'}
proxy_handler=urllib2.ProxyHandler({})
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
    # opener.addheaders([headrs])
    response = opener.open(request)
else:
    # opener = urllib2.build_opener(null_proxy_handler,headrs=headrs)
    response= urllib2.urlopen(url)

print response.read()
