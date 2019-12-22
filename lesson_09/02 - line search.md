# Линейный поиск

**Линейный поиск** один из самых прстых алгоритмов, позволяет найти искомое значение в небольших наборах данных - 
колекциях: списках, кортежах и т.д.  
Суть алгоритма заключается в последовательном переборе всех элементов колекции и сравнении каждого элемента с икомым
значением - ключём. Как только будет обнаружено совпадение значения ключа с элементом колекции, поиск завершается.   
Линейный поиск может выполняться на не отсортрованном (не упорядоченый) наборе данных. Поиск начинается с первого 
элемента и продолжается до последнего элемента или до первого совпадения.

```python
from random import randint

def line_search(collection, key):
    for idx, value in enumerate(collection):
        if key == value:
            return idx
    else:
        return -1


lst = [randint(0, 9) for _ in range(15)]
print(lst)

key = 6
result = line_search(lst, key)

print(result)

# ---------------------------------------------
# [7, 3, 0, 5, 3, 7, 5, 5, 7, 2, 9, 2, 2, 5, 0]
# -1

# [1, 9, 9, 1, 4, 0, 2, 8, 9, 3, 5, 7, 6, 5, 5]
# 12
```

Код в примере выполняет поиск значения ключа в списке и если таковой находится, то мы получаем его индекс, иначе, -1

Можно использовать линейный поиск для нахождения минимального или максимального значения в списке

```python
from random import randint

def search_min_max(collection):
    minimum = collection[0]
    maximum = collection[0]
    for value in collection:
        if minimum > value:
            minimum = value
        elif maximum < value:
            maximum = value

    return minimum, maximum


lst = [randint(0, 9) for _ in range(10)]
print(lst)                                      # [1, 5, 3, 1, 2, 7, 3, 5, 3, 6]

print(search_min_max(lst))                      # (1, 7)
```


> **Задача:** Найти произведение элементов списка, кратных 6 и оканчивающихся на 8. 
> Если таких элементов нет - сообщить об этом

```python
from random import randint

def search_elements(collection):
    p = 1
    result = []
    for value in collection:
        if value % 6 == 0 and value % 10 == 8:
            result.append(value)
            p *= value

    result.insert(0, p)

    return result


lst = [randint(0, 100) for i in range(25)]
print(lst)

res = search_elements(lst)
if len(res) == 1:
    print('Found nothing')
else:
    print(' * '.join(str(x) for x in res[1:]) + ' = ' + str(res[0]))
```