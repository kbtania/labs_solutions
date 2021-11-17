from math import e

def f(x):
    return 1/(1 + e**(3*x))

def work(f, a, b, n):
    # print("\nТекущее число разбиений: ", n)
    # h = (b-a)/float(n)
    # print("Текущий шаг:", h)
    # total = sum([f((a + (k*h))) for k in range(0, n)])
    # result = h * total
    # print("Текущий результат: ", result)
    # return result
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    result = 0
    print("Текущий шаг:", h)
    for i in range(n):
        result += f(a + h * (i))
    result *= h
    print("Текущий результат: ", result)
    return result

def left(a1, a2, n):
    while abs(a1 - a2) > 0.01:
        n *= 2
        a1 = work(f, 2, 3, n)
        n *= 2
        a2 = work(f, 2, 3, n)
    return a2



print("Используем формулу левых прямоугольников")
print("Интегрируемая функция: f(x) = sin(x) ")
print("Точность: 0.001")

n = 2
a1 = work(f, 2, 3, n)
n *= 2
a2 = work(f, 2, 3, n)

res = left(a1, a2, n)

print("\nОтвет LEFT:", res, "\nКоличество разбиений:", n)