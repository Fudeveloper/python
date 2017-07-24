#-*-coding:utf-8-*-

##最常使用的调试方法是logging和ide

'''第一种方法简单直接粗暴有效，就是用print把可能有问题的变量打印出来看看：'''
# def foo(s):
#     n = int(s)
#     print '>>> n = {0}'.format(n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

'''
用print最大的坏处是将来还得删掉它，想想程序里到处都是print，
运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
'''

#凡是用print来辅助查看的地方，都可以用断言（assert）来替代：
'''assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错。

如果断言失败，assert语句本身就会抛出AssertionError：'''
def assert_t(int):
    assert int!=0,'n is zero'

assert_t(1)
# assert_t(0)     #AssertionError: n is zero

'''logging

把print替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：'''

'''这就是logging的好处，它允许你指定记录信息的级别，
有debug，info，warning，error等几个级别，当我们指定level=INFO时，
logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，
比如console和文件。'''

# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n={0}'.format(n))
# print 10/n

#INFO:root:n=0
#ZeroDivisionError: integer division or modulo by zero


import pdb

n=0
for n in range(100):
    pdb.set_trace()
    pass


