from math import e


def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    result = 0
    print("Текущий шаг:", h)
    for i in range(n):
        result += f(a + h * (i+0.5))
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


f = lambda x: 1/(1 + e**(3*x))

print("Используем формулу левых прямоугольников")
print("Интегрируемая функция: f(x) = sin(x)")
print("Точность: 0.001")

n = 2
a1 = work(f, 2, 3, n)
n *= 2
a2 = work(f, 2, 3, n)

res = left_rec(a1, a2, n)

print("\nОтвет MIDDLE:", res, "\nКоличество разбиений:", n)

# Ответ LEFT: 0.0011140255944274023
# Ответ MIDDLE: 0.0007660802077907916
# Ответ Right: 0.0005267184492652666