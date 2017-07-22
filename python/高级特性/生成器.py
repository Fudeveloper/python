#encoding=utf-8

#简单的生成器例子
L=[x for x in range(10)]
print L     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#将列表解析的[]换成（），即为生成器
g=(x+10 for x in L)

print g     #<generator object <genexpr> at 0x0000000002803870>     这是一个generator（生成器）

#循环读取生成器中的结果
for one in g:
    print one
#10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19

#函数中定义生成器方法

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1

fib(6)
# 1
# 2
# 3
# 5
# 8

#将print 改为yield,即为生成器
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib2(6)       #<generator object fib2 at 0x0000000002A73948>
for i in fib2(6):
    print i
# 1
# 2
# 3
# 5
# 8

#这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。

def order():
    print 'step1'
    yield 1
    print 'step2'
    yield 2
    print 'step3'
    yield 3
o=order()
print next(o)     #step1    #1
print next(o)     #step2    #2
print next(o)     #step3    #3
# print next(o)       #StopIteration