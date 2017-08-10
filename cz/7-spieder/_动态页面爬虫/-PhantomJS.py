# -*-coding:utf-8-*-

# 导入webdriver库
from selenium import webdriver
import time
# r表示原始字符
driver=webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 打开页面
driver.get('http://www.baidu.com')

# 根据id寻找“把百度设为主页”标签
element=driver.find_element_by_id('setf')     # <selenium.webdriver.remote.webelement.WebElement (session="f34a7c50-7c12-11e7-9d20-072ea3a1eb33", element=":wdc:1502180651399")>

print element.text      # 把百度设为主页

# 保存页面快照
driver.save_screenshot('baidu.png')


# 导入操作包Keys
from selenium.webdriver.common.keys import Keys

# 根据id找到搜索框
driver.find_element_by_id('kw').send_keys(u'美女图片')

# 截屏
# driver.save_screenshot('keys.png')

# 网页源码
# print driver.page_source

# 使用键盘命令：比如全选（ctrl+a）
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(5)
# 模拟输入回车键
driver.find_element_by_id('kw').send_keys(Keys.RETURN)
driver.save_screenshot(ur'全选.png')
