from math import e


def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    result = 0
    print("Текущий шаг:", h)
    for i in range(n):
        result += f(a + h * (i+1))
    result *= h
    print("Текущий результат: ", result)
    return result

def left_rec(a1, a2, n):
    while abs(a1 - a2) > 0.01:
        n *= 2
        a1 = work(f, 2, 3, n)
        n *= 2
        a2 = work(f, 2, 3, n)
    return a2

def f(x):
    return 1/(1 + e**(3*x))

print("Используем формулу левых прямоугольников")
print("Интегрируемая функция: f(x) = sin(x)")
print("Точность: 0.001")

n = 2
a1 = work(f, 2, 3, n)
n *= 2
a2 = work(f, 2, 3, n)

res = left_rec(a1, a2, n)

print("\nОтвет Right:", res, "\nКоличество разбиений:", n)