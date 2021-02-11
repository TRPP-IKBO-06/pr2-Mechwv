import math


def func(n):
    if n == 0:
        return 8
    else:
        a = math.tan(func(n-1)) + math.cos(func(n-1))
        return a


if __name__ == "__main__":
    print("{:.2e}".format(func(15)))
    print("{:.2e}".format(func(3)))
