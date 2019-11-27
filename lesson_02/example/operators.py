
# унарный минус и плюс
print(5)
print(-5)
print(+5)
print('-' * 100)

# +
print('Test' + ' ' + 'Test')
print('Test' + ' Test')
print('Test ' + str(4))
print('-' * 100)

# *
print(5 * 7)
print('-' * 100)

# **
print(3 ** 3 ** 2)      # 729
print('-' * 100)

# /
print(9 / 2)
print(3.4 / 6)
print('-' * 100)

# //
print(9 // 2)
print(10.0 // 3)
print('-' * 100)

# %
print(10 % 3)
print(3 % 10)
print(1234 % 10)
print(1234 % 100)
print(1234 % 1000)
print('-' * 100)

print(5 > 3)
print(True == False)
print(6 != 9)
print(6 >= 5)
print('-' * 100)

a = 1
b = 1


def f1(x):
    print('F1')
    return x


def f2(y):
    print('F2')
    return y


print('and')
(f1(a) and f2(b))

print('or')
(f1(a) or f2(b))

