from msvcrt import getch
from os import system

# cls
# clear

rows = 10
cols = 10

CODE = 224
UP = 72
DOWN = 80
LEFT = 75
RIGHT = 77
ENTER = 13
ESC = 27
SPACE = 32
SYMBOL = chr(606)


def show(lst):
    system('cls')
    for i in range(rows):
        for j in range(cols):
            print(lst[i][j], end='  ')
        print()


field = [['.'] * cols for _ in range(rows)]
x = 0
y = 0
field[y][x] = SYMBOL
show(field)

while True:
    ch = ord(getch())
    if ch == ESC:       # SPACE
        break
    elif ch == ENTER:
        print('x = {x}\ny = {y}'.format(x=x, y=y))
    elif ch == CODE:
        field[y][x] = '.'
        ch = ord(getch())
        if ch == UP:
            if y > 0:
                y -= 1
        elif ch == DOWN:
            if y < rows -1:
                y += 1
        elif ch == LEFT:
            if x > 0:
                x -= 1
        elif ch == RIGHT:
            if x < cols - 1:
                x += 1
        field[y][x] = SYMBOL
        show(field)

