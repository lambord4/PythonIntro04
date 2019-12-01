# x = 7
# y = 3
#
# print('X equals ' + str(x))
# print('X equals', x)
# print('X equals %d %d' % (x, 9))
#
# print('X equals {} {}'.format(x, 9))
# # f - string
# print(f'{x} - {y}')
# # RAW - string
# print(r'''irhig;erkf3f
#
#       gh45tjyt]p34r
# 345rlthj34iof''')

x = 5
y = 4.36434523
z = x / y

a = -6
b = 8

print('X equals %d %d %d %d' % (x, x, x, x))

print('X equals {x1} {x1} {x1}'.format(x1=x))
print('"{x1:<5}"'.format(x1=x))
print('"{x1:>5}"'.format(x1=x))
print('"{x1:^5}"'.format(x1=x))
print('-'*150)
print('"{x1:^-5}"'.format(x1=a))
print('"{x1:^-5}"'.format(x1=b))

print('"{x1:^+5}"'.format(x1=a))
print('"{x1:^+5}"'.format(x1=b))

print('"{x1:^ 5}"'.format(x1=a))
print('"{x1:^ 5}"'.format(x1=b))

print('"{x1:.>5}"'.format(x1=a))
print('"{x1:.>5}"'.format(x1=b))

print('"{x1:0=+5}"'.format(x1=a))
print('"{x1:0=+5}"'.format(x1=b))

print('"{x1:5.2f}"'.format(x1=y))
print('"{x1:5.1f}"'.format(x1=z))

print('{:d}'.format(63547))
print('{:b}'.format(63547))
print('{:o}'.format(63547))
print('{:X}'.format(63547))

print('{:#d}'.format(63547))
print('{:#b}'.format(63547))
print('{:#o}'.format(63547))
print('{:#x}'.format(63547))