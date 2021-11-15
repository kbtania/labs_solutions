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
h = (beta - alpha) / n
x = [round((alpha + i * h), 2) for i in range(n)]
y = [[0 for i in range(n)] for j in range(n)]

# заповнюємо значення f_i
for i in range(n):
    y[i][0] = round(x[i] * math.log(x[i], math.e) - x[i], 2)
xp = 1.5

print(f"X = {x}")
print(f"Y = {column(y, 0)}")

# Calculating the backward difference table
for i in range(1, n):
    j = n - 1
    while j >= i:
        y[j][i] = y[j][i-1] - y[j-1][i-1]
        j -= 1

for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print("")

xp = float(input("Значення в точці: "))
sum = newton_poly(x, y, xp)
all_n = list(map(lambda xi: newton_poly(x, y, xi), x))
e = max(list(map(lambda yi, ni: abs(yi - ni), column(y, 0), all_n)))
print(f"N({xp}) = {sum}")

print(f"All N(xi) = {all_n}")
print(f"e = {e}")

# plt.plot(x, column(y, 0))  # blue
# plt.plot(x, all_n)  # orange
# plt.show()
