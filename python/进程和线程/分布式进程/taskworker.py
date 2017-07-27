#-*-coding:utf-8-*-
import  time,sys,Queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行taskmanager.py的机器:
address='127.0.0.1'
m=QueueManager(address=(address,5000),authkey='abc')
m.connect()

#获取Queue的对象
task=m.get_task_queue()
result=m.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n=task.get(timeout=10)
        print 'run task {0}'.format(n)
        r='{0}*{1}={2}'.format(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print 'Queue is Empty'

print 'work exit'