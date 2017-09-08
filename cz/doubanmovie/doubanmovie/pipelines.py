# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class DoubanmoviePipeline(object):
    def __init__(self):
        self._file_name = open('douban.json','w')

    def process_item(self, item, spider):
        json_data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self._file_name.write(json_data.encode('utf-8'))
        return item

    def close_spisder(self,spider):
        self._file_name.close()