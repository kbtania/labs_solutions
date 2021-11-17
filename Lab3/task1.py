import math
import matplotlib.pyplot as plt
import random
import numpy as np

steps = 10
a = 1
b = 2


def generate_x_i(alpha, beta, n):
    x_i = []
    for i in range(1, n):
        x_i.append(((beta + alpha) / 2) + ((beta - alpha)/2) * math.cos(math.pi * (2 * i + 1)/(2*(n + 1))))
    return x_i


def generate_f_i(x_i):
   # x_i = generate_x_i(a, b, steps)
    f_i = list(map(lambda x: x * math.log(x, math.e) - x, x_i))
    return f_i


def lagrange(x, y, xp=0.5):
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if j != i:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * p
    return yp


xp = float(input(f"Обчислити значення в точці (Х Є [{a}; {b}]): "))
x = generate_x_i(a, b, steps)  # Х за умовою
y = generate_f_i(x)  # У за умовою

x_r = [random.uniform(1, 2) for i in range(len(x))]
x_r.sort(reverse=True)

y_r = generate_f_i(x_r)  # нове У

# lagrange1 = list(map(lambda xi: lagrange(x, y, xi), x))


all_l1 = list(map(lambda xi: lagrange(x, y, xi), x))  # Лагранж по початкових даних
all_l2 = list(map(lambda xi: lagrange(x_r, y_r, xi), x_r))  # Лагранж на тестових даних


print(f"X (за умовою) = {x}")
print(f"Y (за умовою) = {y}")

print(f"X (довільні з проміжку [1, 2]) = {x_r}")
print(f"Y (довільні з проміжку [1, 2]) = {y_r}")

print(f"Лагранж для даних за умовою = {all_l1}")
print(f"Лагранж для довільних даних з проміжку [1, 2] = {all_l2}")


l = lagrange(x, y, xp)
e = max(list(map(lambda yi, li: abs(yi - li), y, all_l2)))
print(f"Всі похибки = {list(map(lambda yi, li: abs(yi - li), y, all_l2))}")
#print(f"Максимальна похибка = {e}")
print(f"Значення в точці {xp} = {l}")

plt.plot(x, y)  # blue
plt.plot(x, all_l2)  # orange
# plt.plot(x, all_l1)  # orange
plt.show()
