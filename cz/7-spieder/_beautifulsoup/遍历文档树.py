# -*-coding:utf-8-*-

from bs4 import BeautifulSoup


soup=BeautifulSoup(open('html_demo.txt'),'lxml')
# 1)直接子节点

# tag 的 .content 属性可以将tag的子节点以列表的方式输出
print soup.body.contents

# [u'\n', <p class="title" name="dromouse"><b>The Dormouse's story</b></p>, u'\n', <p class="story">Once upon a time there were three little sisters; and their names were\n<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,\n<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and\n<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;\nand they lived at the bottom of a well.</p>, u'\n', <p class="story">...</p>]

# .children返回的不是一个 list，不过我们可以通过遍历获取所有子节点。

for everyone in soup.body.children:
    print everyone
'''
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>


<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


<p class="story">...</p>
'''

#  （2）所有子孙节点
# .contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。

for everyone in soup.body.descendants:
    print everyone


