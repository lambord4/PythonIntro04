```python
from pprint import pprint as pp

lst = [
    'Максимальное напряжение, B              250',
    'Максимальный ток, А                     6',
    'Тип рабочего тока                       переменный',
    'Высота педали, мм                       43.5',
    'Толщина педали, мм                      18',
    'Количество контактов (без реверса)      6'
]

pp(lst)

file = open('example_file.txt', 'w')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()
print()

# read all
print()
lst = []
with open('example_file.txt') as file:
    lst = file.read()
    
pp(lst)
print()

# read all
print()
lst = []
with open('example_file.txt') as file:
    lst = file.readlines()
    
pp(list(map(lambda x: x.strip('\n'), lst)))
print()

# read by 40 symbols
lst = []
pp(lst)
with open('example_file.txt') as file:
    while True:
        line = file.readline(40)
        if line != '':
            lst.append(line.strip('\n'))
        else:
            break
            
print()
pp(lst)

# read by line
lst = []
pp(lst)
with open('example_file.txt') as file:
    for line in file.readlines():
        lst.append(line.strip('\n'))

print()
pp(lst)

# read by line
lst = []
pp(lst)
with open('example_file.txt') as file:
    for line in file:
        lst.append(line.strip('\n'))

print()
pp(lst)
```



```python
size_buff = 32

with open('dog_2.jpg', 'rb') as src, open('dog_3.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break
```