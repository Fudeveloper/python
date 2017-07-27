#-*-coding:utf-8-*-
#注意摘要算法不是加密算法(md5,sha1)

import hashlib
md5=hashlib.md5()
md5.update('abc')
print md5.hexdigest()       #900150983cd24fb0d6963f7d28e17f72

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5=hashlib.md5()
md5.update('a')
md5.update('bc')
print md5.hexdigest()       #900150983cd24fb0d6963f7d28e17f72

#更安全的md5：“加盐”：

def get_md5(password):
    str=password + 'the-Salt'
    print str
    md5=hashlib.md5()
    md5.update(str)
    return md5.hexdigest()

print get_md5('abc')        #1df2f47fe809d5a18758093d9a004254
