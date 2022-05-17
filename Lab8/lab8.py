import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return 2 * np.e ** (x-1) + y


def f_initial(x):
    return (2 * x + 1) * np.e ** (x-1)


RANGE = [1, 2]
h = 0.1

x0 = 1
y0 = 3

def initial_function(x_0, h):
    x_res = []
    y_res = []
    while True:
        y = f_initial(x_0+h)
        x_res.append(round(x_0, 5))
        y_res.append(round(y, 5))
        x_0 = x_0 + h
        if x_0 > RANGE[1]:
            break
    return x_res, y_res

def euler_method(x_0, y_0, h):
    res_x = []
    res_y = []
    while True:
        y1 = y_0 + h * f(x_0, y_0)
        res_x.append(round(x_0, 5))
        res_y.append(round(y1, 5))
        y_0 = y1
        x_0 = x_0 + h
        if x_0 > RANGE[1]:
            break
    return res_x, res_y


euler = euler_method(x0, y0, h)
initial = initial_function(x0, h)
print(f'X = {initial[0]}')
print(f'Точний розв\'язок:\n{initial[1]}')
print(f'Метод Ейлера:\n{euler[1]}')
m = list(map(lambda x, y: abs(y-x), initial[1], euler[1]))
mistake = sum(m)/len(m)


plt.plot(euler[0], euler[1], marker="o")  # метод Ейлера

plt.plot(initial[0], initial[1])  # точне розв'язання

plt.show()
#print(euler[0])
#print(initial[0])
# print('xx = ', euler[0])
# print('yy = ', euler[1])
# print('y_init = ', initial[0])
# print('y_init = ', initial[1])