from math import e, log

a = 2
b = 3
exact_value = (1/3 * log((e ** (3 * b)) / (1 + e ** (3 * b)))) - (1/3 * log((e ** (3 * a)) / (1 + e ** (3 * a))))


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    print("n = ", n)
    return s * h / 3

def f(x):
    return 1 / (1 + e ** (3 * x))

def calc(a1, a2, n, acc):
    while abs(a1 - a2) > acc:
        n *= 2
        a1 = simpson(f, 2, 3, n)
        n *= 2
        a2 = simpson(f, 2, 3, n)
    return a2


n = 2
a1 = simpson(f, 2, 3, n)
n *= 2
a2 = simpson(f, 2, 3, n)

accuracy = float(input("Точність = "))

res = calc(a1, a2, n, accuracy)

print(f"I = {res}")
print(f"Первісна = {exact_value}")