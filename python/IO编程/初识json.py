#-*-coding:utf-8-*-
#将一个python对象转换成json对象：
d={'name':'liu','age':6}
import json
json_str=json.dumps(d)
print json_str      #{"age": 6, "name": "liu"}


print json.loads(json_str,encoding='unicode')
{'age': 6, 'name': 'liu'}

#JSON进阶

'''
Python的dict对象可以直接序列化为JSON的{}，
不过，很多时候，我们更喜欢用class表示对象，
比如定义Student类，然后序列化：
'''

class Student(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age

def stu2json(std):
    return {
        'name':std._name,
        'age':std._age
    }
s=Student('liu',6)
res=json.dumps(s,default=stu2json)
print res

#{"_age": 6, "_name": "liu"}

#讲一个json对象反序列化成python对象:
def json2stu(json_str):
    return Student(json_str['name'],json_str['age'])


s=json.loads(res,object_hook=json2stu)
print s  #返回一个stu对象
print s._name       #liu
#<__main__.Student object at 0x0000000002A207F0>






