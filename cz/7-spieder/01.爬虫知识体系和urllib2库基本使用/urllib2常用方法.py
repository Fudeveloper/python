#-*-coding:utf-8
import urllib2
url='http://www.baidu.com'
data=''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
request=urllib2.Request(url,data,headers)
response=urllib2.urlopen(request)

#返回发送响应的url,防止重定向问题
print response.geturl()     #http://www.baidu.com/search/error.html

#返回HTTP响应码
print response.getcode()        #200

#返回服务器响应的HTTP报头
print response.info()
# Date: Wed, 02 Aug 2017 08:36:17 GMT
# Server: Apache
# P3P: CP=" OTI DSP COR IVA OUR IND COM "
# Set-Cookie: BAIDUID=AF08179FD75E7769465127C0F34B525A:FG=1; expires=Thu, 02-Aug-18 08:36:17 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
# Last-Modified: Mon, 29 Feb 2016 11:11:44 GMT
# ETag: "2bd1-52ce6b6c4bc00"
# Accept-Ranges: bytes
# Content-Length: 11217
# Cache-Control: max-age=86400
# Expires: Thu, 03 Aug 2017 08:36:17 GMT
# Vary: Accept-Encoding,User-Agent
# Connection: Close
# Content-Type: text/html
