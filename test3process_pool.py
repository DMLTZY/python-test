from multiprocessing import Pool
import os, time, random


def pp(num):
    print("I'm {} process ({})".format(num, os.getpid()))
    time.sleep(random.random())
    print("{} sleep".format(num))

if __name__ == '__main__':
    print("The main process is {}".format(os.getpid()))
    p = Pool(4)
    for i in range(10):
        p.apply_async(func=pp, args=(i,))
    p.close()
    p.join()
    print('finish.')

