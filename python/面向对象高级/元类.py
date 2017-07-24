#-*-encoding:utf-8-*-

#type()

from hello import Hello

'''
type()函数可以查看一个类型或变量的类型，Hello是一个class，
它的类型就是type，而h是一个实例，它的类型就是class Hello
'''
h=Hello()
print type(h)       #<class 'hello.Hello'>
print type(Hello)       #<type 'type'>（类属于）

#通过type创建Hello2类，而无需通过class Hello2(object)...的定义：
def say_hello(self,name):
    print 'hello,{0}'.format(name)

Hello2=type('Hello2',(object,),dict(hello=say_hello))  #创建Hello2 class

h2=Hello2()
h2.hello('wang')        #hello,wang
print Hello2        #<class '__main__.Hello2'>
print type(Hello2)      #<type 'type'>



#metaclass


