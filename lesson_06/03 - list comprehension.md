# List comprehension

Специальное выражение позволяющее генерировать списки. При это возможно указывание некоторых условий которые будут 
применяться к каждому значению, исходного списка, прежеде чем тот попадёт в новый список.


```
new_list = [ expression for item in list ]
```

или

```
new_list = [ expression for item in list if conditional ]
```

- создаём список случайных значений в диапазоне от 1 до 10
```python
from random import randint

lst = [randint(1, 10) for _ in range(15)]
print(lst)                                      # [9, 5, 3, 8, 9, 6, 7, 7, 1, 3, 1, 4, 1, 7, 4]

# из полученого, выше, списка формируем новый состоящий только из чётных значений исходного списка
lst = [x for x in lst if x % 2 == 0]
print(lst)                                      # [8, 6, 4, 4]
```

- формируем список возрастающих, не чётных значений в диапазоне от 1 до 25
```python
lst = [x for x in range(1, 25, 2)]
print(lst)                                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
```

- формируем список квадратов возрастающих нечётных значений в диапазоне от 1 до 25
```python
lst = [x**2 for x in range(1, 25, 2)]
print(lst)                                      # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529]
```

- тоже что и в предыдущем слуае, но в новый список попадут только квадраты кратные 3-м
```python
lst = [x**2 for x in range(1, 25, 2) if x % 3 != 0]
print(lst)                                      # [1, 25, 49, 121, 169, 289, 361, 529]
```

- перевод символов строки на верхний регистр (такое можно сделать просто применив к строке метод `upper()`)
```python
s = 'lower case string'
s = ''.join([ch.upper() for ch in s])
print(s)                                        # 'LOWER CASE STRING'
```

- а такое, строковыми методами, сделать не получится. Изменяем регистр символов стоящих на чётных позициях в строке
```python
s = 'lower case string'
s = ''.join([ch.upper() if idx % 2 == 0 else ch for idx, ch in enumerate(s)])
print(s)                                        # 'LoWeR CaSe sTrInG'
```

Если `list comprehension` применяется как параметр какой либо агрегируёщей функции: `sum()`, `min()`, `max()` или
`join(()`, `split()`, то квадратные скобки вокруг выражения можно опускать.

```python
s = 'lower case string'
s = ''.join(ch.upper() if idx % 2 == 0 else ch for idx, ch in enumerate(s))
print(s)                                        # LoWeR CaSe sTrInG
```
