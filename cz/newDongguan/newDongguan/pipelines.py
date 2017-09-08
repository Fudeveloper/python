# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class NewdongguanPipeline(object):
    # 初始化时，创建一个文件来保存数据
    def __init__(self):
        self._file_name=open('newdongguan.json','w')

    def process_item(self, item, spider):
        json_data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self._file_name.write(json_data.encode('utf-8'))
        return item

    # 结束时，关闭文件
    def close_spider(self,spider):
        self._file_name.close()