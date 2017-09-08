# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem

# 保留导演数量
RATAIN_DIRECTORS = 2
# 保留主演数量
RATAIN_ACTORS = 3
# 保留类型数量
RATAIN_TYPE = 2

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    #
    offset = 0
    basic_url = 'https://movie.douban.com/top250?start='
    start_urls = [basic_url + str(offset)]

    # 提取一页内电影详情链接
    def parse(self, response):
        link_list = response.xpath("//div[@class='hd']/a/@href").extract()
        for link in link_list:
            yield scrapy.Request(link,callback= self.parse_page_item)

        # # 每调用一次方法，准备下一次请求的url
        # if self.offset < 225:
        #     self.offset += 25
        # yield scrapy.Request(self.basic_url + str(self.offset),callback = self.parse)



    # 处理电影链接内数据
    def parse_page_item(self,response):
        # 初始化item对象
        item = DoubanmovieItem()
        # 电影名
        item['name'] = response.xpath("//div[@id='content']/h1/span[1]/text()").extract()[0].strip().split()[0]
        # 评分
        item['score'] = response.xpath("//strong[@class='ll rating_num']/text()").extract()[0].strip()

        # 导演等信息XML树
        info_tree = response.xpath("//div[@id='info']")

        # 主演列表
        actor_list = info_tree.xpath("./span[3]/span[2]/a/text()").extract()
        # 主演字段
        item['actors'] = self.retain_element_by_num(actor_list, RATAIN_ACTORS)

        # 导演列表
        director_list = info_tree.xpath("./span[3]//a/text()").extract()
        # 导演字段
        item['directors'] = self.retain_element_by_num(director_list, RATAIN_DIRECTORS)

        # 类型列表
        type_list = info_tree.xpath(".//span[@property='v:genre']/text()").extract()
        # 类型字段
        item['types'] = self.retain_element_by_num(type_list, RATAIN_TYPE)

        # 评价人数
        item['people_number'] = response.xpath("//a[@class='rating_people']/span/text()").extract()[0]
        # 将item交给pipelines处理
        yield item

    # 用于保留指定个数的元素，如果该列表中元素数量比指定元素数量少，则保留全部
    def retain_element_by_num(self,element_list,num):
        # 需要保留的元素个数
        max_number = num
        # 取出元素总个数
        list_len = len(element_list)
        # 定义一个列表来存放前保留的元素
        need_list = []
        # 如果元素总个数比想保留的主演个数少，那么就保留所有元素
        if list_len < 3:
            max_number = list_len
        # 将需要保留的元素加入到列表中
        for i in range(max_number):
            need_list.append(element_list[i] + '/')

        # 将元素列表转化成字符串并返回
        return ''.join(need_list).rstrip('/')

