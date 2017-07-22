#encoding=utf-8
#筛选出偶数
def is_odd(x):
    return x%2==0
print filter(is_odd,[1,2,3,4,5,6])      #[2, 4, 6]

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print filter(not_empty,{'a','','b','c',''})     #['a', 'c', 'b']