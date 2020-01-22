from random import randint

size = 10

matrix = [[randint(1, 50) for _ in range(size)] for _ in range(size)]


def show(lst):
    tmp = [0] * size
    for i in range(size):
        for j in range(size):
            print('{:>4}'.format(lst[i][j]), end='')
            tmp[j] += lst[i][j]
        print()

    for i in range(size):
        print('{:>4}'.format(tmp[i]), end='')

    print()
    print()
    print()


def sort_matrix(lst):
    tmp = [0] * size
    for i in range(size):
        for j in range(size):
            tmp[j] += lst[i][j]

    for _ in range(size):
        for j in range(size-1):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
                for i in range(size):
                    lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]

    for column in range(size):
        for _ in range(size):
            for i in range(size-1):
                if lst[i][column] > lst[i+1][column] if column % 2 else lst[i][column] < lst[i+1][column]:
                    lst[i][column], lst[i + 1][column] = lst[i + 1][column], lst[i][column]


show(matrix)
sort_matrix(matrix)
show(matrix)
