# Selection sort

Алгоритм **сортировки выбором** заключается в поиске на необработанном срезе массива или списка минимального значения и
в дальнейшем обмене этого значения с первым элементом необработанного среза. На следующем шаге необработанный срез 
уменьшается на один элемент. 

**Основные шаги:**
1. Найти наименьшее значение в списке.
2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
5. Продолжать выполнять поиcк и обмен, пока не будет достигнут конец списка.

```python
from random import randint

def selection_sort(collection, direction=True):
    for i in range(len(collection) - 1):
        m = i
        for j in range(i, len(collection)):
            if collection[j] < collection[m] if direction else collection[j] > collection[m]:
                m = j

        collection[i], collection[m] = collection[m], collection[i]

lst1 = [randint(1, 10) for _ in range(15)]
lst2 = lst1.copy()
print('Before sort')
print('lst1 =', lst1)
print('lst2 =', lst2)
print()
print('After sort')
selection_sort(lst1)
print('lst1 =', lst1)
selection_sort(lst2, False)
print('lst2 =', lst2)
```

> Before sort  
> lst1 = [1, 6, 3, 8, 7, 8, 8, 10, 7, 8, 10, 5, 2, 9, 2]  
> lst2 = [1, 6, 3, 8, 7, 8, 8, 10, 7, 8, 10, 5, 2, 9, 2]  
>  
> After sort  
> lst1 = [1, 2, 2, 3, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10]  
> lst2 = [10, 10, 9, 8, 8, 8, 8, 7, 7, 6, 5, 3, 2, 2, 1]  


![selection](img/selection_sort.gif)