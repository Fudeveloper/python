#-*-coding:utf-8-*-

try:
    f=open('test.txt')
    print f.read()
except  IOError:
    print '未找到文件'
finally:
    f.close()

#hello

#为了方便,python 引入了with语句作为上下文管理器（自动释放资源）
with open('test.txt') as f:
    for line in f.readlines():        #hello
        print line.strip()


#按二进制方式读取文件：
with open('test.txt','rb') as bf:
    print bf.read()

#读取非ASCll编码的文件，就必须以二进制模式打开，再解码，如GBK编码文件
f=open('GBK.txt','rb')
u=f.read().decode('gbk')
print u     #测试

#with 方式
import codecs
with codecs.open('GBK.txt','rb','gbk') as f:
    print f.read()      #测试