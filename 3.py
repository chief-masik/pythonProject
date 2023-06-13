import math


def main(n, a, m):
    x = 0
    for j in range(1, m + 1):
        for k in range(1, a + 1):
            for i in range(1, n + 1):
                x += i ** 15 / 66 + j ** 7 + 92 * j ** 3 + k + 74 * j ** 2
    return x


result = main(2, 6, 4)
print(result)
