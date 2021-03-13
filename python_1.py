import numpy as np
x_angle = 10
x_mat = np.mat([[1, 0, 0, 0], [0, cos(x_angle), sin(x_angle), 0], [0, -sin(x_angle), cos(x_angle), 0], [0, 0, 0, 1]])
x_angle = -10
x_mat_reverse = np.mat([[1, 0, 0, 0], [0, cos(-x_angle), sin(x_angle), 0], [0, -sin(x_angle), cos(x_angle), 0], [0, 0, 0, 1]])
z_mat = np.mat([[cos(2), sin(2), 0, 0], [-sin(2), cos(2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
# x_mat * z_mat != z_mat * x_mat
# x_mat * x_mat_reverse = I

def count():
    funcs = []
    for i in [1, 2, 3]:
        def g():
            tmp = int(i)    # 这里创建了一个匿名函数
            return tmp
        funcs.append(g)        # 将循环变量的值传给 g
    return funcs

def count():
    funcs = []
    for i in [1, 2, 3]:
        def g(param):
            tmp = lambda : param    # 这里创建了一个匿名函数
            return tmp
        # 必须要让循环中的i即时生效出来，而不是在函数延迟调用时才访问i的值
        funcs.append(g(i))        # 将循环变量的值传给 g
    return funcs


f1, f2, f3 = count()
f1()
f2()
f3()
