# coding=utf-8
# author: kayi
# date: 2021/3/19
import os
# 多进程的fork只能用于unix的系统中
# pid = os.fork()
#
# if pid < 0:
#     print 'Fail to create process'
# elif pid == 0:
#     print 'I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

import os
from multiprocessing import Process

# 子进程要执行的代码
def child_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=child_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'