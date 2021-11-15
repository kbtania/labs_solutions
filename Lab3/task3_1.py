import math
import numpy as np
import matplotlib.pyplot as plt

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

def table_coeff():
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
alpha = 1
beta = 2
h = (beta - alpha) / n

x = [round((alpha + i * h), 2) for i in range(n)]
y = [[0 for i in range(n)] for j in range(n)]

# заповнюємо значення f_i
for i in range(n):
    y[i][0] = round(x[i] * math.log(x[i], math.e) - x[i], 2)

print(f"X = {x}")
print(f"Y = {column(y, 0)}")

table_coeff()
print_table(x, y)

all_n = list(map(lambda xi: newton_poly(x, y, xi), x))
xp = float(input(f"Обчислити значення в точці (Х Є ({alpha}; {beta}])): "))
print(all_n)

e = max(list(map(lambda yi, ni: abs(yi - ni), column(y, 0), all_n)))

print(f"N({xp}) = {newton_poly(x, y, xp)}")
print(f"e = {e}")

# plt.plot(x, column(y, 0))  # blue
# plt.plot(x, all_n)  # orange
# plt.show()