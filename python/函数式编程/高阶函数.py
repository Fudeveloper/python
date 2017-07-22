#encoding=utf-8
#高阶函数意味着可以将函数名作为参数传递

print abs(-10)      #10

#将f绑定在abs上，通过f（）即可调用abs（）
f=abs
print f(-10)        #10


#定义一个方法，将函数名当做参数传递
def add(x,y,func):
    return func(x)+func(y)

print add(-9,9,abs)       #18
