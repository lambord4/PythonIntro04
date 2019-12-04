## FOR
![for](img/for.jpg)

### syntax
```
for <var> in <iterable>:
    <statement(s)>
    
OR

for i in <collection>
    <loop body>
```

- прследовательный вывод цветов радуги
```python
i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep = '')
    i += 1
```
вывод:
```
#1 color of rainbow is red
#2 color of rainbow is orange
#3 color of rainbow is yellow
#4 color of rainbow is green
#5 color of rainbow is cyan
#6 color of rainbow is blue
#7 color of rainbow is violet
```

- В списке значений могут быть выражения различных типов
```python
for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)
```
вывод:
```
1
2
3
one
two
three
```

### range()
```
range(start, stop, step)

OR

range(stop)
```

! Stop value not include in range.
For example: 
```python
range(1, 10, 2)     # 1, 3, 5, 7, 9

range(10)           # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

- using `range()` with loop of `for`'
```python
for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
    # здесь можно выполнять циклические действия
    print(i)
    print(i ** 2)
# цикл закончился, поскольку закончился блок с отступом
print('Конец цикла')
```

- summa of values from 1 to `n`
```python
sum = 0
n = 5
for i in range(1, n + 1):
    sum += i
print(sum)
```

