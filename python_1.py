import numpy as np
x_angle = 10
x_mat = np.mat([[1, 0, 0, 0], [0, cos(x_angle), sin(x_angle), 0], [0, -sin(x_angle), cos(x_angle), 0], [0, 0, 0, 1]])
x_angle = -10
x_mat_reverse = np.mat([[1, 0, 0, 0], [0, cos(-x_angle), sin(x_angle), 0], [0, -sin(x_angle), cos(x_angle), 0], [0, 0, 0, 1]])
z_mat = np.mat([[cos(2), sin(2), 0, 0], [-sin(2), cos(2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
# x_mat * z_mat != z_mat * x_mat
# x_mat * x_mat_reverse = I