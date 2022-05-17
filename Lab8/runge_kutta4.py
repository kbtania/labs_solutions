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


def runge_kutta_4_order(x_0, y_0, h):
    res_x = []
    res_y = []
    # k1 = f(x_0, y_0)
    # k2 = f(x_0+h, y_0+k1*h)
    while True:
        k1 = f(x_0, y_0)
        k2 = f(x_0 + h/2, y_0 + k1 * (h/2))
        k3 = f(x_0 + h/2, y_0+k2*(h/2))
        k4 = f(x_0+h, y_0+k3*h)
        y1 = y_0 + (1/6*k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4) * h
        res_x.append(round(x_0, 5))
        res_y.append(round(y1, 5))
        y_0 = y1
        x_0 = x_0 + h
        if x_0 > RANGE[1]:
            break
    return res_x, res_y


runge = runge_kutta_4_order(x0, y0, h)
initial = initial_function(x0, h)
print(f'X = {initial[0]}')
print(f'Точний розв\'язок:\n{initial[1]}')
print(f'Метод Рунге-Кутта:\n{runge[1]}')
m = list(map(lambda x, y: abs(y-x), initial[1], runge[1]))
mistake = sum(m)/len(m)
print('Максимальна похибка = ', mistake)


plt.plot(runge[0], runge[1], marker="o")  # метод Рунге-Кутта

plt.plot(initial[0], initial[1])  # точне розв'язання

plt.show()
