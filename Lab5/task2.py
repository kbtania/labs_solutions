import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from math import cos, exp, pi


ALPHA = 1
BETA = 2
N_h = BETA - ALPHA
N = 10
polynom_power = 5
# xj = ALPHA + jh
X = [x * 0.1 for x in range(10, 20)]
Y = list(map(lambda x: x * math.log(x, math.e) - x, X))

# f = lambda x: x * math.log(x, math.e) - x
f_c = lambda x, n: x ** n
f_d = lambda x, n:  (x * math.log(x, math.e) - x)* (x ** n)


def get_C(func):
    coefficients_C = []
    for i in range(polynom_power*2+1):
        coefficients_C.append(integrate.quad(func, ALPHA, BETA, args=(i,))[0])
    return coefficients_C


def get_D(func):
    coefficients_D = []
    for i in range(polynom_power+1):
        coefficients_D.append(integrate.quad(func, ALPHA, BETA, args=(i,))[0])
    return coefficients_D

def create_matrix(arr):
    matrix = []
    start = 0
    finish = arr.index(arr[polynom_power])
    for i in range(len(arr)):
        matrix.append(arr[start:finish+1])
        start += 1
        finish += 1
        if finish >= len(arr): break
    return matrix


C = get_C(f_c)
D = get_D(f_d)

C_matrix = np.array(create_matrix(C))
D_matrix = np.array(create_matrix(D))[0]

a = np.linalg.solve(C_matrix, D_matrix)

p = np.poly1d(np.flip(a))
print(f'[ m = {polynom_power} ] Поліном: {p}')
P = list(map(lambda x: p(x), X))  # значення поліному в точках Х

# ---------- Похибки ----------
errors = list(map(lambda y, p: y - p, Y, p))
average_error = math.sqrt(sum(list(map(lambda x: x ** 2, errors))) / N + 1)
print(f'[ m = {polynom_power} ] Похибки: ', errors)
print(f'[ m = {polynom_power} ] Похибка середньоквадратичного наближення: ', average_error)

# ---------- Graphics ---------
plt.plot(X, Y, linestyle="", marker="o")  # початкова функція (точки)

plt.plot(X, P)  # поліном

plt.show()





