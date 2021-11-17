import math
import numpy as np
import matplotlib.pyplot as plt
import random

def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp


def product(n):
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p

def newton_poly(x, y, xp):
    sum = y[0][0]
    u = (xp - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        sum = sum + (u_cal(u, i) * y[0][i]) / product(i)
    return sum

def table_coeff(y):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
 # виведення таблиці

def print_table(x, y):
    for i in range(n):
        print(x[i], end="\t")
        for j in range(n - i):
            print(y[i][j], end="\t")
        print("")

def column(matrix, i):
    return [row[i] for row in matrix]

n = 10
m = 10
alpha = 1
beta = 2
h = (beta - alpha) / n

x = [(alpha + i * h) for i in range(n)]
y = [[0 for i in range(n)] for j in range(n)]

# заповнюємо значення f_i
for i in range(n):
    y[i][0] = round(x[i] * math.log(x[i], math.e) - x[i], 2)

table_coeff(y)
# print_table(x, y)


xp = float(input(f"Обчислити значення в точці (Х Є ({alpha}; {beta}])): "))


x_m = [(alpha + i * h) for i in range(m)]
y_m = [[0 for i in range(n)] for j in range(m)]
# заповнюємо значення f_i
for i in range(len(x)):
    y_m[i][0] = x_m[i] * math.log(x_m[i], math.e) - x_m[i]
# x_m.sort()
table_coeff(y_m)
all_n1 = list(map(lambda xi: newton_poly(x, y, xi), x))
all_n2 = list(map(lambda xi: newton_poly(x_m, y_m, xi), x_m))
e = max(list(map(lambda yi, ni: abs(yi - ni), column(y, 0), all_n2)))
print(f"x1 = {x}")
print(f"y1 = {column(y, 0)}")
print(f"x_m = {x_m} ")
print(f"y_m = {column(y_m, 0)}")
print(f"N1 = {all_n1}")
print(f"N2 = {all_n2}")
# print(f"N1 = {all_n1}")
print(f"Всі похибки = {list(map(lambda yi, li: abs(yi - li), column(y, 0), all_n2))}")
print(f"N({xp}) = {newton_poly(x, y, xp)}")
#print(f"e = {e}")

plt.plot(x, column(y, 0))  # blue
plt.plot(x, all_n2)  # orange
plt.show()
