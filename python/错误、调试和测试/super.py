#-*-coding:utf-8

#总结

'''
Summary
如果类被设计成使用了super，那么所有子类也必须要调用super，否则直接调用会出现重复调用的问题
super调用的目标函数通常是用 *args, **kwargs 作为参数，这样可以解决目标函数参数匹配的问题
'''


'''
这里我们通过super来调用父类的__init__，
super(B, self)返回一个bounded对象（因为我们传入了self)。
从输出可以看到，调用正确。就像我们直接调用A.__init__(self)一样。
这样做的好处是，可以不用直接引用基类的名称就可以调用基类的方法。
如果我们改变了基类的名称，那么所有子类的调用将不用改变。
'''
class A(object):
    def __init__(self):
        print 'Enter A'
        print 'Leave A'

class B(A):
    def __init__(self):
        print 'Enter B'
        super(B,self).__init__()
        print 'Leave B'
B()
# Enter B
# Enter A
# Leave A
# Leave B


#但是super其实并不是我们想的那么简单，super不是简单地调用所谓基类的方法，
# 而是调用MRO中的下一个类的方法，也就是类似于next的方法。
# 这段代码摘自Python's Super Considered Harmful
class A(object):
    def __init__(self):
        print "A"
        super(A, self).__init__()
class B(object):
    def __init__(self):
        print "B"
        super(B, self).__init__()
class C(A):
    def __init__(self, arg):
        print "C","arg=",arg
        super(C, self).__init__()
class D(B):
    def __init__(self, arg):
        print "D", "arg=",arg
        super(D, self).__init__()
class E(C,D):
    def __init__(self, arg):
        print "E", "arg=",arg
        super(E, self).__init__(arg)
print "MRO:", [x.__name__ for x in E.__mro__]       #MRO: ['E', 'C', 'A', 'D', 'B', 'object']
E(10)

'''
出错的原因是因为调用继续到A.__init__时，我们调用了super(A,self).__init__。
记得上面我们说过super类似于next函数，是调用mro中下一个类型的方法。
这里我们给出的类型是A，那么mro中下一个类型就是D，
很显然，super将会调用D.__init__(self)。可是，D.__init__却接受一个额外的参数arg，所以调用错误
'''

#