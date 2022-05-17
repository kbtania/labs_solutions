import matplotlib.pyplot as plt
import numpy as np

ALPHA = 1
BETA = 4
ROOT_RANGE = [4, 5]

DELTA = 0.00001
EPSILON = 0.0001
def x_i(alpha, beta):
    x_i = []
    for i in range(alpha, beta):
        x_i.append(i)
    return x_i

def fun(x):
    return 2 * np.log10(x) - x/2 + 1

def cal_val(fun, a, b):
    n = 1
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


x = cal_val(fun, ROOT_RANGE[0], ROOT_RANGE[1])

print(f'Корінь Х = {x}')
print(f'EPSILON = {EPSILON}')

fig = plt.subplots()
x = np.linspace(0.1, 6, 1000)
y1 = lambda x: 2*np.log10(x)
y2 = lambda x: x/2 - 1

plt.plot(x, y1(x))
plt.plot(x, y2(x))
plt.show()





