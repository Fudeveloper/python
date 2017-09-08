# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影名
    name = scrapy.Field()
    # 导演
    directors = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 主演
    actors = scrapy.Field()
    # 类型
    types = scrapy.Field()
    # 评价人数
    people_number = scrapy.Field()
