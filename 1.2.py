import math
#1.2

def func(x):
    if x < 29:
        return x ** 2 - 28 * x ** 3
    elif x < 56:
        return x ** 4 - 20 * x ** 5
    elif x < 122:
        return x ** 8 + (x ** 4) / 81 + 88
    elif x >= 122:
        return math.tan(x ** 4) - math.tan(x)


if __name__ == "__main__":
    print("{:.2e}".format(func(6)))
    print("{:.2e}".format(func(76)))
