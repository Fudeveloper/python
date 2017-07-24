#-*-coding:utf-8-*-
class MyDict(dict):
    def __init__(self,**kwargs):
        super(MyDict,self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('myDict\'obj has no attribute {0}'.format(key))

    def __setattr__(self, key, value):
        self[key]=value
'''
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，

我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEquals()：
'''
import unittest
class TestMyDict(unittest.TestCase):
    def test_init(self):
        d=MyDict(a=1,b='test')
        self.assertEqual(d.a,1)     #对比字符串
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))     #d是否为dict类型

    def test_key(self):
        d=MyDict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

#另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError

    def test_keyerror(self):
        d=MyDict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

#加上以下两行执行测试
if __name__ == '__main__':
    unittest.main()