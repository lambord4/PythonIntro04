# part III - map, filter, zip

## map
Функция `map(func, *iterables)` - позволяет применить функцию `func` ко всем элементам последовательности `iterables`.
Функция `map` возвращает итератор.

```python
def fahrenheit(temperature):
    return round(((float(9)/5)*temperature + 32), 2)


def celsius(temperature):
    return round((float(5)/9)*(temperature-32), 2)


temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)

temperatures_in_fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_celsius = list(map(celsius, temperatures_in_fahrenheit))
print(temperatures_in_fahrenheit)               # [97.7, 98.6, 99.5, 100.4, 102.2]
print(temperatures_in_celsius)                  # [36.5, 37.0, 37.5, 38.0, 39.0]
```

Тот же результат можно получить используя анонимные функции

```python
C = [39.2, 36.5, 37.3, 38, 37.8]

F = list(map(lambda x: round((float(9)/5)*x + 32, 2), C))
print(F)                                        # [102.56, 97.7, 99.14, 100.4, 100.04]

C = list(map(lambda x: round((float(5)/9)*(x-32), 2), F))
print(C)                                        # [39.2, 36.5, 37.3, 38.0, 37.8]
```

Функцию `map()` можно применять сразу к нескольким спискам. Главное условие, списки должны быть одной длины

```python
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y : x+y, a, b)))                   # [18, 14, 14, 14]

print(list(map(lambda x, y, z : x+y+z, a, b, c)))           # [17, 10, 19, 23]

print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))) # [37.5, 33.0, 24.5, 21.0]
```

Если один из списков исеет меньшую длину чем другие, то функция `map()` завершит свою работу когда будет использован
самый короткий список

```python
a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))) # [37.5, 33.0, 24.5]
```

Видео по теме [map](https://www.youtube.com/watch?v=CDgOn4i6sSw)

## filter

Функция `filter(func, iterable)` - применяет функцию `func` ко всем элементам последовательности `iterable` и возвращает
для каждого элемента `True` или `False`. В результат работы функции `filter()` будут включены только те елементы 
последовательности, для который `func` вернула `True`.

```python
from random import randint

lst = [randint(0, 100) for _ in range(20)]
print(lst)                                      # [8, 44, 25, 64, 15, 55, 14, 10, 56, 7, 87, 89, 44, 69, 18]

odd_numbers = list(filter(lambda x: x % 2, lst))
print(odd_numbers)                              # [25, 15, 55, 7, 87, 89, 69]

even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)                             # [8, 44, 64, 14, 10, 56, 44, 18]

# alternatively
even_numbers = list(filter(lambda x: x % 2-1, lst))
print(even_numbers)                             # [8, 44, 64, 14, 10, 56, 44, 18]
```

Видео по теме [filter](https://www.youtube.com/watch?v=H4AlLQnEXDY)

## zip



```python
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

dict_res = dict(zip(name_hero, name_real))
list_res = list(zip(name_hero, name_real))
print(dict_res)
print(list_res)

rev_dict_res = list(zip(*dict_res))
print(rev_dict_res)

rev_list_res = list(zip(*list_res))
print(rev_list_res)

a, b = ([', '.join(x)] for x in rev_list_res)

print(a, b)
```

[Функция zip для прохода по нескольким итерируемым объектам](https://otus.ru/nest/post/819/?utm_source=email&utm_medium=email&utm_campaign=webdev&utm_term=sale_17.7)