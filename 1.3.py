#1.3
def func(n, m):
    summ = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            summ += (i ** 4 + i ** 6 + 90)
    for i in range(1, n+1):
        summ += i ** 4 - 20 * i ** 5
    return summ


if __name__ == "__main__":
    print("{:.2e}".format(func(99, 73)))
    print("{:.2e}".format(func(72, 38)))
