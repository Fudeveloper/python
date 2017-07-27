#-*-coding:utf-8-*-

#用一个全局dict存放所有的Student对象，
#然后以thread自身作为key获得线程对应的Student对象
#则可以解决传参问题
class Student(object):
    def __init__(self,name):
        self._name=name


import threading
global_dict={}

def run_thread(name):
    std=Student(name)
    global_dict[threading.current_thread()]=std
    print threading.current_thread()       #<_MainThread(MainThread, started 158284)>
    do_task1()
    do_task2()

def do_task1():
    #根据当前线程查找所需要值
    std=global_dict[threading.current_thread()]
    print std._name
def do_task2():
    std=global_dict[threading.current_thread()]
    print std._name
run_thread('wang')


#ThreadLocal自动实现上方所示功能
import threading
#创建全局ThreadLocal对象
local_school=threading.local()
def student_thread(name):
    local_school.student=name
    student_process()
def student_process():
    print 'hello,{0} in {1}'.format(local_school.student,threading.current_thread().name)

#执行线程时，函数所需参数应放在args=中
t1=threading.Thread(target=student_thread,args=('lili',), name='thread--1')
t2=threading.Thread(target=student_thread,args=('liu',), name='thread--2')
t1.start()
t2.start()
t1.join()
t2.join()

# hello,lili in thread--1
# hello,liu in thread--2




