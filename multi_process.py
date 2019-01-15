import multiprocessing
import os


def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

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
    multi_process_main()

