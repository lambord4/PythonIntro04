
current_x = int(input('Текущая позиция по горизонтали: '))
current_y = int(input('Текущая позиция по вертикали: '))

new_x = int(input('Новая позиция по горизонтали: '))
new_y = int(input('Новая позиция по вертикали: '))

dx = abs(current_x - new_x)
dy = abs(current_y - new_y)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print('Yes')
else:
    print('No')
