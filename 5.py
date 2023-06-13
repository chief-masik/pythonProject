import math


def main(x):
    sum = 0
    n = len(x)
    for i in range(1, n + 1):
        sum += 63 * (x[math.ceil(i / 2) - 1] ** 3 -
                     x[n - i] ** 2 - 67 * x[n - i]) ** 4
    return sum


f = [-0.77, 0.62, 0.31, -0.18, 0.38]
print(main(f))
