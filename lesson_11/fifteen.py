from msvcrt import getch
# from getch import getch
from os import system
from time import sleep

# cls
# clear

size = 4

CODE = 224
UP = 72
DOWN = 80
LEFT = 75
RIGHT = 77
SPACE = 32


def show(lst):
    system('cls')
    print('+----+----+----+----+')
    for i in range(size):
        for j in range(size):
            print('|{value:^4}'.format(value=lst[i][j] if lst[i][j] != 16 else ''), end='')
        print('|')
        print('+----+----+----+----+')


def go_up(lst, x, y):
    if y > 0:
        y -= 1
        lst[y][x], lst[y+1][x] = lst[y+1][x], lst[y][x]
    
    return x, y
        
        
def go_down(lst, x, y):
    if y < size-1:
        y += 1
        lst[y][x], lst[y - 1][x] = lst[y - 1][x], lst[y][x]

    return x, y
        

def go_left(lst, x, y):
    if x > 0:
        x -= 1
        lst[y][x], lst[y][x + 1] = lst[y][x + 1], lst[y][x]

    return x, y


def go_right(lst, x, y):
    if x < size-1:
        x += 1
        lst[y][x], lst[y][x - 1] = lst[y][x - 1], lst[y][x]
        
    return x, y


def step(lst, x, y):
    ch = ord(getch())
    if ch == CODE:
        ch = ord(getch())
        if ch == UP:
            return go_up(lst, x, y)
        elif ch == DOWN:
            return go_down(lst, x, y)
        elif ch == LEFT:
            return go_left(lst, x, y)
        elif ch == RIGHT:
            return go_right(lst, x, y)
    elif ch == SPACE:
        return None
    else:
        return x, y


def shake(lst, x, y):
    from random import randint
    for _ in range(1000):
        direct = randint(1, 4)
        if direct == 1:
            x, y = go_up(lst, x, y)
        elif direct == 2:
            x, y = go_down(lst, x, y)
        elif direct == 3:
            x, y = go_left(lst, x, y)
        elif direct == 4:
            x, y = go_right(lst, x, y)

    return x, y


def is_win(lst):
    x = 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if x == lst[i][j]:
                x += 1
            else:
                return False

    return True


field = [[j+1 + i*size for j in range(size)] for i in range(size)]
show(field)

emp_x = size - 1
emp_y = size - 1
sleep(5)
emp_x, emp_y = shake(field, emp_x, emp_y)
show(field)

while True:
    res = step(field, emp_x, emp_y)
    if res is None:
        break

    show(field)
    emp_x, emp_y = res

    if is_win(field):
        print('Game over!')
        break
