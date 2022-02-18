import time
import os
# 引入模块
import multiprocessing
import numba
from numba import  jit


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
#     count_process1 = multiprocessing.Process(target=count_number,args=(10000000,)) #创立多线程任务，以元组的方式指定任务传参
#     count_process2 = multiprocessing.Process(target=count_num, kwargs={"num": 10000000})#创立多线程任务，以字典的方式指定任务传参
#     #设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
#     count_process1.daemon = True
#     count_process2.daemon = True
#     count_process2.start()
#     count_process1.start()
#
#     print("主进程执行完毕")
#
#     #进程的注意点
#     # 1. 主进程会等待所有子进程执行结束后再结束
#     # 2. 如果想要主进程关闭时子进程同时关闭的效果，可以设置守护主进程
#     # 3.设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码

@jit(nopython = True)
def count(num):
    k = 1
    for i in range (1,num):
        if i >= k:
            k = i
    print(k)
t1 =time.time()
count(10000000000)
t2=time.time()
print(t2-t1)


