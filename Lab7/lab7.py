import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def x1(y):
    return np.sin(y + 2) - 1.5


def y2(x):
    return 0.5 - np.cos(x - 2)


def partial_derivative(f, variable, points):  # значення частинної похідної в точці
    x, y = symbols('x y')
    func = lambda x, y: f
    derivative_x = lambdify((x, y), diff(func(x, y), x))
    derivative_y = lambdify((x, y), diff(func(x, y), y))
    if variable == 'x':
        return derivative_x(points[0], points[1])
    if variable == 'y':
        return derivative_y(points[0], points[1])


EPSILON = 0.1
f1 = lambda x, y: np.sin(y+2) - x - 1.5
f2 = lambda x, y: y + np.cos(x - 2) - 0.5
equation1 = 'sin(y+2) - x - 1.5'
equation2 = 'y + cos(x-2) - 0.5'
x0 = np.array([-10, 10])  # початкове наближення


def newton(x_0):
    i = 0
    while True:
        f_x = np.array(f1(x_0[0], x_0[1]))
        f_y = np.array(f2(x_0[0], x_0[1]))
        f_x0 = np.array([f_x, f_y])
        df_x0_1 = partial_derivative(equation1, 'x', x_0)
        df_x0_2 = partial_derivative(equation1, 'y', x_0)
        df_x0_3 = partial_derivative(equation2, 'x', x_0)
        df_x0_4 = partial_derivative(equation2, 'y', x_0)
        df_x0 = np.array([[df_x0_1, df_x0_2], [df_x0_3, df_x0_4]])
        f_inverse = np.linalg.inv(df_x0)
        x_1 = np.subtract(x_0, np.dot(f_inverse, f_x0))
        i += 1
        print(f'[i={i}]: x, y = {x_1}')
        if max(np.abs(x_1[0] - x_0[0]), np.abs(x_1[1] - x_0[1])) <= EPSILON:
            break
        x_0 = x_1
    return x_1

def relaxation(x_0):
    TAU = -0.4
    eps = 0.1
    i = 0
    while True:
        f_x = np.array(f1(x_0[0], x_0[1]))
        f_y = np.array(f2(x_0[0], x_0[1]))
        f_x_0 = np.array([f_x, f_y])
        x_1 = -f_x_0*TAU + x_0
        i += 1
        print(f'[i={i}]: x, y = {x_1}')
        if max(np.abs(x_1[0] - x_0[0]), np.abs(x_1[1] - x_0[1])) <= eps:
            break
        x_0 = x_1
    return x_1

def jacobi(x_0):
    x = lambda y: np.sin(y+2) - 1.5
    y = lambda x: 0.5 - np.cos(x-2)
    i = 0
    while True:
        x_1 = x(x_0[1])
        y_1 = y(x_0[0])
        x_next = [x_1, y_1]
        i += 1
        print(f'[i={i}]: x, y = {x_next}')
        if max(np.abs(x_next[0]-x_0[0]), np.abs(x_next[1]-x_0[1])) <= EPSILON:
            break
        x_0 = x_next
    return x_next


def zeidel(x_0):
    x = lambda y: np.sin(y+2) - 1.5
    y = lambda x: 0.5 - np.cos(x-2)
    i = 0
    while True:
        x_1 = x(x_0[1])
        y_1 = y(x_1)
        x_next = [x_1, y_1]
        i += 1
        print(f'[i={i}]: x, y = {x_next}')
        if max(np.abs(x_next[0] - x_0[0]), np.abs(x_next[1] - x_0[1])) <= EPSILON:
            break
        x_0 = x_next
    return x_next


y1 = np.linspace(-3, 3, 100)
x2 = np.linspace(-3, 3, 100)


plt.plot(x1(y1), y1)
plt.plot(x2, y2(x2))
plt.show()
print('[Метод Ньютона] = ', newton(x0))
print('[Метод Якобі] = ', jacobi(x0))
print('[Метод Зейделя] = ', zeidel(x0))
#print('[Метод релаксації] = ', relaxation(x0))
#print('[Метод Зейделя] = ', zeidel(x0))
