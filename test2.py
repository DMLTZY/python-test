from multiprocessing import Process
import os, time


def run_proc(name):
    print('Run child process {} ({})...'.format(name, os.getpid()))
    print('This will sleep 3s')
    time.sleep(3)
    print('OK, I am done.')

if __name__ == '__main__':
    print('Parent pocess {}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('**659659**',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
