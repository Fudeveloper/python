#-*-coding:utf-8-*-

'''
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，
表示补了多少字节，解码的时候，会自动去掉。

Python内置的base64可以直接进行base64的编解码：

'''
import base64
res=base64.b64encode('wang')        #d2FuZw==
print res
print base64.b64decode(res)     #wang

'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')     #abcd++//

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')     #abcd--__

#编写一个自动补齐=号并解码的函数
def decode(str):
    return base64.b64decode(str+(4-(len(str)%4))*'=')

str='d2FuZw'
print decode(str)       #wang
