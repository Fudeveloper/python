# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 昵称
    nickname = scrapy.Field()
    # 图片
    imagelink = scrapy.Field()
    # 图片本地路径
    imagePath = scrapy.Field()


    # # 房间名
    # room_name = scrapy.Field()
    # # 在线人数
    # online_num = scrapy.Field()
