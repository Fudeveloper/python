#-*-coding:utf-8-*-

#自己编写一个错误类

class MyError(StandardError):
    pass

def tt(nn):
    if nn==0:
        raise MyError('param=0')


tt(0)       #__main__.MyError: param=0