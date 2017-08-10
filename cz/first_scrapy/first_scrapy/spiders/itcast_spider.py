# -*-coding:utf-8-*-
import scrapy
from first_scrapy.items import ItcastItem
class ItcastSpider(scrapy.Spider):
    name='itcast'
    #允许爬虫作用的范围
    allowd_domains=['http:www.itcast.cn/']
    #爬虫起始url
    start_urls=['http://www.itcast.cn/channel/teacher.shtml#']

    # 重写parse方法
    def parse(self,response):
        # with open('teacher.html','w') as f:
        #     f.write(response.body)

        # 用scrapy自带的xpath来寻找目标元素
        # 教师列表
        teacher_list=response.xpath('//div[@class="li_txt"]')

        # 所有老师的集合
        # teachers_item=[]

        for each in teacher_list:
            #实例化item对象，来保存数据
            item =ItcastItem()
            # 姓名(xpath对象)，通过extract()将匹配出来的结果转换为Unicode字符串
            name= each.xpath('./h3/text()').extract()
            # 职称(xpath对象)
            title=each.xpath('./h4/text()').extract()
            # 简历(xpath对象)
            info=each.xpath('./p/text()').extract()

            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            # teachers_item.append(item)

            # 将数据yield给pipeline文件处理
            yield item

        # 不经过pipelines处理，直接返回
        # return teachers_item


