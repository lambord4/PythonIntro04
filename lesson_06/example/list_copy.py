import copy

a = 5
b = a
print(id(a))
print(id(b))

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = x
print(x)
print(y)
x[3] = 100
print(x)
print(y)
print(id(x))
print(id(y))

y = x.copy()
print(x)
print(y)
x[6] = 200
print(x)
print(y)
print(id(x))
print(id(y))
print('-' * 150)
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = a.copy()
print(id(a))
print(id(b))

s = a[0][0]

print(a)
print(b)

a[0][1] = 50
print(a)
print(b)

b = copy.deepcopy(a)
print(a)
print(b)
a[1][1] = 500
print(a)
print(b)
