from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('process to write: {}'.format(os.getpid()))
    for value in ['***a', '***b', '***c']:
        print('put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read: {}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('I get {}'.format(value))


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()