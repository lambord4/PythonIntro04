# Декораторы

Замеряем время выполнения функции

```python
from datetime import datetime

def gen_1():
    lst = []
    start = datetime.now()
    for i in range(10**5):
        if i % 2 == 0:
            lst.append(i)
    print(datetime.now() - start)
    return lst

def gen_2():
    start = datetime.now()
    lst = [x for x in range(10**5) if x % 2 == 0]
    print(datetime.now() - start)
    return lst

gen_1()                                         # 0:00:00.045635
gen_2()                                         # 0:00:00.017619
```

Но в этом примере яно есть повторяющийся код, да и хорошая функция должна выполнять одно лог. действие, а наши функции 
выполняют два: генерируют списки чётных значений и замеряют время. Это не очень хорошо.

Функции - объекты первого класса.

Чтоб избавиться от подобных проблем, мы можем создать декоратор который сможет замерять время выполнения функции.
```python
def measure_time(function):
    from datetime import datetime

    def wrapper():
        start = datetime.now()
        result = function()
        print(datetime.now() - start)
        return result
    return wrapper

@measure_time
def gen_1():
    lst = []
    for i in range(10**5):
        if i % 2 == 0:
            lst.append(i)

    return lst

@measure_time
def gen_2():
    lst = [x for x in range(10**5) if x % 2 == 0]
    return lst

gen_1()
gen_2()
```

Если предполагается передавать в наши функции какие-то параметры, то это надо учесть в декораторе
```python
def measure_time(function):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = function(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@measure_time
def gen_1(num):
    lst = []
    for i in range(num):
        if i % 2 == 0:
            lst.append(i)

    return lst

@measure_time
def gen_2(num):
    lst = [x for x in range(num) if x % 2 == 0]
    return lst

gen_1(10**5)
gen_2(10**5)
```

Как это всё работает

```python
def measure_time(function):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = function(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

def gen_1(num):
    lst = []
    for i in range(num):
        if i % 2 == 0:
            lst.append(i)

    return lst

def gen_2(num):
    lst = [x for x in range(num) if x % 2 == 0]
    return lst

g1 = gen_1
res = g1(10)
print(res)                                      # [0, 2, 4, 6, 8]

dec1 = measure_time(gen_1)
print(type(dec1), dec1.__name__)                # <class 'function'> wrapper
res = dec1(10)
print(res)                                      # [0, 2, 4, 6, 8]

res = measure_time(gen_1)(10)                   # ==> wrapper(10) [0, 2, 4, 6 , 8]
```

Декораторы так же как и любая функция (декоратор и есть функция) могут принимать параметры

```python
def measure_time(arg):
    from datetime import datetime
    print(arg)

    def outer(function):

        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer

@measure_time('gen_1')
def gen_1(num):
    lst = []
    for i in range(num):
        if i % 2 == 0:
            lst.append(i)

    return lst

@measure_time('gen_2')
def gen_2(num):
    lst = [x for x in range(num) if x % 2 == 0]
    return lst

gen_1(10**5)
gen_2(10**5)

res = measure_time('gen_1')(gen_1)(10)
print(res)                                      # [0, 2, 4, 6, 8]
```