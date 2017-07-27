#-*-coding:utf-8-*-
from multiprocessing import Process
import os

#window中没有fork
# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'


#进程间通信
#我们以Queue为例，在父进程中创建两个子进程，
# 一个往Queue里写数据，一个从Queue里读数据：

import multiprocessing,os,time,random
#写数据进程执行的代码
def write(q):
    for value in ['A','B','C']:
        print 'put {0} to queue'.format(value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    while True:
        value=q.get()
        print 'get {0} from queue'.format(value)

if __name__=='__main__':
    #父进程创建Queue，并传递给子进程
    q=multiprocessing.Queue()
    pw=multiprocessing.Process(target=write,args=(q,))
    pr=multiprocessing.Process(target=read,args=(q,))

    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr中循环为死循环，只能强制停止
    pr.terminate()






