def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        w = fib(n - 1) + fib(n - 2)
        return w


print(fib(8))

# 0 1 1 2 3 5 8 13 21
