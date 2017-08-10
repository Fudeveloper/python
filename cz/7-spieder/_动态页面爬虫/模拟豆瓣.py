# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 创建PhantomJS浏览器对象
webdriver=webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

webdriver.get('https://www.douban.com/')
# 截屏
webdriver.save_screenshot('douban.png')

captcha=raw_input('验证码:\n')
# 输入账号
webdriver.find_element_by_id('form_email').send_keys('13960942437')

# 输入密码
webdriver.find_element_by_id('form_password').send_keys('wo951127')

# 输入验证码
webdriver.find_element_by_id('captcha_field').send_keys(captcha)

#点击登陆
webdriver.find_element_by_class_name('bn-submit').click()



webdriver.save_screenshot('login.png')
