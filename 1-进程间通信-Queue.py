from multiprocessing import Process, Queue
import time
import random


def put_num(q):
    for i in range(5):
        q.put(i)
        print('得到数据--', i)
        time.sleep(random.random())


def get_num(q):
    while True:
        if not q.empty():
            data = q.get(True)
            print('取出数据-----', data)
            time.sleep(random.random())
        else:
            break


def main():
    q = Queue()
    t2 = Process(target=get_num, args=(q, ))
    t1 = Process(target=put_num, args=(q, ))
    t1.start()
    t1.join()

    t2.start()
    t2.join()
    print('')
    print("已全部读写完毕")


if __name__ == '__main__':
    main()
