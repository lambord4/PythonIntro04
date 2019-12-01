## WHILE
![while](img/while.jpg)

### syntax WHILE
```
while <condition>:
    блок инструкций
```

- программа печатает на экран квадраты всех целых чисел от 1 до 10.
```python
# 
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
```

- определение количества цифр натурального числа `n`
```python
n = int(input())
length = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    length += 1
print(length)
```

### operator BREAK
Применяется для прерывания работы цикла **полностью**.
```python
a = b = 1
while a != 0 and b != 0:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        print('Делить на 0 нельзя:', a)
        break
    print(a / b)
```

- не лучший вариант использования BREAK (данный код считает количество знаков в числе)
```python
n = int(input('Введите целое многозначное число: '))
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Длина числа равна', length)
```

- так правильнее
```python
n = int(input('Введите целое многозначное число: '))
length = 0
while n != 0:
    length += 1
    n //= 10
print('Длина числа равна', length)
```

- или так :-)
```python
n = int(input('Введите целое многозначное число: '))
print('Длина числа равна', len(str(n)))
```

### operator CONTINUE
Применяется для прерывания **только текущей** итерации.
```python
a = b = 1
while a != 0:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        print('Делить на 0 нельзя:', a)
        continue
    print(a / b)
```

### syntax WHILE-ELSE
```
while <condition>:
    блок инструкций
else:
    блок инструкций
```

- вывод значений от 1 до 10 включительно
```python
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Цикл окончен, i =', i)
```

- программа, считывает числа до тех пор, пока не встретит отрицательное число
```python
a = int(input())
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input())
else:
    print('Ни одного отрицательного числа не встретилось')
```