#-*-coding:utf-8-*-
import random,Queue,time
from multiprocessing.managers  import BaseManager
from multiprocessing import freeze_support
class QueueManager(BaseManager):
    pass

#定义发送任务和接受任务的队列
def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue

task_queue=Queue.Queue()
result_queue=Queue.Queue()

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue',callable=get_task_queue)
QueueManager.register('get_result_queue',callable=get_result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey='abc')

# 启动Queue

server = manager.get_server()

server.serve_forever()
def communicate():
    # 获得通过网络访问的Queue对象:
    task=manager.get_task_queue()
    result=manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=1)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()




if __name__ == '__main__':
    freeze_support()
    # 启动Queue:
    manager.start()
    communicate()