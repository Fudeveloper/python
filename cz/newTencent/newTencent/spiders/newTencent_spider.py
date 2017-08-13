# -*-coding:utf-8-*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

from newTencent.items import NewtencentItem

class NewTencentSpider(CrawlSpider):
    name='newtencent'
    allow_domains=['hr.tencent.com']
    start_urls=['http://hr.tencent.com/position.php?&start=0']

    # 获取response里的链接提取规则，返回符合匹配规则的所有链接
    page_link=LinkExtractor(allow=('start=\d+'))
    # new_link=new_link
    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定返回回调函数
        Rule(page_link,callback='parse_tencent',follow=True)
        # Rule(new_link)
    ]
    def get_text(self,element,xpath_express):
        try:
            res=element.xpath(xpath_express)
            return res.extract()[0]
        except:
            return ''

    # 指定回调函数
    def parse_tencent(self,response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            # 初始化item模型对象(类似一个dict)
            item = NewtencentItem()

            # 职位名称
            item['name'] = self.get_text(each, './td[1]/a/text()')
            # 详情链接
            item['link'] = 'http://hr.tencent.com/{0}'.format(self.get_text(each, './td[1]/a/@href'))
            # 职位类别
            item['category'] = self.get_text(each, './td[2]/text()')
            # 人数
            item['number'] = self.get_text(each, './td[3]/text()')
            # 地点
            item['position'] = self.get_text(each, './td[4]/text()')
            item['date'] = self.get_text(each, './td[5]/text()')
            # 将数据交给管道文件处理
            yield item



