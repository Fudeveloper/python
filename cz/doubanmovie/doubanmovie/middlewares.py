# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from settings import USER_AGENTS
from settings import PROXIES
import base64
# 随机的User-agent
class RandomUseragent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        print user_agent
        request.headers.setdefault('User-Agent',user_agent)

# 随机代理
class RandomProxy(object):
    def process_request(self,request,spider):
        # 在列表中随机选取一个ip
        proxy = random.choice(PROXIES)

        # 使用没有代理账户验证的ip
        if proxy['user_passwd'] is None:
            request['proxy']='http://'+proxy['ip_port']
        else:
            request.meta['proxy'] = 'http://' + proxy['ip_port']
            # 对账户密码进行base64编码
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 模拟信令
            request.headers['Proxy-Authorization'] = 'Basic '+base64_userpasswd



















# class DoubanmovieSpiderMiddleware(object):
    # # Not all methods need to be defined. If a method is not defined,
    # # scrapy acts as if the spider middleware does not modify the
    # # passed objects.
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     # This method is used by Scrapy to create your spiders.
    #     s = cls()
    #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
    #     return s
    #
    # def process_spider_input(self, response, spider):
    #     # Called for each response that goes through the spider
    #     # middleware and into the spider.
    #
    #     # Should return None or raise an exception.
    #     return None
    #
    # def process_spider_output(self, response, result, spider):
    #     # Called with the results returned from the Spider, after
    #     # it has processed the response.
    #
    #     # Must return an iterable of Request, dict or Item objects.
    #     for i in result:
    #         yield i
    #
    # def process_spider_exception(self, response, exception, spider):
    #     # Called when a spider or process_spider_input() method
    #     # (from other spider middleware) raises an exception.
    #
    #     # Should return either None or an iterable of Response, dict
    #     # or Item objects.
    #     pass
    #
    # def process_start_requests(self, start_requests, spider):
    #     # Called with the start requests of the spider, and works
    #     # similarly to the process_spider_output() method, except
    #     # that it doesn’t have a response associated.
    #
    #     # Must return only requests (not items).
    #     for r in start_requests:
    #         yield r
    #
    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)

