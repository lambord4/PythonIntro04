def iteratively_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res


print(iteratively_pow(2, 5))


def recursive_pow(num, exp):
    # base case
    if exp == 0:
        return 1

    # recursive case
    return num * recursive_pow(num, exp - 1)


print(recursive_pow(2, 5))


def fibonacci_recursive(n):
    return n if 0 <= n <= 1 else fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


'''
        x1  x2  y
    x1  x2  y
    0   1   1   2
'''


def fibonacci_it(num):
    x1 = 0
    x2 = 1
    while num > 0:
        y = x1 + x2
        x1 = x2
        x2 = y
        num -= 1

    return x1


print(fibonacci_recursive(10))
print(fibonacci_it(10))
