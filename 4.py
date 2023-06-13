import math


def main(n):
    if n == 0:
        return 0.03
    else:
        return 7 * math.tan(main(n - 1)) ** 2 - main(n - 1) -\
               38 * main(n - 1) ** 3


print(main(4))
