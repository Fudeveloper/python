#-*-coding:utf-8-*-

import threading,time
def loop():
    print '{0} is running'.format(threading.current_thread().name)
    x=0
    while x<5:
        print '{0} >>> {1}'.format(threading.current_thread().name,x)
        x=x+1
    print '{0} is end'.format(threading.current_thread().name)

print '{0} is running'.format(threading.current_thread().name)
tloop=threading.Thread(target=loop,name='LoopThread')
tloop.start()
tloop.join()

print '{0} is end'.format(threading.current_thread().name)

# MainThread is running
# LoopThread is running
# LoopThread >>> 0
# LoopThread >>> 1
# LoopThread >>> 2
# LoopThread >>> 3
# LoopThread >>> 4
# LoopThread is end
# MainThread is end

#Lock
#为了保证数据的正确性，使用lock
#包含锁的某段代码实际上只能以单线程模式执行

lock=threading.Lock()
print lock      #<thread.lock object at 0x0000000002402170>
def run_thread():
    for i in range(1000):
        #先获取锁
        lock.acquire()
        try:
            print i
        #最后一定要释放锁
        finally:
            lock.release()

run_thread()