import gevent
from gevent import monkey
import time


monkey.patch_all()  # 让程序识别io操作


def work1(num):
    for i in range(num):
        print("\33[41;m-----我是分割线----\033[0m")
        # t2.switch()
        time.sleep(0.5)


def work2(num):
    for i in range(num):
        print("\33[45;m----I am splitters-----\033[0m")
        # t1.switch()
        time.sleep(0.5)


t1 = gevent.spawn(work1, 5)
t2 = gevent.spawn(work2, 5)

t1.join()
t2.join()