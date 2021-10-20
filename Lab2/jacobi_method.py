import numpy as np

epsilon = float(input("Точність: "))
A = np.array([
    [5., -1., 1.],
    [1., 6., 1.],
    [1., 1., -8.]])
f = np.array([2., 12., 11.])
res = np.array([1., 2., -1.])  # точний розв'язок


def jacobi(a, b, eps):
    x_i = np.zeros((len(a[0])))  # x_0 (розв'язок на 0 ітерації)
    d = np.diag(a)
    zero_diagonal = a - np.diagflat(d)  # початкова матриця з 0 на діагоналі
    iteration_count = 0
    while True:
        x_i = (b - np.dot(zero_diagonal, x_i)) / d  # розв'язок на i-й ітерації
        iteration_count += 1
        print(f"x_{iteration_count}: ", x_i)
        if np.linalg.norm(np.subtract(res, x_i), np.inf) < eps:
            break
    return x_i


print(f"X = {jacobi(A, f, epsilon)}")
