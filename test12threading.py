# import threading, multiprocessing
#
# balance = 0
# ll = threading.Lock()
#
#
# def aa(n):
#     global balance
#     balance += n
#     balance -= n
#
#
# def bb(n):
#     for _ in range(1000000):
#         ll.acquire()
#         aa(n)
#         ll.release()
#
# t1 = threading.Thread(target=bb, args=(4,))
# t2 = threading.Thread(target=bb, args=(6,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# --------------------------------------------------------------
import threading
import time


def aa(n):
    print("aa():I'm in aa(), I get {}.".format(n))
    print("aa(): need to sleep 10 sec.")
    time.sleep(10)
    print("aa(): awake.")


def bb(n):
    print("bb():I'm in bb(), I get {}.".format(n))
    print("bb(): need to sleep 14 sec.")
    time.sleep(14)
    print("bb(): awake.")


th = []
th.append(threading.Thread(target=aa, args=(123,), name='a'))
th.append(threading.Thread(target=bb, args=(454,), name='b'))
print(">I have created 2 threads, I will start them.")
for i in range(len(th)):
    print(">I start {} now.".format(th[i].getName()))
    th[i].start()
print(">I do 1 thing in main()")
for i in range(len(th)):
    print(">I wait threads end, use join")
    th[i].join()
print(">Threads should be done...")