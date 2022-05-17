import matplotlib.pyplot as plt
import numpy as np
import math
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
    return 2 * np.log10(x) - x/2 + 1

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


X = mixed_method(fun)

print(f'X = {X}')
print(f'EPSILON = {EPSILON}')
