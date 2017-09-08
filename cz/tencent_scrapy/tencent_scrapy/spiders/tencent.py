# -*- coding: utf-8 -*-
import scrapy
from tencent_scrapy.items import TencentScrapyItem

# 默认__init__方法
class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url='http://hr.tencent.com/position.php?&start='
    offset=0
    start_urls = [url+str(offset)]

    def get_text(self,element,xpath_express):
        try:
            res=element.xpath(xpath_express)
            return res.extract()[0]
        except:
            return ''


    def parse(self, response):
        # 遍历表格每一行
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            # 初始化item模型对象(类似一个dict)
            item = TencentScrapyItem()


            # 职位名称
            item['name'] = self.get_text(each,'./td[1]/a/text()')
            # 详情链接
            item['link'] = 'http://hr.tencent.com/{0}'.format(self.get_text(each,'./td[1]/a/@href'))
            # 职位类别
            item['category'] = self.get_text(each,'./td[2]/text()')
            # 人数
            item['number'] = self.get_text(each,'./td[3]/text()')
            # 地点
            item['position'] = self.get_text(each,'./td[4]/text()')
            item['date'] = self.get_text(each,'./td[5]/text()')
            # 将数据交给管道文件处理
            yield item

        # url变化规律
        if self.offset < 1680:
            self.offset += 10
            print 'add'
            print 'offset={0}'.format(self.offset)

        # 处理完一页的数据后，发送下一个页面请求
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


