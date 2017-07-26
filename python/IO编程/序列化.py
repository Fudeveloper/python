#-*-coding:utf-8-*-

#只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''
Python提供两个模块来实现序列化：cPickle和pickle。
这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，
pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
用的时候，先尝试导入cPickle，如果失败，再导入pickle：
'''

try:
    import cPickle as pickle
except ImportError:
    import pickle

#将d转化为序列化对象
d={'name':'liu','age':6}
print pickle.dumps(d)
# (dp1
# S'age'
# p2
# I6
# sS'name'
# p3
# S'liu'
# p4
# s.

#将序列化对象存进文件
with open('dump.txt','w') as wf:
    pickle.dump(d,wf )

with open('dump.txt','rb') as rf:
    print pickle.load(rf)       #{'age': 6L, 'name': 'liu'}





