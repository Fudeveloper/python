#-*-coding:utf-8-*-
#__str__

class Student(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'Student object {0}'.format(self.name)
    def __repr__(self):
        self.__repr__=self.__str__
s=Student('lio')
print s         #<__main__.Student object at 0x0000000002944438>
#加上__str__属性后
s=Student('lio')
print s     #Student object lio

#定义__repr__方法后，直接用s即可输出
s       #Student object lio


#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1    #初始化两个计数器a,b
    def __iter__(self):
        return self         #实例本身就是可迭代对象，故返回自己
    def next(self):
        self.a,self.b=self.b,self.a+self.b      #计算下一个值
        if self.a>10:     #退出循环的条件
            raise StopIteration()
        return self.a

f=Fib()
for i in f :
    print i
# 1
# 1
# 2
# 3
# 5
# 8

# print f[5]
#AttributeError: Fib instance has no attribute '__getitem__'

#加上'__getitem__'属性
class Fib2(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a
f2=Fib2()
print f2[10]        #89


#但是list有个神奇的切片方法：

print range(100)[5:10]      #[5, 6, 7, 8, 9]
#但是，传入list后Fib2()报错
# f2[5:10]        #TypeError: range() integer end argument expected, got slice.

class Fib3(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            res=[]
            a,b=1,1
            for x in  range(item.stop):
                if x>=item.start:
                    a,b=b,a+b
                    res.append(a)
            return res

f3=Fib3()
print f3[10]        #89

print f3[5:10]      #[1, 2, 3, 5, 8]

