import math


def main(z):
    if (z < 99):
        return math.log10(z ** 3) ** 4
    elif (z >= 99 and z < 188):
        return (z ** 2 - 80) ** 4
    elif (z >= 188 and z < 209):
        return 1 + 23 * math.tan(z) ** 5
    else:
        return 50 * (10 * z ** 3 + 51) ** 5


result = main(190)
print("Результат:", result)