# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newDongguan.items import NewdongguanItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class NewdongguanSpider(CrawlSpider):
    name = 'newdongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=90']

    rules = (
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'report\?page='), follow=True),
    )

    # def print_url(self, response):
    #     print 'print_url'
    #     print response.url
    #     return response

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
        str = ''.join(lists)
        # 如果上面的内容为空，则替换
        if len(str)==4 or len(str)==0:
            lists = response.xpath("//div[@class='pagecenter p3']//div[@class='contentext']/text()").extract()
            str = ''.join(lists).strip()
        item['content'] = str
        print len(str)
        # 该帖子地址
        item['url'] = response.url
        yield item
