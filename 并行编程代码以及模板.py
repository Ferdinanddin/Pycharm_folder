import time
import os
# 引入模块
import multiprocessing
from multiprocessing import Pool
#
# def work():
#     #获取当前进程编号
#     print("work进程编号：", os.getpid())
#     #获取父进程的编号
#     print("work父进程的编号：", os.getppid())
#
# def count_number(num):
#     print("count_cumber的进程编号：", os.getpid())
#     t1 = time.time()
#     for i in range(1, num):
#         k = 1
#         if i >= k:
#             k = i
#     t2 = time.time()
#     t = t2-t1
#     print(k)
#     print(t)
#     return k, t
#
# def count_num(num):
#     print("count_cum的进程编号：", os.getpid())
#     t1 = time.time()
#     for i in range(1, num):
#         k = 1
#         if i >= k:
#             k = i
#     t2 = time.time()
#     t = t2-t1
#     print(k)
#     print(t)
#     return k, t
# if __name__ == '__main__':
#     #2. 使用进程类创建进程对象
#     # target： 指定进程执行的函数名
#     #args： 使用元组方式给指定任务传参
#     #          元组的元素顺序就是任务的参数顺序
#     #kwargs： 使用字典方式给指定任务传参
#     #           key名就是参数的名字
#
#     # count_process1 = multiprocessing.Process(target=count_number,args=(10000000,)) #创立多线程任务，以元组的方式指定任务传参
#     # count_process2 = multiprocessing.Process(target=count_num, kwargs={"num": 10000000})#创立多线程任务，以字典的方式指定任务传参
#     # #设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
#     # count_process1.daemon = True
#     # count_process2.daemon = True
#     # count_process2.start()
#     # count_process1.start()
#
#     print("主进程执行完毕")
#
#     #进程的注意点
#     # 1. 主进程会等待所有子进程执行结束后再结束
#     # 2. 如果想要主进程关闭时子进程同时关闭的效果，可以设置守护主进程
#     # 3.设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
#
#
#
#
#





'''


多线程


'''
#为什么使用多线程： 线程是程序执行的最小单位，线程可以与同属一个进程的其他线程共享进程所拥有的所有资源
#就如同一个QQ软件（进程）打开两个窗口（线程）跟两个人聊天一样，实现多任务的同时节省了资源。
# 线程的创建步骤
# 1.导入线程模块
# 2. 通过线程类创建线程对象
# 3. 启动线程执行任务

# #1.
# import threading
# #2.
# # 线程对象 = threading.Thread(target=任务名)
# # #3.
# # 线程对象.start()
# def count_number():
#     t1 = time.time()
#     for i in range(1, 100000000):
#         k = 1
#         if i >= k:
#             k = i
#     t2 = time.time()
#     t = t2-t1
#     print(k)
#     print(t)
#     return k, t
#
# def count_num():
#     t1 = time.time()
#     for i in range(1, 100000000):
#         k = 1
#         if i >= k:
#             k = i
#     t2 = time.time()
#     t = t2-t1
#     print(k)
#     print(t)
#     return k, t
# if __name__ == '__main__':
#     #2. 使用线程 类创建进程对象
#     # target： 指定进程执行的函数名
#     #args： 使用元组方式给指定任务传参
#     #          元组的元素顺序就是任务的参数顺序
#     #kwargs： 使用字典方式给指定任务传参
#     #           key名就是参数的名字
#     count_num_thread = threading.Thread(target=count_num)
#     count_number_thread = threading.Thread(target=count_number)
#     count_number_thread.start()
#     count_num_thread.start()
#     #两种方法守护主线程
#     #1.创建的时候设置参数daemon
#     count_num_thread = threading.Thread(target=count_num, daemon=True)
#     #2.在启动之前通过setDaemon传参
#     count_num_thread.setDaemon(True)
#     count_num_thread.start()
#
#
#
#     ###线程之间的执行顺序：无序的,是由操作系统调度的
#     #可以用for 函数创建range长度的线程数量进行执行任务
#     for i in range(5):
#         count_num_thread = threading.Thread(target=count_num)
#         count_num_thread.start()
#
#
#
#
#     '''线程和进程对此
#     创建进程的资源开销比创建线程的资源开销大
#     进程是由操作系统资源分配的基本单位，线程是CPU调度的基本单位
#     '''





'''


进程池


'''
import multiprocessing as mp
import numba
from numba import  jit
import timeit


@jit(nopython=True)
def count_number():
    k = 0
    for i in range(100000000):
        if i >= k:
            k = i
    print(k)


t1=time.time()
count_number()
t2 = time.time()
print(t2 - t1)


def count_num(name, num,result_dict, result_lock):
    t1 = time.time()
    for i in range(num):
        k = 1
        if i >= k:
            k = i

    # 在并行运算结束之后，我们通过 print() 函数来查看字典里的结果。
    # 注意这里既然出现了可以共享的数据类，我们就要再次通过锁 (Lock) 来避免资源竞争，
    #所以同时通过 Manager 创建了锁 Lock 类，以第四个参数传入计算函数，并且用 With 语境来锁住共享的字典类。
    with result_lock:
        result_dict[name] = k
    t2=time.time()
    print(k)
    print(t2-t1)
    return k


if __name__ == '__main__':

    t1 = time.time()
    num_cores = int(mp.cpu_count())
    print(num_cores)
    pool = mp.Pool(num_cores)
    param_dict = {'task1': list(range(1, 10000000)),
                  'task2': list(range(10000000, 20000000)),
                  'task3': list(range(20000000, 30000000)),
                  'task4': list(range(30000000, 40000000)),
                  'task5': list(range(40000000, 50000000)),
                  'task6': list(range(50000000, 60000000)),
                  'task7': list(range(60000000, 70000000)),
                  'task8': list(range(70000000, 80000000)),
                  'task9': list(range(80000000, 90000000)),
                  'task10': list(range(90000000, 100000000))}
    #创建manager来当作多进程共享的数据容器
    manager = mp.Manager()
    managed_locker = manager.Lock()
    managed_dict = manager.dict()
    results = [pool.apply_async(count_number, args=(name, num, managed_dict, managed_locker)) for name, num in param_dict.items()]
    #results是list的形式 如果你检查列表 results 里的类，你会发现 apply_async() 返回的是 ApplyResult，也就是调度结果类。
    # 这里用到了 Python 的异步功能，目前教程还没有讲到，简单的来说就是一个用来等待异步结果生成完毕的容器。
    results = [p.get() for p in results]  #用p.get获得results结果里面的每一个list
    print(managed_dict)
    t2 = time.time()
    t = t2-t1
    print(t)
'''这里我们用 Manager 来创建一个可以进行进程共享的字典类，随后作为第三个参数传入计算函数中。
计算函数把计算好的结果保存在字典里，而不是直接返回。在并行运算结束之后，我们通过 print() 函数来查看字典里的结果。
注意这里既然出现了可以共享的数据类，我们就要再次通过锁 (Lock) 来避免资源竞争，
所以同时通过 Manager 创建了锁 Lock 类，以第四个参数传入计算函数，并且用 With 语境来锁住共享的字典类。
'''


