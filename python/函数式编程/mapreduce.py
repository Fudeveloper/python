#encoding=utf-8
#map
'''
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
'''
def f(x):
    return x**2
L=[1,2,3,4,5,6,7,8]
print map(f,L)      #[1, 4, 9, 16, 25, 36, 49, 64]

print map(str,L)       #print map(str,L)

#reduce
'''reduce把一个函数作用在一个序列[x1, x2, x3...]上，
这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算
'''
def add(x,y):
    return x+y
print reduce(add,L)     #36

def fn(x,y):
    return 10*x+y
print reduce(fn,L)      #12345678


#mapreduce 模拟int()
def str2int(s):
    def char2int(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        return 10*x+y
    return reduce(fn,map(char2int,s))

print str2int('12341')

#用lambda方式
def str2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def num2int(num):
    return reduce(lambda x,y:10*x+y,map(str2num,num))

print num2int('123456')



