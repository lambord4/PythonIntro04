a = []
print(type(a))
b = list()
print(type(b))
c = list('Hello World')
print(type(c))
d = [1, 2, 3, 4, 5]
print(type(d))

print(d[3])
lst = [1, 'String', 'f', True, 3.14]
print(lst)

print(a)
a.append(56)
a.append(True)
print(a)

a = [1, 2, 3, 4]
b = [5, 6, 7]
c = a + b
print(c)

a = [1, 2, 3]
print(a * 3)

a = [6] * 10
print(a)

a = [1, 2, 3, 4]
print(len(a))

lst = [1, 'String', 'f', True, 3.14]
for i in range(len(lst)):
    print(lst[i], end=', ')
    # lst[i] = 0
print()
for el in lst:
    print(el, end=', ')
print()

s = 'Does numpy not like performing array functions on complex numbers'
print(s)
s = s.split()
print(s)

s = ' '.join(s)
print(s)

s = s.split()
print(s)
del s[1]
print(s)

s.clear()
print(s)

del s
# print(s)

a = [1, 2, 3, 4]
print(a)
a.reverse()
print(a)
