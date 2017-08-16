# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from newDongguan.items import NewdongguanItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class NewdongguanSpider(scrapy.Spider):
    name = 'other'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    basic_url='http://wz.sun0769.com/index.php/question/report?page='

    start_urls = [basic_url+str(offset)]
    print start_urls
    # 处理本页内容，并向下翻页
    def parse(self, response):

        # 匹配所有问题链接，并发送对问题链接的请求
        link_list = response.xpath("//div[@id='morelist']//a[@class='news14']/@href").extract()
        for link in link_list:
            yield scrapy.Request(link,callback=self.parse_item)

        # 向下翻页
        if self.offset<104520:
            self.offset += 30
            yield scrapy.Request(self.basic_url+str(self.offset),callback=self.parse)




    # 处理帖子内容的方法
    def parse_item(self, response):
        item = NewdongguanItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # 详细信息
        all = response.xpath("//div[@class='pagecenter p3']//strong[@class='tgray14']/text()").extract()[0].strip()
        # print all
        # 标题
        item['title'] = all.split('  ')[0][9:]
        # 编号
        item['number'] = all.split('  ')[-1].split(":")[-1]
        # 内容
        lists = response.xpath("//div[@class='pagecenter p3']//div[@class='c1 text14_2']/text()").extract()
        str = ''.join(lists).strip()
        # 如果上面的内容为空，则替换
        if len(str)==4 or len(str)==0:
            lists = response.xpath("//div[@class='pagecenter p3']//div[@class='contentext']/text()").extract()
            str = ''.join(lists).strip()
        item['content'] = str
        # print len(str)
        # 该帖子地址
        item['url'] = response.url
        yield item
