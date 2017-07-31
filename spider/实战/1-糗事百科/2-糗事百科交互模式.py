#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK(object):
    #初始化方法，定义一些变量
    def __init__(self):
        self.page_index=1
        #初始化headers
        self.headrs={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36 Name'}
        #声明一个用来存放段子的列表，每一个元素，是一页中的段子
        self.stories=[]
        #程序是否继续运行的标识
        self.continue_flag=False
    #开始方法
    def start(self):
        print "正在读取糗事百科,按回车查看新段子，Q退出"
        #将继续进行标识置为true
        self.continue_flag=True
        #首先加载一页内容
        self.load_page()
        #声明一个局部变量，来纪录当前读到的页码
        now_page_index=0

        while self.continue_flag:
            # print len(self.stories)
            if len(self.stories)>0:
                #从全局list中获取新一页的段子
                now_page_stories=self.stories[0]
                now_page_index+=1
                del self.stories[0]
                self.get_next_story(now_page_stories,now_page_index)
    #声明读取下一个故事的交互方法
    def get_next_story(self,now_page_stories,now_page_index):
        #遍历这一页的段子

        for story in now_page_stories:

            print '发布者：{0}\n点赞数：{1} \n{2} \n '.format(story[0].strip(),story[3].strip(),story[1].strip())
            print

            #等待用户输入
            user_input=raw_input()
            self.load_page()
            if user_input=='Q':
                print 'end'
                self.continue_flag=False
                return


    #加载并提取页面的内容，加入到列表中
    def load_page(self):
        #如果当前未看的页数小于2页，则加载新的一页
        if self.continue_flag==True:
            if len(self.stories)<2:
                #获取新的一页
                page_stories=self.get_page_items(self.page_index)
                #将页面内的段子存进全局list
                if page_stories:
                    self.stories.append(page_stories)
                    #存完后，将page_index+1,表示下次读取下一页
                    self.page_index+=1



    #根据页面索引值，将这个页面中无图片的段子添加到列表中，并返回
    def get_page_items(self,page_index):
        page_stories=[]
        #获取到网页源码
        page_content=self.get_page_by_index(page_index)
        # print page_content
        #如果网页源码为空，返回none
        if not page_content:
            print '页面加载失败，line41'
            return None
        # 预编译正则字符串
        pattern = re.compile('<div class="article block untagged.*?<h2>(.*?)</h2>[\s\S]*?</a>[\s\S]<div class="articleGender.*?<span>(.*?)</span>.*?<!-- (.*?)<div class="stats.*?number">(.*?)</i>.*?">.*?</i>', re.S)
        items = re.findall(pattern, page_content)
        # print len(items)
        # 下面开始筛选出没有图片的段子：
        # 创建一个list来存放不含图片的段子：

        for item in items:
            have_img = re.search('img', item[2])
            if not have_img:
                page_stories.append(item)
        # print len(self.stories)
        return page_stories

    #定义一个根据页面索引值来获取页面内容的方法,并返回
    def get_page_by_index(self,page_index):
        #根据page_index来获得页面url
        url='https://www.qiushibaike.com/8hr/page/{0}/'.format(page_index)
        # print url
        # 构建request
        request=urllib2.Request(url,headers=self.headrs)
        #尝试获取页面源码
        try:
            response=urllib2.urlopen(request)
            #将页面源码解码为utf-8
            page_content=response.read().decode('utf-8')
            return page_content
        except urllib2.URLError,e:
            print '打开页面失败'
            if hasattr(e,'reason'):
                print e.reason
            if hasattr(e,'code'):
                print e.code
            return None




spider=QSBK()
# spider.get_page_by_index(2)
# spider.start()
spider.start()







