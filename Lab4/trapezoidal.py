from math import e, log

a = 2
b = 3
exact_value = (1/3 * log((e ** (3 * b)) / (1 + e ** (3 * b)))) - (1/3 * log((e ** (3 * a)) / (1 + e ** (3 * a))))


def f(x):
    return 1 / (1 + e ** (3 * x))


def trapezoidal(f, x0, xn, n):
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    integration = integration * h / 2
    print("n = ", n)
    return integration

def calc(a1, a2, n, acc):
    while abs(a1 - a2) > acc:
        n *= 2
        a1 = trapezoidal(f, 2, 3, n)
        n *= 2
        a2 = trapezoidal(f, 2, 3, n)
    return a2


n = 2
a1 = trapezoidal(f, 2, 3, n)
n *= 2
a2 = trapezoidal(f, 2, 3, n)

accuracy = float(input("Точність = "))

res = calc(a1, a2, n, accuracy)


print(f"I = {res}")
print(f"Первісна = {exact_value}")