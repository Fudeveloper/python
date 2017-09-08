# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FirstScrapyPipeline(object):
#     def process_item(self, item, spider):
#         return item


class ItcastPipeline(object):

    # 初始化时创建文件
    def __init__(self):
        self.file_name=open('teacher.json','w')

    # 必须写的一个方法，用来处理item数据
    def process_item(self,item,spider):
        # 有中文就必须加上ensure，禁用ascii编码方式，使用utf-8
        json_text=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file_name.write(json_text.encode('utf-8'))
        return item

    # 可选方法，结束时自动调用
    def close_spider(self):
        self.file_name.close()