import numpy as np
import math
from scipy.misc import derivative


def change_sign(a, b):
    if a * b < 0:
        return 1
    return 0


def sturm(x):
    p = []
    p.append(np.poly1d(x))
    p.append(np.polyder(p[0]))  # похідна
    while True:
        remainder = np.polydiv(p[len(p)-2], p[len(p)-1])[1]  # ділення кутом
        if remainder == np.poly1d(0):
            break
        p.append(-remainder)
    return p


def roots(p):
    changes = 0
    bound = 10000
    for x in range(len(p)-1):
        changes += change_sign(np.polyval(p[x], -bound), np.polyval(p[x+1], -bound))
    for x in range(len(p)-1):
        changes -= change_sign(np.polyval(p[x], bound), np.polyval(p[x+1], bound))
    return changes


def intervals(p):
    numRoot = roots(p)
    num = numRoot
    interval = []
    upperbound = 1000
    for x in range(num-1):
        changes = numRoot - x
        if x == 0:
            lowerbound = -1000
        else:
            lowerbound = interval[x-1]
        while(changes == numRoot-x):
            changes = 0
            lowerbound += .5
            for y in range(len(p)-1):
                changes += change_sign(np.polyval(p[y], lowerbound), np.polyval(p[y+1], lowerbound))
            for y in range(len(p)-1):
                changes -= change_sign(np.polyval(p[y], upperbound), np.polyval(p[y+1], upperbound))
        interval.append(lowerbound-.5)

    numRoot = 0
    for y in range(len(p)-1):
        numRoot += change_sign(np.polyval(p[y], upperbound), np.polyval(p[y+1], upperbound))
    changes = numRoot
    while changes == numRoot:
        changes = 0
        upperbound -= 1
        for y in range(len(p)-1):
            changes += change_sign(np.polyval(p[y], upperbound), np.polyval(p[y+1], upperbound))
    interval.append(upperbound)
    interval.append(upperbound+1)
    return interval


f0 = [1.0, -3.0, 9.0, 2.0]
ROOT_RANGE = [intervals(sturm(f0))[0], intervals(sturm(f0))[1]]

DELTA = 0.00001
EPSILON = 0.0001

def x_i(alpha, beta):
    x_i = []
    for i in range(alpha, beta):
        x_i.append(i)
    return x_i

def fun(x):
    return x**3 - 3*x**2 + 9*x +2

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
        print(f'Ітерація [{n}]: x = {c}; f(a) = {fa}; f(b) = {fb}')
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
    TAU = -0.1
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

print("Кільксть коренів: ", roots(sturm(f0)))
print("Інтервали: ", ROOT_RANGE)
# x = cal_val(fun, ROOT_RANGE[0], ROOT_RANGE[1])

# print(f'[Поділ відрізку пополам]: Х = {cal_val(fun)}\n')
# print(f'[Метод хорд]: Х = {chord(fun)}\n')
print(f'[Метод Ньютона]: Х = {newton(fun)}\n')
print(f'[Метод простих ітерацій]: Х = {simple_iteration(fun)}\n')
print(f'[Комбінований метод хорд і дотичних]: Х = {mixed_method(fun)}\n')
print(f'EPSILON = {EPSILON}')

