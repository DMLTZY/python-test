from concurrent.futures import ProcessPoolExecutor
import time, random


def aa(num):
    print('I am {}. It is in aa() and I will sleep'.format(num))
    a = random.random()
    time.sleep(a)
    print('{} sleeped {}'.format(num, a))


if __name__ == '__main__':
    with ProcessPoolExecutor(2) as ex:
        for i in range(1, 4):
            ex.submit(aa, (i,))
