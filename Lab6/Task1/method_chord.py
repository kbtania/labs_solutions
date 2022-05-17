import numpy as np

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

X = chord(fun)

print(f'X = {X}')
print(f'EPSILON = {EPSILON}')
