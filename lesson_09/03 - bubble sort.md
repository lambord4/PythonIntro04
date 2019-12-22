# Bubble sort

**Сортировка пузырьком** - это метод сортировки массивов и списков путем последовательного сравнения и обмена соседних
элементов, если предшествующий оказывается больше последующего. В процессе выполнения данного алгоритма элементы с 
большими значениями оказываются в конце списка, а элементы с меньшими значениями постепенно перемещаются по направлению 
к началу списка. Образно говоря, тяжелые элементы падают на дно, а легкие медленно всплывают подобно пузырькам воздуха.

В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка минус единица, так как 
когда второй элемент становится на свое место, то первый уже однозначно минимальный и находится на своем месте.

Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже отсортирован,
и выполнять проход по этим элементам смысла нет.

```python
from random import randint

def bubble_sort(collection, direction=True):
    count_of_iteration = 0
    for i in range(len(collection)-1):
        for j in range(len(collection) - i - 1):
            if collection[j] > collection[j+1] if direction else collection[j] < collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]

        count_of_iteration += 1
    return count_of_iteration

lst1 = [randint(1, 10) for _ in range(15)]
lst2 = lst1.copy()
print('Before sort')
print('lst1 =', lst1)
print('lst2 =', lst2)

print()
print('After sort')
print('cnt iter lst1 =', bubble_sort(lst1))
print('lst1 =', lst1)

print()
print('cnt iter lst2 =', bubble_sort(lst2, False))
print('lst2 =', lst2)
```

> Before sort  
> lst1 = [2, 4, 1, 5, 3, 6, 9, 9, 7, 6, 5, 10, 7, 7, 8]  
> lst2 = [2, 4, 1, 5, 3, 6, 9, 9, 7, 6, 5, 10, 7, 7, 8]  
>
> After sort  
> cnt iter lst1 = **14**  
> lst1 = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 9, 9, 10]  
>
> cnt iter lst2 = **14**  
> lst2 = [10, 9, 9, 8, 7, 7, 7, 6, 6, 5, 5, 4, 3, 2, 1]  


Этот алгоритм довольно медлительный так как выполняет. Он будет неплохо работать на небольшом списке (массиве), но если
список большой, то количество проходов по списку (массиву) будет так же увеличиваться.  
Но алгоритм можно немного оптимизировать, если добавив проверку того факта, что была ли перестановка элементов 
(значений) на предыдущем проходе или нет.

```python
from random import randint

def bubble_sort(collection, direction=True):
    count_of_iteration = 0
    for i in range(len(collection)-1):
        flag = True
        for j in range(len(collection) - i - 1):
            if collection[j] > collection[j+1] if direction else collection[j] < collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
                flag = False

        if flag:
            break
        count_of_iteration += 1
    return count_of_iteration

lst1 = [randint(1, 10) for _ in range(15)]
lst2 = lst1.copy()
print('Before sort')
print('lst1 =', lst1)
print('lst2 =', lst2)

print()
print('After sort')
print('cnt iter lst1 =', bubble_sort(lst1))
print('lst1 =', lst1)

print()
print('cnt iter lst2 =', bubble_sort(lst2, False))
print('lst2 =', lst2)
```

> Before sort  
> lst1 = [10, 4, 1, 5, 10, 1, 9, 6, 1, 7, 1, 7, 6, 1, 3]  
> lst2 = [10, 4, 1, 5, 10, 1, 9, 6, 1, 7, 1, 7, 6, 1, 3]  
>
> After sort  
> cnt iter lst1 = **9**  
> lst1 = [1, 1, 1, 1, 1, 3, 4, 5, 6, 6, 7, 7, 9, 10, 10]
>
> cnt iter lst2 = **7**  
> lst2 = [10, 10, 9, 7, 7, 6, 6, 5, 4, 3, 1, 1, 1, 1, 1]


![bubble](img/bubble_sort.gif)  
[визуализация](https://www.youtube.com/watch?v=7vqkHGKbb8k)
