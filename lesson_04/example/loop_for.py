i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='')
    i += 1


for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
    # здесь можно выполнять циклические действия
    print(i, end=' ')
    print(i ** 2)
# цикл закончился, поскольку закончился блок с отступом
print('Конец цикла')

