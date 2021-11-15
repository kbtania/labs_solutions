import numpy as np
import random
import math
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')


def generate_f_i(X):
    x_i = X
    f_i = list(map(lambda x: x* math.log(x) -x, x_i))
    #f_i = list(map(lambda x: math.sqrt(math.sin(x)) + x ** 5 / math.cos(x), x_i))
    # f_i = list(map(lambda x: math.sqrt(math.sin(x)) + x**5/math.cos(x)), x_i)
    return f_i


def divided_difference(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])
        print(f"{a[k:m]}")
    return a


def newton_polynomial(x_data, y_data, x):
    a = divided_difference(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p
    return p


n = 10
alpha = 1
beta = 2
x_calc = float(input("Обчислити значення в точці: "))

# randomly generated X in range(1, 2)
# X = [round(random.uniform(alpha, beta), 2) for i in range(n+1)]
# X.sort()
# Y = generate_f_i(X)

# testing example
X = [1.67, 1.11, 1.21, 1.26, 1.61, 1.49, 1.81, 1.47, 1.16, 1.29, 1.7]
X.sort()
Y = generate_f_i(X)

# X  =  [1.01, 1.06, 1.13, 1.16]
# Y = [-1.0, -1.0, -0.99, -0.99]
all_n = list(map(lambda xi: newton_polynomial(X, Y, xi), X))
e = max(list(map(lambda yi, ni: abs(yi - ni), Y, all_n)))

print(f"All N = {all_n}")
print(f"X = {X}")
print(f"Y = {Y}")
print("Таблиця розділених різниць: ")
print(f"N({x_calc}) = ", newton_polynomial(X, Y, x_calc))
# print(list(map(lambda yi, ni: abs(yi - ni), Y, all_n)))
print(f"e = {e}")

plt.plot(X, Y)  # blue
plt.plot(X, all_n)  # orange
plt.show()


