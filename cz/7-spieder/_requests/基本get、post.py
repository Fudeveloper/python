# -*-coding:utf-8-*-

import requests
# 基本get
get_res=requests.get('http://www.baidu.com')

print get_res       # <Response [200]>
print get_res.status_code       # 200
print get_res.cookies           # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print get_res.encoding          # ISO-8859-1

# 取得网页响应文本
# print get_res.text
print get_res.content

# 加参数
data={'key1':'value1','key2':'value2'}
r=requests.get('http://www.baidu.com', params=data)
# 打印response对象的url
print r.url     # http://www.baidu.com/?key2=value2&key1=value1



# 如果想请求JSON文件，可以利用 json() 方法解析


r=requests.get("https://github.com/timeline.json")
print r.text
# {"message":"Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.","documentation_url":"https://developer.github.com/v3/activity/events/#list-public-events"}

print r.json()
'''
{"message":"Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.","documentation_url":"https://developer.github.com/v3/activity/events/#list-public-events"}
{u'documentation_url': u'https://developer.github.com/v3/activity/events/#list-public-events', u'message': u'Hello there, wayfaring stranger. If you\u2019re reading this then you probably didn\u2019t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.'}
'''
hearders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
requests.get('http://www.baidu.com', hearders=hearders)


#响应头
r = requests.get('http://m.ctrip.com')
print r.headers
print r.headers['Content-Type']
print r.headers.get('content-type') #访问响应头部分内容的两种方式

#设置访问代理
proxies = {
           "http": "http://10.10.10.10:8888",
           "https": "http://10.10.10.100:4444",
          }
r = requests.get('http://m.ctrip.com', proxies=proxies)

# post
post_res=requests.post('http://www.baidu.com')
# 重新设置response对象的编码为utf-8
post_res.encoding='utf-8'
# print post_res.text
# print post_res.content

# 定制hearders
hearders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
requests.post('http://www.baidu.com', hearders=hearders)


#复杂post请求
url = 'http://m.ctrip.com'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload)) # 如果传递的payload是string而不是dict，需要先调用dumps方法格式化一下