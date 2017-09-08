# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位名称
    name = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地点
    position = scrapy.Field()
    # 发布时间
    date = scrapy.Field()





