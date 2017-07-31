#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import urllib2
import re

#百度贴吧爬虫类
class BDTB(object):
    #初始化方法，传入基础url和是否只看楼主。（0为否，1为是）
    def __init__(self,base_url,see_lz=1):
        # 构造真实url
        self.url=base_url+'?see_lz={0}'.format(see_lz)

    def start(self):
        #获取第一页内容，标题和页面总数
        index_page_content=self.read_page(1)
        self.title_page_sum=self.get_title_and_page_sum(index_page_content)
        print '帖子标题：{0}，总页数：{1}页'.format(self.title_page_sum[0],self.title_page_sum[1])
        #将内容写进文件
        try:
            for i in range(1,int(self.title_page_sum[1])+1):
                undispose_content=self.read_page(i)
                tidy_content=self.clean_content(undispose_content)
                print tidy_content
                self.write_content(tidy_content)
                print '正在写入第{0}页数据,还剩下{1}页'.format(i,int(self.title_page_sum[1])-i)
        except  IOError,e:
            print '写入异常，{0}'.format(e.message)
        finally:
            print '写入完成'
    def write_content(self,text):
        fw=open(self.title_page_sum[0]+'.txt','a')
        fw.write(text)

        # print title_page_sum
    def read_page(self,page_num):
        # 构造当前页面url
        self.page_url=self.url+'&pn={0}'.format(page_num)
        # print self.final_url
        #尝试读取页面
        try:
            request = urllib2.Request(self.page_url)
            response=urllib2.urlopen(request)
            # print response
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            print 'UrlError'
            if hasattr(e,'reason'):
                print e.reason
            if hasattr(e,'code'):
                print e.code
            return None
    #获取帖子标题,帖子总页数的方法
    def get_title_and_page_sum(self,content):
        #使用正则来获取标题
        title_patten='<h3 class="core_title_txt .*?>(.*?)</h3>'
        title_result=re.search(title_patten,content)
        page_sum_patten = re.compile(ur'<li class="l_reply_num.*>(.*?)</span>页</li>')
        page_result = re.search(page_sum_patten,content)


        if title_result and page_result:
            title=title_result.group(1).strip()
            page_sum=page_result.group(1).strip()
            #返回一个元组,
            return title,page_sum
        else:
            print '获取帖子标题,帖子总页数失败'
            return None
    #获取内容并清洗出文字
    def clean_content(self,page_content):
        t=Tool()
        patten=re.compile(ur'<div id="post_content.*?>(.*?)</div>',re.S)
        items=re.findall(patten,page_content)
        res=''
        for item in items:

            # item=items[0]
            # print item
            res+=t.dispose_content(item)
        print res
        return res






class Tool(object):
    #匹配图片,多余的空格
    remove_img=re.compile(ur'<img(.*?)>| {8}',re.S)
    #匹配超链接
    remove_a=re.compile(ur'<a href=.*?>|</a>',re.S)
    #匹配<br>
    remove_br=re.compile(ur'<br><br>|<br>',re.S)
    replaceTD = re.compile('<td>')

    removeExtraTag = re.compile('<.*?>')
    def dispose_content(self,content):
        #剔除所有图片，超链接，保留超链接中的文本
        content=re.sub(self.remove_img,'\n    ',content)
        content=re.sub(self.remove_a,'',content)
        content = re.sub(self.replaceTD, '\t', content)
        # 将所有html换行符用\n替代
        content = re.sub(self.remove_br, '\n', content)
        content = re.sub(self.removeExtraTag, '', content)
        return content


# res=b.get_title_and_page_sum()  #纯原创我心中的NBA2014-2015赛季现役50大
# print res[0],res[1]



# b=BDTB('https://tieba.baidu.com/p/3138733512',1)
# # b.read_page(2)
#
# page_content=b.read_page(1)
# b.clean_content(page_content)
# t=Tool()

print '请输入帖子地址，如https://tieba.baidu.com/p/3138733512'
input_url=raw_input()
#初始化BDTB类
bdtb=BDTB(input_url)
bdtb.start()
