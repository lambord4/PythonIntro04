# part I - Именованные функции

**Функции** – это многократно используемые фрагменты программы. Они позволяют дать имя определённому блоку команд с тем, 
чтобы впоследствии запускать этот блок по указанному имени в любом месте программы и сколь угодно много раз. Это 
называется вызовом функции. Мы уже использовали много встроенных функций, как то len и range.

**Функция** – это, пожалуй, наиболее важный строительный блок любой нетривиальной программы (на любом языке 
программирования), поэтому в этой главе мы рассмотрим различные аспекты функций.

**Функция** может принимать параметры и **всегда возвращает** значение

```python
print("Сколько бананов и ананасов для обезьян?")
a = int(input())
b = int(input())
print("Всего", a+b, "шт.")
 
print("Сколько жуков и червей для ежей?")
a = int(input())
b = int(input())
print("Всего", a+b, "шт.")
 
print("Сколько рыб и моллюсков для выдр?")
a = int(input())
b = int(input())
print("Всего", a+b, "шт.")
```


## Объявление функций.
Синтакис:
```
def function_name(<list_of_arguments>):
    body_of_function
# end function
```

Функции определяются при помощи зарезервированного слова `def`. После этого слова указывается имя функции, за которым 
следует пара скобок, в которых можно указать имена некоторых переменных, и заключительное двоеточие в конце строки. 
Далее следует блок команд, составляющих функцию.

```python
def print_some_text():
    print('Hello World!')
```

Для объявления функции, без описания действий которые она будет выполнять, можно воспользоваться следующим выриантом 
описания функции:

```python
def some_function():
    pass
```

Ключевое слово `pass` является своего рода заглушкой и позволяет объявить функцию не описывая её тела.

## Вызов функций. 
Чтоб вызвать функцию на исполнение, достаточно указать, в коде (или прямо в коммандной строке) её имя и круглые скобки,
в которых необходимо перечислить аргументы функции (если таковых нет, круглые скобки необходимо указать пустыми).

```python
def get_2_x_2():                                # объявление функции
    print(2 * 2)
    
get_2_x_2()                                     # 4 (вызов функции)
print(get_2_x_2())                              # 4
                                                # None
```

```python
def get_2_x_2():
    return 2 * 2
    
print(get_2_x_2())                              # 4 (вызов функции)
```

## Примеры создания и вызова функций. 
- функция рисует закрашеный прямоугольник (квадрат)
```python
def draw_rect():
    for _ in range(11):
        for _ in range(11):
            print('* ', end='')
        print()
        
draw_rect()
```

- функция рисует закрашеный треугольник (равнобедренный)
```python
def draw_triangle():
    h = 15
    for i in range(h):
        for j in range(h - i):
            print(' ', end='')
    
        for j in range(h - 2 *i, h+1):
            print('*', end='')
    
        print()
        
draw_triangle()
```

или

```python
def draw_triangle():
    h = 15
    for i in range(h):
        print(' ' * (h-i), end='')
        print('*' * ((h+1) - (h - 2 * i)), end='')
        print()
```

## Передача аргументов.
Функции могут принимать параметры. Параметры могут быть **обязательными** и нет (**по умолчанию**). 
Обязательные параметры - необходимо указывать (передавать) при вызове финкции

```python
def multi(a, b):
    print(a * b)
    
multi(3, 6)                                     # 18
``` 

При передачи параметров в функцию можно использовать литералы (как в примере выше), переменные и даже выражения, 
которые будут вычислены перед вызовом функции.

```python
def multi(a, b):
    print(a * b)
    
    
x = 4
y = 8
multi(x, y)                                     # 32
multi(x+y, y-x)                                 # 48
``` 

Параметры по умолчанию - параметры которые имеют значение, при вызове функции, даже если для них небыли переданы 
значения явно. Отсюда следует, что при вызове функции эти параметры не обязательно указывать.

```python
def func(a, b=3):
    print(a, b)


func(2)                                         # 2 3
func(5, 9)                                      # 5 9
```

Параметры по умолчанию указываются в конце списка параметров.


## Глобальные и локальные переменные. 

**Локальная переменная** - переменная объявленная внутри тела функции является локальной, её область видимости и время
жизни ограничивается телом функции.

```python
def func(x):
    print('param x =', x)
    x = 3
    print('local x =', x)


a = 4
print('before func a =', a)
func(a)
print('after func a =', a)
```

**Глобальная переменная** - переменная объявленная вне тела функции называется глобальной, время жизни и область 
видимости ограничена модулем.

Переменная `a`, из примера выше является глобальной по отношению к переменной `x`.

Если глобальная и локальная переменная имеют одно и тоже имя, то с моменда объявления локальной переменной, она 
перекрывает глобальную переменную.

```python
x = 10
print('global x before func: ', x)              # global x before func:  10


def func():
    x = 3
    print('local x =', x)                       # local x = 3


func()
print('global x after func: ', x)               # global x after func:  10
```

Если необходимо использовать глобальную переменную в теле функции необходимо восользоваться оператором `global`

```python
x = 10
print('global x before func: ', x)              # global x before func:  10


def func():
    global x
    x = 3
    print('local x =', x)                       # local x = 3


func()
print('global x after func: ', x)               # global x after func:  3
```

`nonlocal` - позволяет использовать переменную которая является ни локальной, ни глобально. Применяется, обычно, в 
функциях объявленых внутри другой функции.

```python
def func_outer():
    x = 2
    print('x equal:', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Local variable \'x\' change to:', x)


func_outer()
```

## Ключевые аргументы (параметры по умолчанию).
Можно создать функцию с **необязательными** параметрами, которые, на момент вызова имеют собственные значени, по 
умолчанию. Такие параметры при вызове можно не указывать.

```python
def say(message, times = 1):
    print(message * times)


say('Привет')                                   # Привет
say('Мир ', 5)                                  # Мир Мир Мир Мир Мир
```

Параметры по умолчанию определяются в конце списка параметров

```python
def func(a, b, c, d=1, e=2, f=3):
    pass
```

Обращаясь к параметрам (по умолчанию) по имени можно передавать любое количество параметров и в любой 
последовательности

```python
def func(a, b, c, d=1, e=2, f=3):
    print('a = {A}\tb = {B}\tc = {C}\td = {D}\te = {E}\tf = {F}\n'.format(
        A=a, B=b, C=c, D=d, E=e, F=f
    ))


func(10, 20, 30)                            # a = 10	b = 20	c = 30	d = 1	e = 2	f = 3
func(10, 20, 30, f=40, d=50)                # a = 10	b = 20	c = 30	d = 50	e = 2	f = 40
func(c=30, a=10, b=20)                      # a = 10	b = 20	c = 30	d = 1	e = 2	f = 3
func(e=45, c=30, d=34, a=10, f=56, b=20)    # a = 10	b = 20	c = 30	d = 34	e = 45	f = 56
```  

Ключевые аргументы иницциализируются ОДИН раз, при первом вызове

```python
def func(a, b=[]):
    print('before b =', b, end='\t')
    b.append(a)
    print('after append b =', b)


s = []
func(1, s)                                      # before b = []	after append b = [1]
func(1)                                         # before b = []	after append b = [1]
func(2)                                         # before b = [1]	after append b = [1, 2]
func(3)                                         # before b = [1, 2]	after append b = [1, 2, 3]
func(4)                                         # before b = [1, 2, 3]	after append b = [1, 2, 3, 4]
func(5)                                         # before b = [1, 2, 3, 4]	after append b = [1, 2, 3, 4, 5]
func(1, [])                                     # before b = []	after append b = [1]
func(10)                                        # before b = [1, 2, 3, 4, 5]	after append b = [1, 2, 3, 4, 5, 10]
```

## *args и **kwargs - функции с переменным числом аргументов

Мы можем создавать функции с переменным количеством аргументов или/и переменным количеством ключевых аргументов.  
Для передачи любого количества аргументов, будем использовать `*args` *(правилнее сказать, эту возможность даёт 
оператор `*` который ставится перед именем параметра, само же имя, может быть любым)*

```python
def multi_var(*args):
    print(args)
    for value in args:
        print(value, end=', ')
    print()


multi_var(1, 2, 3, 'ads')                       # (1, 2, 3, 'ads')
                                                # 1, 2, 3, ads, 


a = 5
b = 9
c = 2

multi_var(a, 4+5, 'Hello World!', b, c)         # (5, 9, 'Hello World!', 9, 2)
                                                # 5, 9, Hello World!, 9, 2, 
```

По сути `*args` является кортежем из всех, переданных аргументов.

Для передачи любого количества ключевых аргументов используетсяаргумент `**kwargs` *(так же как и в случае спеременным 
числом аргументов, имя может быть любое, важно наличие оператора `**` перед именам аргумента)*.

```python
def multi_kw(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('key = {k:12}\tvalue = {v}'.format(k=key, v=value))
    print()


multi_kw(name='Ivan', job='Worker', salary=5600)                    
# {'name': 'Ivan', 'job': 'Worker', 'salary': 5600}
# key = name        value = Ivan
# key = job         value = Worker
# key = salary      value = 5600                                    

multi_kw(type='lorry', model='IVECO', length=25.7, weight=8500)      
# {'type': 'lorry', 'model': 'IVECO', 'length': 25.7, 'weight': 8500}
# key = type        value = lorry
# key = model       value = IVECO
# key = lenght      value = 25.7
# key = weght       value = 8500
```

В данном случае `**kwargs` представляетс из себя словарь. Ключами данного словаря выступают имена параметров, а 
значениями - значения параметров.

## Функция это объект

Функция в языке Python - это объект и раз так, то функцию можно присвоить переменной (точнее на функцию можно 
установить ссылку).

Функцию можно вызвать по этой ссылке
```python
def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


x = compare

k = 4
l = 8
print(x(k, l))                                  # -1
```

ссылку на функцию можно передавать как параметр в другую функцию

```python
def list_compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def dict_compare(a, b):
    if len(str(list(a.values())[0])) > len(str(list(b.values())[0])):
        return 1
    elif len(str(list(a.values())[0])) < len(str(list(b.values())[0])):
        return -1
    else:
        return 0


def comparing(collection, comparator):
    i = iter(collection)
    try:
        while True:
            d1 = next(i)
            d2 = next(i)
            if comparator(d1, d2) == 0:
                print(f'{d1} == {d2}')
            else:
                print(f'{d1} <> {d2}')
    except StopIteration as ex:
        print('End of collection')


lst = [2, 5, 3, 3, 4, 3, 3, 2, 1, 1]
dic = [{'type': 'lorry'}, {'model': 'IVECO'}, {'length': 25.7}, {'weight': 8500.1}]

comparing(lst, list_compare)
# 2 <> 5
# 3 == 3
# 4 <> 3
# 3 <> 2
# 1 == 1
# End of collection

comparing(dic, dict_compare)
# {'type': 'lorry'} == {'model': 'IVECO'}
# {'length': 25.7} <> {'weight': 8500.1}
# End of collection
```

Хорошее видео по вопросу [*args и **kwargs](https://www.youtube.com/watch?v=VJJ9wwzgJCA&t=1s)

## Возврат значения(й) из функции

Функция в Python всегда возвращает значение(я), вопрос в другом, какие это значения и как их функция фозвращает.
Любая функция, как минимум, может возвращать значение `None`.
Но это значение несёт мало информации. Горазно более важно вернуть какайто более весомый результат выполнения функции.
Например, функция которая умее возводить число в степень, может, не просто напечатать результат на экране, а вернуть его
в код который вызвал эту функцию

```python
def my_pow(a, b):
    return a ** b


x = my_pow(2, 5)
print(x)                                        # 32
```

Как вы могли заметить в коде функции появился новый оператор `return`. Как раз он и используется для возврата ОДНОГО 
значения из функции. Если этого оператора в функции нет, то функция возвращает `None`.

```python
def my_pow(a, b):
    return a ** b


x = my_pow(2, 5)
print(x)                                        # 32
                                                # None
```

Для того чтоб вернуть несколько значений, мы можем из "запаковать", например, в кортеж и вернуть уже кортеж

```python
def basic_arithmetic(x, y):
    sum = x + y
    product = x * y
    quotient = x / y
    difference = x - y

    return sum, product, quotient, difference   # ==> (sum, product, quotient, difference)


print(basic_arithmetic(3, 30))                  # (33, 90, 0.1, -27)
# or
print(basic_arithmetic(3,30)[0])                # 33
print(basic_arithmetic(3,30)[1])                # 90
print(basic_arithmetic(3,30)[2])                # 0.1
print(basic_arithmetic(3,30)[3])                # -27
```

Так же, мы можем вернуть именованный кортеж

```python
from collections import namedtuple


def basic_arithmetic(x, y):
    sum = x + y
    product = x * y
    quotient = x / y
    difference = x - y

    # Create named tuple
    result = namedtuple("Result", "sum product quotient difference")
    this_result = result(sum, product, quotient, difference)

    return this_result


calculation = basic_arithmetic(3, 30)

print(calculation.sum)
print(calculation.product)
print(calculation.quotient)
print(calculation.difference)
```

Почитать об именованных кортежах можно [здесь](https://habr.com/ru/post/330034/).


## Встроенные функции Python

Прежде чем вы решите сесть и написать замечательную функцию, спросите себя: «Для этого уже есть встроенная функция?».  
Python включает в себя ряд функций, встроенных прямо в интерпретатор, которые вы можете использовать сразу. Иногда вы 
можете обнаружить, что уже есть функция, которая делает то, что вы хотите, или, по крайней мере, часть этого.  
Например, Python включает `sum()` функцию, которую можно использовать вместо той, `calculation.sum` что мы использовали 
в приведенном выше примере. На самом деле встроенная `sum()` функция делает больше, так как позволяет вам предоставить 
список чисел (т.е. она может добавлять более двух чисел одновременно).  
Следующие функции всегда доступны, так как они встроены прямо в интерпретатор Python. Если вы знакомы с другими языками
программирования, вы, вероятно, узнаете некоторые из них и догадаетесь, как они работают. В любом случае, смотрите 
[официальные документы](https://docs.python.org/3/library/functions.html) для получения дополнительной информации о том,
как каждый из них работает.

```
+---------------+--------------+----------------+
| abs()         | frozenset()  | open()         |
| all()         | getattr()    | ord()          |
| any()         | globals()    | pow()          |
| ascii()       | hasattr()    | print()        |
| bin()         | hash()       | property()     |
| bool()        | help()       | range()        |
| bytearray()   | hex()        | repr()         |
| bytes()       | id()         | reversed()     |
| callable()    | input()      | round()        |
| chr()         | int()        | set()          |
| classmethod() | isinstance() | setattr()      |
| compile()     | issubclass() | slice()        |
| complex()     | iter()       | sorted()       |
| delattr()     | len()        | staticmethod() |
| dict()        | list()       | str()          |
| dir()         | locals()     | sum()          |
| divmod()      | map()        | super()        |
| enumerate()   | max()        | tuple()        |
| eval()        | memoryview() | type()         |
| exec()        | min()        | vars()         |
| filter()      | next()       | zip()          |
| float()       | object()     | __import__()   |
| format()      | oct()        |                |
+---------------+--------------+----------------+
```

Вы также можете проверить индекс пакетов Python [PyPI](https://pypi.org/) , который представляет собой массивный 
репозиторий модулей, пакетов и даже каркасов приложений Python.