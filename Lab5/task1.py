import math
import numpy as np
import matplotlib.pyplot as plt

ALPHA = 1
BETA = 2
N = 10
# M = [1, 2, 3, 4, 5]
polynom_power = 5

X = [x * 0.1 for x in range(10, 20)]
Y = list(map(lambda x: x * math.log(x, math.e) - x, X))


def create_table_X(x_arr, power):
    table_x = []
    for i in range(2*power + 1):
        x_column = [x ** i for x in x_arr]
        table_x.append(x_column)
    return table_x

def create_table_Y(x_arr, y_arr, power):
    table_y = []
    for i in range(power+1):
        y_column = list(map(lambda x, y: x**power * y, x_arr[i], y_arr))
        table_y.append(y_column)
    return table_y

# c, d - коефіцієнти
def get_coefficients(arr):
    coef = []
    for col in arr:
        coef.append(sum(col))
    return coef

x_table = create_table_X(X, polynom_power)
y_table = create_table_Y(x_table, Y, polynom_power)

x_coef = get_coefficients(x_table)
y_coef = get_coefficients(y_table)

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


left_coeff = create_matrix(x_coef)  # коефіцієнти С
right_coeff = y_coef  # коефіцієнти d

c = np.array(left_coeff)
d = np.array(right_coeff)

a = np.linalg.solve(c, d)  # розвязок системи
print(f'[ m = {polynom_power} ] Розвязок системи: {a}')

p = np.poly1d(np.flip(a))
print(f'[ m = {polynom_power} ] Поліном: {p}')
P = list(map(lambda x: p(x), X))  # значення поліному в точках Х

# ---------- Похибки ----------
errors = list(map(lambda y, p: y - p, Y, P))
average_error = math.sqrt(sum(list(map(lambda x: x ** 2, errors))) / N + 1)
print(f'[ m = {polynom_power} ] Похибки: {errors}')
print(f'[ m = {polynom_power} ] Похибка середньоквадратичного наближення: {average_error}')

# ---------- Graphics ---------
plt.plot(X, Y, linestyle="", marker="o")  # початкова функція (точки)

plt.plot(X, P)  # поліном

plt.show()





