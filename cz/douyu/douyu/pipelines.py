# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os
import scrapy
class DouyuPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    # IMAGE_DIRECTOR = 'E:/learn/python/cz/douyu/img'
    #
    def get_media_requests(self, item, info):
        img_src = item['imagelink']
        yield scrapy.Request(img_src)

    def item_completed(self, results, item, info):
        image_path = [x for ok, x in results if ok]

        # os.rename(self.IMAGE_DIRECTOR+'/'+image_path[0],self.IMAGE_DIRECTOR + '/' + item['nickname'] + '.jpg')

        item['imagePath'] = self.IMAGES_STORE + '/' + item['nickname']

        return item