# Рекурсия

## Что такое рекурсия и рекурсивная функция

**Рекурсивная функция** - это функция, определяемая в терминах самой себя посредством выражений с самоссылкой, или 
более простыми словами, рекурсивная функция - это функция способная вызывать саму себя.  
Это означает, что функция будет продолжать вызывать себя и повторять свое поведение, пока не будет выполнено какое-либо 
условие для возврата результата. Все рекурсивные функции имеют общую структуру, состоящую из двух частей: базовый случай
и рекурсивный случай.

Давайте попробуем разобраться с этим понятием. Для примера возьмём простую задачу - возведение числа в степень. В 
математике, решение этой задачи будет выглядеть так:

> 2<sup>3</sup> = 2 x 2 x 2

Как ещё можно записать эту задачу? Очень просто:

> 2<sup>3</sup> = 2 x 2<sup>2</sup> ==> 2 x 2<sup>1</sup> ==> 2 x 2<sup>0</sup> ==> 1

То есть:

> 2<sup>N</sup> = 2 x 2 x ... x 2 - N раз

или

> 2<sup>N</sup> = 2 x 2<sup>N-1</sup>

Первый вариант функции, которая возводит число в степень путём умножения числа само на себя некоторое количество раз 
(использование циклов), называется - итеративное решение, выглядит так:

```python
def iteratively_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res
    
print(iteratively_pow(2, 5))                    # 32
```

И второй вариант, аналог первого, но используещего другой подход для решения - `рекурсию`, будет выглядеть так:

```python
def recursive_pow(num, exp):
    # base case
    if exp == 0:
        return 1

    # recursive case
    return num * recursive_pow(num, exp-1)
    
print(recursive_pow(2, 5))                      # 32
``` 

Так же решается и задача с вычисление факториала (Факториал числа N - это произведение всех чисел от 1 до числа N 
включительно). Давайте попробуем её разобрать.

Факториал 5-ти записывается так: `5!` и его решение будет выклядить как произведение всех чисел от 1 до 5 включительно:

> 5! = 1 x 2 x 3 x 4 x 5 = 120

или, эту же задачу можно решить так:

> 5! = 5 x 4! ==> 4 x 3! ==> 3 x 2! ==> 2 x 1! ==> 1

или

> N! = 1 x 2 x 3 x .... x N-1 x N

и

> N! = N x (N - 1)!

Ну и функции, итеративная и рекурсивная:

```python
def factorial_iteratively(num):
    res = 1
    for i in range(1, num+1):
        res *= i

    return res
    
print(factorial_iteratively(5))                 # 120
```

```python
def factorial_recursive(num):
    if num == 1:
        return 1

    return num * factorial_recursive(num-1)

print(factorial_recursive(5))                   # 120
```

![img](img/factorial_rec.gif)


## Поддержка состояния

При работе с рекурсивными функциями необходимо помнить, что каждый рекурсивный вызов имеет свой собственный контекст 
выполнения, поэтому для поддержания состояния во время рекурсии необходимо:
- пропустите состояние через каждый рекурсивный вызов так, чтобы текущее состояние было частью контекста выполнения 
текущего вызова
- поддерживать состояние в глобальном масштабе

Например, нам необходимо посчитать (с использованием рекурсии) сумму чисел от 1 до 100: 

> 1 + 2 + 3 + ... + 99 + 100

Состояние которое мы должны поддерживать это: текущее число что мы добавляем и накопленную, уже, сумму.

Вот как это выглядит если пропускать это состояние через каждый рекурсивный вызов (т.е. передавая обновлённое текущее 
состояние, в качестве аргумента, каждому рекурсивному вызову):

```python
def recursive_sum(number, summa):
    # base case - return the final state
    if number == 0:
        return summa

    # recursive case - thread the state through the recursive call
    else:
        return recursive_sum(number - 1, summa + number)

print(recursive_sum(10, 0))                     # 55
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)   # 55
```

или вот так, если сохранять в глобальном контексте:

```python
number = 10                                     # gloabla variable 'number'
summa = 0                                       # global variable 'summa'

def recursive_sum():
    global number
    global summa

    # base case
    if number == 0:
        return summa

    # recursive case
    summa += number
    number -= 1
    return recursive_sum()

print(recursive_sum())
```

## Рекурсивные структуры данных

**Структура данных** может считаться рекурсивной, если она может быть определена в терминах уменьшенной версии самой 
себя. Список является примером рекурсивной структуры данных.   
Например, есть пустой список, и единственная операция, которую можно выполнить над ним:

```python
def attach2head(new_element, lst):
    return [new_element] + lst


lst = []
print(lst)                                      # []
lst = attach2head('hello', lst)
print(lst)                                      # ['hello']
lst = attach2head(-31, lst)
print(lst)                                      # [-31, 'hello']
lst = attach2head(46, lst)
print(lst)                                      # [46, -31, 'hello']
lst = attach2head(1, lst)
print(lst)                                      # [1, 46, -31, 'hello']


lst = []
lst = attach2head(1, attach2head(46, attach2head(-31, attach2head('hello', lst))))
print(lst)                                      # [1, 46, -31, 'hello']
```

![attach2head](img/attach2head.gif)

Начиная с пустого списка, можно сгенерировать любой список рекурсивно вызывая функцию `attach2head()`. Применяя функцию
к аргументу (пустому списку), передаём результат её работы в другой вызов, этой же функции, как аргумент.  
Многократная передача функции `attach2head()`, как аргумента, в другой её вызов, равносильно многократному вызову этой
функции. 

В качестве рекурсивной структур данных можно использовать не только списки, но и множества, словари 

Можно построить рекурсивную функция для работы с уже созданной рекурсивной структурой данных. Например, можно рекурсивно
посчитать сумму элементов списка:

```python
from random import randint

def recursive_list_sum(lst):
    if not lst:
        return 0

    return lst[0] + recursive_list_sum(lst[1:])


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst1, '= ', end='')
print(recursive_list_sum(lst1))                 # [1, 2, 3, 4, 5, 6, 7, 8, 9] = 45
lst2 = [randint(1, 10) for _ in range(15)]
print(lst2, '= ', end='')
print(recursive_list_sum(lst2))                 # [6, 9, 9, 7, 2, 4, 7, 10, 6, 4, 7, 7, 10, 2, 6] = 96
```

## Наивная рекурсия

Наивную рекурсию попробуем рассмотреть на примере вычисления чисел Фибоначчи.

Числа Фибоначчи были первоначально определены итальянским математиком Фибоначчи в тринадцатом веке для моделирования 
роста популяций кроликов. Фибоначчи предположил, что число пар кроликов, рожденных в данном году, равно числу пар 
кроликов, рожденных в каждом из двух предыдущих лет, начиная с одной пары кроликов в первый год.

[![fibonacci number](img/fib_number.png)](https://www.youtube.com/watch?v=tje_xhghD6A)

Числа Фибоначчи описывают следующую последовательность:

> F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>

Частные случаи это:

> F<sub>0</sub> = 0 и F<sub>1</sub> = 1

Рекурсивная функция для вычисления числа фибоначи выглядит так:

```python
# 0 1 1 2 3 5 8 13 21 34 55 89
# 0 1 2 3 4 5 6 7  8  9  10 11

def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="")

    # Base case
    if 0 <= n <= 1:
        return n

    # Recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(5))
```

> Calculating F(5)  
> Calculating F(4)  
> Calculating F(3)  
> Calculating F(2)  
> Calculating F(1)  
> Calculating F(0)  
> Calculating F(1)  
> Calculating F(2)  
> Calculating F(1)  
> Calculating F(0)  
> Calculating F(3)  
> Calculating F(2)  
> Calculating F(1)  
> Calculating F(0)  
> Calculating F(1)  
> Result fib(5) = 5

Это наивная реализация. Но явно видны повторяющиеся вызовы функции, что не очень оптимально.

Если воспользоваться `декоратором` из пакета `functools`, то можно, существенно улучшить работу данной функции за счёт 
кэширования некоторых (повторяющихся) вызовов: 

```python
# 0 1 1 2 3 5 8 13 21 34 55 89
# 0 1 2 3 4 5 6 7  8  9  10 11
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="")

    # Base case
    if 0 <= n <= 1:
        return n

    # Recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(11))
```

> Calculating F(5)  
> Calculating F(4)  
> Calculating F(3)  
> Calculating F(2)  
> Calculating F(1)  
> Calculating F(0)  
> Result fib(5) = 5  

`lru_cache` это декоратор, который кеширует результаты. Таким образом, мы избегаем повторного вычисления, явно проверяя 
значение перед тем, как пытаться вычислить его. Следует помнить одну вещь: `lru_cache` использует для кэширования 
результатов словарь, позиционные и ключемые аргументы (которые служат ключами в этом словаре) функции должны быть 
хэшируемыми.

## Ограничения рекурсии

Любая рекурсивная функция должна иметь условие выхода из рекурсии. Если это условие отсутствует или определено не верно
то можно вызвать переполнение стека, что вызовет аварийное завершение программ. Глубина стека для рекурсивных вызовов
ограничена. Но её (глубину) можно временно изменить, если в этом етьс необходимость

```python
import sys

print(sys.getrecursionlimit())                  # 1000
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())                  # 3000
```

Привет неверного определения уловия выхода из рекурсии (точнее его отсутствие):

```python
def r_pow(num, exp):
    return num * r_pow(num, exp-1)


print(r_pow(2, 5))
```

в результате получаем исключение:

> return num * r_pow(num, exp-1)  
    [Previous line repeated 995 more times]  
> RecursionError: maximum recursion depth exceeded

## Преимущества рекурсии

1. Рекурсивные функции делают код более чистым и элегантным.
2. Сложная задача может быть разбита на более простые подзадачи с помощью рекурсии.
3. Генерация последовательности проще с рекурсией, чем с использованием некоторой вложенной итерации.

## Недостатки рекурсии

1. Иногда логику рекурсии трудно понять.
2. Рекурсивные вызовы дороги (неэффективны), так как занимают много памяти и времени.
3. Рекурсивные функции трудно отлаживать.

---

## Небольшой пример использования рекурсии на практике:

```python
def discovery_fs(root_dir, indent_level=1):
    import os

    for name in os.listdir(root_dir):
        if not name.startswith('.'):
            try:
                path = os.path.join(root_dir, name)
                prefix = indent_level * (' '*4)
                if os.path.isfile(path):
                    print('{prefix} ({size} bytes)'.format(prefix=prefix + '|__ ' + name,
                                                           size=os.path.getsize(path)))
                else:
                    print(prefix + name + ':')
                    discovery_fs(path, indent_level+1)
            except Exception as ex:
                print(ex)


discovery_fs('<some path>')
```

данная функция позволяет обойти объекты файловой системы и построить дерево вложености, начиная с `root_dir`.

























