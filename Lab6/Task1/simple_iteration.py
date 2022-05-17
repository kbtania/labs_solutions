import matplotlib.pyplot as plt
import numpy as np
import math

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
    return 2 * np.log10(x) - x/2 + 1

def simple_iteration(f):
    x_0 = ROOT_RANGE[0]
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


X = simple_iteration(fun)

print(f'X = {X}')
print(f'EPSILON = {EPSILON}')
