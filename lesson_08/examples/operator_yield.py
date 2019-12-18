def count_down_1(num):
    result = []
    while num != 0:
        result.append(num - 1)
        num -= 1
    return result


print(count_down_1(5))


def count_down_2(num):
    while num != 0:
        yield num - 1
        num -= 1

it = count_down_2(5)
print(next(it))                                 # 4
print(next(it))                                 # 3
print(next(it))                                 # 2
print(next(it))                                 # 1
print(next(it))                                 # 0
# print(next(it))                               # ERROR

for value in count_down_2(5):
    if value < 3:
        break

    print(value)
