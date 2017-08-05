# -*-coding:utf-8-*-

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建一个BeautifulSoup对象
soup = BeautifulSoup(html,'lxml')


# 也可以通过本地文件来创建beautifulsoup对象
soup2=BeautifulSoup(open('html_demo.txt'),'lxml')

# 格式化输出soup的内容
print soup.prettify()

'''
<title>The Dormouse's story</title>

<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
1
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
上面的 title a 等等 HTML 标签加上里面包括的内容就是 Tag，下面我们来感受一下怎样用 Beautiful Soup 来方便地获取 Tags
'''
print soup.title        # <title>The Dormouse's story</title>

print soup.a        # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

# 对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下

# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
print soup.name       # [document]
print soup.a.name       # a

# attrs
# 取出a的所有属性
print soup.a.attrs      # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

# 取出a的单个属性
print soup.a.attrs['class']     # ['sister']
print soup.a.get('class')       # ['sister']

# 我们可以对这些属性和内容等等进行修改，例如

soup.a.attrs['class']='wang'
print soup.a.attrs      # {'href': 'http://example.com/elsie', 'class': 'wang', 'id': 'link1'}

# 获取标签内部的文字
print soup.head.string     # The Dormouse's story
print type(soup.head.string)    # <class 'bs4.element.NavigableString'>


# Comment
# Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
# 可以发现：a.string 输出的是注释的内容
print soup.a.string     # Elsie
print type(soup.a.string)       # <class 'bs4.element.Comment'>

#所以在取出内容时，加个判断
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
