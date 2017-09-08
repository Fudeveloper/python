# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json
class DouyuImageSpider(scrapy.Spider):
    name = 'douyu_image'
    allowed_domains = ['capi.douyucdn.cn']
    basic_url='http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [basic_url+str(offset)]

    def parse(self, response):
        # 把json格式的数据转换为python格式，data段是列表
        data = json.loads(response.text)["data"]

        # 遍历json格式数据文本，取出各字段值
        for each in data:
            # 初始化模型对象
            item = DouyuItem()
            # 昵称
            item['nickname'] = each['nickname']
            # 图片
            item['imagelink'] = each['vertical_src']

            # 将item返回给pipelines处理
            yield item
        # 调用一次parse方法后，处理url
        self.offset += 20
        # 准备发送下一个请求
        yield scrapy.Request(self.basic_url+str(self.offset),callback=self.parse)
