# Insertion sort

**Сортировка вставками** — простой алгоритм сортировки. Хотя этот алгоритм сортировки уступает в эффективности более 
сложным (таким как быстрая сортировка), у него есть ряд преимуществ:
- эффективен на небольших наборах данных, на наборах данных до десятков элементов может оказаться лучшим;
- эффективен на наборах данных, которые уже частично отсортированы;
- это устойчивый алгоритм сортировки (не меняет порядок элементов, которые уже отсортированы);
- может сортировать список по мере его получения;

На каждом шаге алгоритма мы выбираем один из элементов входных данных и вставляем его на нужную позицию в уже 
отсортированном списке, до тех пор, пока набор входных данных не будет исчерпан. Метод выбора очередного элемента из 
исходного массива произволен; может использоваться практически любой алгоритм выбора. Обычно (и с целью получения 
устойчивого алгоритма сортировки), элементы вставляются по порядку их появления во входном массиве.
Приведенный ниже алгоритм использует именно эту стратегию выбора.

```python
from random import randint

def insertion_sort(collection, direction=True):
    for i in range(len(collection)):
        tmp = collection[i]
        for j in range(i-1, -1, -1):
            if tmp < collection[j] if direction else tmp > collection[j]:
                break

            collection[j+1], collection[j] = collection[j], collection[j+1]

lst1 = [randint(1, 10) for _ in range(15)]
lst2 = lst1.copy()
print('Before sort')
print('lst1 =', lst1)
print('lst2 =', lst2)
print()
print('After sort')
insertion_sort(lst1)
print('lst1 =', lst1)
insertion_sort(lst2, False)
print('lst2 =', lst2)
```

![insertion](img/insertion_sort.gif)
