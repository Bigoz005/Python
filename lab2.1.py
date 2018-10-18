def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))


def silnia2(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x


print(silnia2(5))
