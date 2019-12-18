height = int(input('Введите высоту треугольника: '))

i = 0
while i < height:
    j = 0
    while j < height * 2 - 1:
        if height - 1 - i == j or j == height - 1 + i or i == height - 1:
         # height - 1 - i <= j <= height - 1 + i or i == height - 1:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()
