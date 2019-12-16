# def print_some_text():
#     print('Hello World!')
#
#
# print_some_text()
#
#
# def get_2_x_2():  # объявление функции
#     print(2 * 2)
#
#
# get_2_x_2()  # 4 (вызов функции)
# print(get_2_x_2())  # 4
#
#
# # None
# def get_2_x_2():
#     return 2 * 2
#
#
# print(get_2_x_2())


# def draw_rect(size=5):
#     for _ in range(size):
#         for _ in range(size):
#             print('*  ', end='')
#         print()
#     print()
#
#
# draw_rect(8)
# draw_rect()
#
# rows = 10
#
#
# def draw(cols, t=5, y=9):
#     global rows
#     for i in range(rows):
#         for j in range(cols):
#             if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
#                 print('*  ', end='')
#             else:
#                 print('   ', end='')
#         print()
#     print()
#
#
# print(rows)
# # draw(3)
# draw(3, 6)
# draw(3, 6, 8)
# draw(3, 6, 7, 6)


# def func(a, b, c, d=1, e=2, f=3):
#     print('a = {A}\tb = {B}\tc = {C}\td = {D}\te = {E}\tf = {F}\n'.format(
#         A=a, B=b, C=c, D=d, E=e, F=f
#     ))
#
#
# func(4, 5, 6)
# func(4, 5, 6, 7)
# func(4, 5, 6, 7, 8)
# func(4, 5, 6, 7, 8, 9)

# func(c=5, a=9, b=0, f=5, d=8)

def func_1(*args):
    print(type(args))
    print(args)


# func_1(3, 6, 'g', True)


def my_print(*args, sep=' ', end='\n'):
    for element in args:
        print(element, sep='', end='')
        print(sep, sep='', end='')
    print(end, sep='', end='')


my_print(3, 6.7, 'g', True, sep=', ')

d = {'m': 5, 'y': 3, 'd': 9}


def func_2(**kwargs):
    print(type(kwargs))
    print(kwargs)


func_2(m=5, y=3, d=9)
func_2(**d)


def func_3(**kwargs):
    if 'a' in kwargs:
        print('param A')

    if 'n' in kwargs:
        print('param M')

    if 'test' in kwargs:
        print('TEST')


func_3(a=8, test='test', f=8)


def my_pow(a, b=2):
    # print(a ** b)
    return a**b


x = my_pow(2, 5)
print(x)
print(my_pow(3))


def test_return(a, b, c):
    return a, b, c


t = test_return(3, 6, 4)
print('type =', type(t), 'value =', t)

x, y, z = test_return(1, 4, 7)
print(x, y, z)

a, b, c = 1, 2, 3
