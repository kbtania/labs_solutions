import math
import matplotlib.pyplot as plt

def u_calc(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp

def product(n):
    p = 1
    for i in range(2, n):
        p *= i
    return p


def column(matrix, i):
    return [row[i] for row in matrix]

def newton_poly(x, y, xp):
    sum = y[n - 1][0]
    u = (xp - x[n - 1]) / (x[1] - x[0])
    for i in range(1, n):
        sum = sum + (u_calc(u, i) * y[n - 1][i]) / product(i)
    return sum
n = 10
alpha = 1
beta = 2
m = 10
h = (beta - alpha) / n
x = [(alpha + i * h) for i in range(n)]
y = [[0 for i in range(n)] for j in range(n)]

# заповнюємо значення f_i
for i in range(n):
    y[i][0] = x[i] * math.log(x[i], math.e) - x[i]
xp = 1.5

x_m = [(alpha + i * h) for i in range(m)]
y_m = [[0 for i in range(m)] for j in range(m)]

# заповнюємо значення f_i
for i in range(m):
    y_m[i][0] = x_m[i] * math.log(x_m[i], math.e) - x_m[i]

print(f"X = {x}")
print(f"Y = {column(y, 0)}")

print(f"X_m = {x_m}")
print(f"Y_m = {column(y_m, 0)}")
# Calculating the backward difference table for Y
for i in range(1, n):
    j = n - 1
    while j >= i:
        y[j][i] = y[j][i-1] - y[j-1][i-1]
        j -= 1

# Calculating the backward difference table for Y_m
for i in range(1, m):
    j = m - 1
    while j >= i:
        y_m[j][i] = y_m[j][i-1] - y_m[j-1][i-1]
        j -= 1

xp = float(input("Значення в точці: "))
sum = newton_poly(x, y, xp)
all_n1 = list(map(lambda xi: newton_poly(x, y, xi), x))
all_n2 = list(map(lambda xi: newton_poly(x_m, y_m, xi), x_m))

e = max(list(map(lambda yi, ni: abs(yi - ni), column(y, 0), all_n2)))
print(f"N({xp}) = {sum}")

print(f"All N(xi) = {all_n1}")
print(f"All N2 = {all_n2}")
print(f"Всі похибки = {list(map(lambda yi, li: abs(yi - li), column(y, 0), all_n2))}")
#print(f"e = {e}")

plt.plot(x, column(y, 0))  # blue
plt.plot(x, all_n2)  # orange
plt.show()
