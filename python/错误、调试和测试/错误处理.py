#-*-coding:utf-8-*-

try:
    r=10/0
except  ZeroDivisionError:
    print '除数为0'
finally:
    print 'finally'
print 'end'

# 除数为0
# finally
# end



try:
    r=10/1
except  ZeroDivisionError:
    print '除数为0'
finally:
    print 'finally'
print 'end'

# finally
# end



#第二个例子
try:
    r=10/int('a')
except ValueError:
    print 'ValueError'
except ZeroDivisionError:
    print 'ZeroDivisionError'
else:
    print 'no error'
finally:
    print 'finally'

#ValueError
#finally


try:
    r=10/int('0')
except ValueError:
    print 'ValueError'
except ZeroDivisionError:
    print 'ZeroDivisionError'
else:
    print 'no error'
finally:
    print 'finally'

#ZeroDivisionError
#finally

#try中也可以使用else
try:
    r = 10 / int('4')
except ValueError:
    print 'ValueError'
except ZeroDivisionError:
    print 'ZeroDivisionError'
else:
    print 'no error'
finally:
    print 'finally'

#no error
#finally


#使用logging模块纪录错误,程序就算出错也可以在打印完错误后，继续执行并正常退出
import logging
try:
    r=10/0
except Exception,e:
    logging.exception(e)

print 'normal'
# ERROR:root:integer division or modulo by zero
# Traceback (most recent call last):
#   File "F:/learngit/python/python/�������߼�/������.py", line 79, in <module>
#     r=10/0
# ZeroDivisionError: integer division or modulo by zero

#normal


