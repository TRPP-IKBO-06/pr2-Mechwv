import math
# 1.1

def func(x, y):
    return math.sqrt(x ** 2 - 36 * x ** 3) + (x ** 4 - 20 * y ** 5) / (y ** 8 + (y ** 4) / 81 + 88) \
           + math.sqrt(7 * y ** 2 - y ** 5)


if __name__ == "__main__":
    print("{:.2e}".format(func(-20, -96)))
    print("{:.2e}".format(func(-25, -13)))
