import math


def main(x):
    a = x ** 4
    b = 25 * (x + 15 * x ** 3 + 29 * x ** 2) ** 3
    c = math.log10(x) ** 4
    return a - math.sqrt(b - c)


result = main(0.96)
print("Результат:", result)
