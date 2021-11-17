import numpy as np
import random
import math
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')


def generate_f_i(X):
    x_i = X
    f_i = list(map(lambda x: x * math.log(x) - x, x_i))
    #f_i = list(map(lambda x: math.sqrt(math.sin(x)) + x ** 5 / math.cos(x), x_i))
    # f_i = list(map(lambda x: math.sqrt(math.sin(x)) + x**5/math.cos(x)), x_i)
    return f_i


def divided_difference(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])
        #print(f"{a[k:m]}")
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
m = 100
x_calc = float(input("Обчислити значення в точці: "))

# randomly generated X in range(1, 2)
X = [random.uniform(alpha, beta) for i in range(n+1)]
X.sort()
Y = generate_f_i(X)

X_m = [random.uniform(alpha, beta) for i in range(len(X))]
X_m.sort()
Y_m = generate_f_i(X_m)

all_n1 = list(map(lambda xi: newton_polynomial(X, Y, xi), X))
all_n2 = list(map(lambda xi: newton_polynomial(X_m, Y_m, xi), X_m))
print(f"X = {X}")
print(f"Y = {Y}")
print(f"X_m = {X_m}")
print(f"Y_m = {Y_m}")
print(f"N1 = {all_n1}")
print(f"N2 = {all_n2}")
print(f"N({x_calc}) = ", newton_polynomial(X, Y, x_calc))

e = max(list(map(lambda yi, li: abs(yi - li), Y, all_n2)))
print(f"Всі похибки = {list(map(lambda yi, li: abs(yi - li), Y, all_n2))}")
#print(f"e = {e}")
plt.plot(X, Y)  # blue
plt.plot(X, all_n2)  # orange
plt.show()


