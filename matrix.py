import numpy as np
from copy import deepcopy


def swap(m, n, i):
    max_el = -1e100
    for r in range(i, n):
        if max_el < abs(m[r][i]):
            max_row = r
            max_el = abs(m[r][i])
    m[i], m[max_row] = m[max_row], m[i]


def remove_last(m):
    if len(m[0]) - len(m) != 1:
        raise SystemExit('Перевірте розмір матриці.')
    square_matrix = np.delete(m, -1, axis=1)
    return square_matrix


def solve_equation(m):
    # forward elimination
    n = len(m)
    if np.linalg.det(remove_last(m)) == 0:
        raise SystemExit('Система є лінійно залежною.')
    else:
        for i in range(n):
            swap(m, n, i)
            for j in range(i + 1, n):
                m[j] = [m[j][k] - m[i][k] * m[j][i] / m[i][i] for k in range(n + 1)]
    # backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = round((m[i][n] - s) / m[i][i])
    return x


def small_matrix(original_matrix, row, column):  # алгебраїчне доповнення
    new_matrix = deepcopy(original_matrix)
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].pop(column)
    return new_matrix


def determinant(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise SystemExit('Матриця повинна бути квадратна.')
        if len(matrix) == 2:
            simple_determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return simple_determinant
        else:
            # Minors extraction
            answer = 0
            num_columns = num_rows
            for j in range(num_columns):
                minor = (-1) ** (0 + j) * matrix[0][j] * determinant(small_matrix(matrix, 0, j))
                answer += minor
            return answer


def inverse_matrix(x):
    if len(x) == len(x[0]):
        if np.linalg.det(x) != 0:
            A_copy = deepcopy(x)
            I = np.identity(len(x))
            I_copy = deepcopy(I)

            indices = list(range(len(x)))

            for fd in range(len(x)):
                fdScaler = 1.0 / A_copy[fd][fd]
                for j in range(len(x)):
                    A_copy[fd][j] *= fdScaler
                    I_copy[fd][j] *= fdScaler
                for i in indices[0:fd] + indices[fd + 1:]:
                    crScaler = A_copy[i][fd]
                    for j in range(len(x)):
                        A_copy[i][j] = A_copy[i][j] - crScaler * A_copy[fd][j]
                        I_copy[i][j] = I_copy[i][j] - crScaler * I_copy[fd][j]
            return I_copy
        else:
            raise SystemExit('Детермінант = 0. Неможливо знайти обернену матрицю.')
    else:
        raise SystemExit('Матриця повинна бути квадратна.')


def generate_matrix(n):
    A = [[round(1 / (i + j - 1), 3) for j in range(1, n+1)] for i in range(1, n+1)]
    X = [i ** 2 for i in range(1, n+1)]
    return A, X


def condition_number(A):
    norm_A = np.linalg.norm(A)
    norm_inversed_A = np.linalg.norm(inverse_matrix(A))
    return norm_A * norm_inversed_A

def display_matrix(m):
    for row in m:
        print(row)


a = [
    [5, 8, -1, 16],
    [1, 2, 3, 10],
    [2, -3, 2, 5],
]
b = [
    [1, 3, 4],
    [1, 5, 4],
    [1, 2, 3]
]
print("[Завдання 1] Розв'язок системи рівнянь: ", solve_equation(a), "\n")

print("[Завдання 2.1] Детермінант: ", determinant(b), "\n")

print("[Завдання 2.2] Обернена матриця: ")
display_matrix(inverse_matrix(b))
print("\n")

gen = generate_matrix(3)
print("[Завдання 3.1]")
print("А = ")
display_matrix(gen[0])

print("f = ", gen[1])
print("\n")

print("cond(A): ", condition_number(gen[0]), "\n")

print("Ax=f; x = ", np.linalg.solve(gen[0], gen[1]))

