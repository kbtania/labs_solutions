from math import e, log


a = 2
b = 3

exact_value = (1/3 * log((e ** (3 * b)) / (1 + e ** (3 * b)))) - (1/3 * log((e ** (3 * a)) / (1 + e ** (3 * a))))


def f(x):
    return 1 / (1 + e ** (3 * x))


def calc(f, a, b, n):
    h = (b-a)/float(n)
   # print("\nПоточна кількість розбиттів: ", n)
    result = 0
    for i in range(n):
        result += f(a + h * (i+0.5))
    result *= h
    print("n = ", n)
    #print("Поточний результат ", result)
    return result


def middle(a1, a2, n, acc):
    while abs(a1 - a2) > acc:
        n *= 2
        a1 = calc(f, 2, 3, n)
        n *= 2
        a2 = calc(f, 2, 3, n)

    return a2


accuracy = float(input("Введіть точність: "))

n = 2
a1 = calc(f, 2, 3, n)
n *= 2
a2 = calc(f, 2, 3, n)

res = middle(a1, a2, n, accuracy)


print(f"I = {res}")
print(f"Первісна = {exact_value}")