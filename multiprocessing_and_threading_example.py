"""
Python3 Threading example

# ref: https://blog.csdn.net/qdx411324962/article/details/46810421

"""
import multiprocessing
import os
import threading


def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()


def multi_thread_main():
    print("Main", os.getpid())

    record = list()
    lock = threading.Lock()
    for i in range(5):
        thread = threading.Thread(target=worker,args=('thread',lock))
        thread.start()
        record.append(thread)

    for thread in record:
        thread.join()


def multi_process_main():
    # Multi-process
    record = []
    lock = multiprocessing.Lock()
    for i in range(5):
        process = multiprocessing.Process(target=worker,args=('process', lock))
        process.start()
        record.append(process)

    for process in record:
        process.join()


if __name__ == '__main__':
    multi_thread_main()
    multi_process_main()
