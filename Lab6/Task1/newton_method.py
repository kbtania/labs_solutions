import numpy as np
import sympy
from scipy.misc import derivative

ALPHA = 1
BETA = 4
ROOT_RANGE = [4, 5]
DELTA = 0.00001
EPSILON = 0.0001

TAU = 0.5

def x_i(alpha, beta):
    x_i = []
    for i in range(alpha, beta):
        x_i.append(i)
    return x_i

def fun(x):
    return x**3-3*x**2+6*x+3

# def check():
#     d = derivative(fun, ROOT_RANGE[0], dx=1e-6, n=2)
#     f_val = fun(ROOT_RANGE[0])
#     return d * f_val

def newton():
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

X = newton()
print(X)
print(f'EPSILON = {EPSILON}')
