import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

ALPHA = 1
BETA = 4
ROOT_RANGE = [0, 1]

DELTA = 0.00001
EPSILON = 0.001
def x_i(alpha, beta):
    x_i = []
    for i in range(alpha, beta):
        x_i.append(i)
    return x_i

def fun(x):
    return np.log10(2+x) + 2*x - 3
    #return 2 * np.log10(x) - x/2 + 1

def cal_val(fun):
    n = 1
    a = ROOT_RANGE[0]
    b = ROOT_RANGE[1]
    fa = fun(a)
    fb = fun(b)
    while True:
        if fa*fb > 0:
            break
        c = (a+b)/2
        fc = fun(c)
       # print(f'Ітерація [{n}]: x = {c}; f(a) = {fa}; f(b) = {fb}')
        n = n+1
        if abs(fc) < DELTA:
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        if b - a < EPSILON:
            break
    return c


def chord(f):
    a = ROOT_RANGE[0]
    b = ROOT_RANGE[1]
    i = 0
    while True:
        b_n = b - (((a-b) / (f(a) - f(b))) * f(b))
        temp = b
        b = b_n
        i += 1
        print(f'Ітерація [{i}]: x = {b_n}')
        if abs(b_n - temp) < EPSILON:
            break
    return b_n


def newton(fun):
    x = ROOT_RANGE[0]
    i = 0
    while True:
        x_new = x - (fun(x) / derivative(fun, x, dx=1e-6))
        temp = x
        x = x_new
        i += 1
        print(f'Ітерація [{i}]: x = {x_new}')
        if abs(x_new - temp) < EPSILON:
            break
    return x_new

def simple_iteration(f):
    x_0 = ROOT_RANGE[0]
    TAU = -0.5
    i = 0
    while True:
        x_k = x_0 + TAU * f(x_0)
        temp = x_0
        x_0 = x_k
        i += 1
        print(f'Ітерація [{i}]: xi = {x_k}')
        if abs(x_k - temp) < EPSILON:
            break
    return x_k

def mixed_method(f):
    a_0 = ROOT_RANGE[0]
    b_0 = ROOT_RANGE[1]
    i = 0
    while True:
        a_n = a_0 - f(a_0) / derivative(f, a_0, dx=1e-6)
        b_n = b_0 - ((a_0 - b_0) / (f(a_0) - f(b_0))) * f(b_0)
        a_0 = a_n
        b_0 = b_n
        i += 1
        print(f'Ітерація [{i}]: xi = {a_n}')
        if abs(b_0 - a_n) < EPSILON:
            break
    return a_n


#print(f'[Метод поділу відрізку пополам]: Х = {cal_val(fun)}\n')
fig = plt.subplots()
x = np.linspace(0.1, 6, 1000)
y1 = lambda x: np.log10(2+x)
y2 = lambda x: 3 - 2*x

plt.plot(x, y1(x))
plt.plot(x, y2(x))
plt.show()
print(f'[Метод хорд]: Х = {chord(fun)}\n')
print(f'[Метод Ньютона (дотичних)]: Х = {newton(fun)}\n')
print(f'[Метод простих ітерацій]: Х = {simple_iteration(fun)}\n')
print(f'[Комбінований метод хорд і дотичних]: Х = {mixed_method(fun)}\n')
print(f'EPSILON = {EPSILON}')







