import math
import matplotlib.pyplot as plt

steps = 10
a = 1
b = 2


def generate_x_i(alpha, beta, n):
    x_i = []
    for i in range(1, n):
        x_i.append(round(((beta + alpha) / 2) + ((beta - alpha)/2) * math.cos(math.pi * (2 * i + 1)/(2*(n + 1))), 2))
    return x_i


def generate_f_i():
    x_i = generate_x_i(a, b, steps)
    f_i = list(map(lambda x: round(x * math.log(x, math.e) - x, 2), x_i))
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
x = generate_x_i(a, b, steps)
y = generate_f_i()
all_l = list(map(lambda xi: lagrange(x, y, xi), x))
print(f"All L {all_l}")

print(f"X = {x}")
print(f"Y = {y}")

l = lagrange(x, y, xp)
e = max(list(map(lambda yi, li: abs(yi - li), y, all_l)))
print(f"e = {e}")
print(f"L_n = {l}")

plt.plot(x, y)  # blue
plt.plot(x, all_l)  # orange
plt.show()

