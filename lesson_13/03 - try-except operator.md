# try - except - else - finally, assert, raise

Синтаксические ошибки обнаруживаются анализаторами кода на этапе написания этого кода и могут быть исправлены сразу

```
print(25 / 0))
  File "<input>", line 1
    print(25 / 0))
                 ^
SyntaxError: invalid syntax
```

в сообщении об ршибке ясно сказано о выявленой **синтаксической ошибке**. И даже показано возможное место ошибки `^`. В
данном примере, оказалась лишняя закрывающаяся скобка.  
Исправим и попробуем запустить код снова

```
print(25 / 0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    print(25 / 0)
ZeroDivisionError: division by zero
```

и опять ошибка, но теперь другая. Мы поймали исключение или `Exception`. И эта ошибка, является ошибкой этапа 
выполнения, мы попытались выполнить деление на ноль. Об этом говорит и сообщение об ошибке

```
ZeroDivisionError: division by zero
```

Это системное исключение, которое встроено в Python. Python имеет довольно большой набор встроеных исключений. С списком 
этих исключений можно ознакомиться ниже или в [документации](https://docs.python.org/3/library/exceptions.html) Python.

## Возбуждение исключений
Исключения вызываться автоматически, вашим кодом, но могут возбуждаться и самим пользователем, для того чтоб 
сигнализировать вызывающему процессу о возникновении какой-то исключительной ситуации. Для этих целей используется 
оператор `raise`.   
Синтаксис оператора

```
raise <some_exception>(message)
```

Например, нам необходимо возбуждать исключение, если в функцию передаётся отрицательное значение

```python
def some_function(value):
    if value < 0:
        raise ValueError('Value must be positive')

    print('value is', value)


some_function(5)
some_function(-5)
```

```
value is 5

Traceback (most recent call last):
  File "/Users/nikolay.kiseev/PycharmProjects/HillelExamples/tt.py", line 9, in <module>
    some_function(-5)
  File "/Users/nikolay.kiseev/PycharmProjects/HillelExamples/tt.py", line 3, in some_function
    raise ValueError('Value must be positive')
ValueError: Value must be positive
```

В данном примере видно что как только было передано отрицательное значение, сработал оператор `if` и в нём было 
сгенерировано исключение `ValueError` с соббщением о том что значение должно быть только положительным.  
Таким образом можно сообщить вызывающему коду о том что, что-то пошло не так.

## Утверждения `assert`

Инструкция assert позволяет производить проверки истинности утверждений, что может быть использовано в отладочных целях.
Эта инструкция является средством отладки, а не механизмом обработки ошибок. Если проверка не прошла, возбуждается 
исключение `AssertionError`.  
`AssertionError` - возбуждается когда выражение в `assert` возпращает `False`.  
 Рекомендуется использовать инструкцию только для проверки внутреннего состояния программы — ситуаций, которые не должны
 происходить вовсе, которые нельзя обработать или это не имеет смысла (обычно это является указанием на то, что код 
 программы содержит ошибку).
 
```python
x = 5

assert x < 10, 'value more than 10'

# the same

if not x < 10:
    raise AssertionError('value more than 10')
```

код ниже, будет работать только если будет запущен в операционной системе Linux

```python
import sys

assert 'linux' in sys.platform, 'This code work in Linux only'
```

иначе мы получим 

```
Traceback (most recent call last):
  File "/Users/nikolay.kiseev/PycharmProjects/HillelExamples/tt.py", line 2, in <module>
    assert 'linux' in sys.platform, 'This code work in Linux only'
AssertionError: This code work in Linux only
```

Несколько предостережений:
1. никогда не используйте `assert` для проверки данных
    > выполнение `assert` может быть отключено в компиляторе и соответственно все проверки реализованые на `assert` 
    просто не будут выполняться
                                                          
2. будьте внимательны при описании условий в `assert`
    > иногда, при написании условий в `assert` может получиться так, что условие никогда не будет ложным

Например:    

```python
assert 1 == 2, '1 not equal 2'                  # correct
assert (1 == 2, '1 not equal 2')                # not correct
```

## Блок обработки исключений try - except

Блок `try - except` используется для перехвата и обработки исключений. Общая форма записи данного оператора выглядит
следующим образом

```
try:
    oretator 1
    operator 2
    .
    .
    .
    operator N
except <some_exception_error> [as <same name>]:
    some code to use if appere <some_exception_error>
```

Как работает данный операторор. Код в которым необходимо отслеживать исключения (исключительный или критические 
ситуации) помещается сразу за ключевым словом `try`, перед словом `except`. Если в этом блоке кода произойдёт какая-то
ошибка, то будет сгенерировано исключение. Если это исключение совпадёт с `<some_exception_error>`, будет выполнен код
помещённый в блок `except`.

```python
x = int(input('Пожалуйста, введите первое число: '))
y = int(input('Пожалуйста, введите второе число: '))

try:
    print('Результат деления:', x / y)
except ZeroDivisionError as ex:
    print(ex)
```

если второе число будет ноль, то мы увидем следующий вывод

```
Пожалуйста, введите первое число: 6
Пожалуйста, введите второе число: 0
division by zero
```

да, деление не выполнилось, но и программа не завершилась с ошибкой. И появилась возможность, как-то отреагировать на 
попытку деления на ноль.  
Если пример, приведённый выше, поместить в оператор цикла, то мы просто пропустили одну итерацию и перейдём к следующей,
без аварийного завершения программы

```python
while True:
    try:
        x = int(input('Пожалуйста, введите первое число: '))
        y = int(input('Пожалуйста, введите второе число: '))
        print('Результат деления:', x / y)
    except ZeroDivisionError as ex:
        print('Деление на ноль невозможно.\nВведите другие значения.')
```

> Не желательно в качестве перехватываемого исключения указывать `Exception` так как в таком случае, блок `try-except` 
> будет перехватывать любые исключения что могут возникнуть в коде блока `try`. Это маскирует ошибки и их сложно 
> анализировать.

Если в коде предполагается возникновение нескольких, различных типов исключений, можно применить несколько блоков 
`except`

```python
while True:
    try:
        x = int(input('Пожалуйста, введите первое число: '))
        y = int(input('Пожалуйста, введите второе число: '))
        print('Результат деления:', x / y)
    except ZeroDivisionError as ex:
        print('Деление на ноль невозможно.\nВведите другие значения.')
    except ValueError as ex:
        print('Неверные тип значения.\nВведите другие значения.')
```

Итак: 
- код в блоке `try` выполняеться полностью, если не будут возникать никакие исключения, иначедо того момента как 
возникнет первое исключение
- в блоке `except` описавается то как программа должна отреагировать на возникшее исключение
- можно перехватывать несколько типов исключений в одном операторе `try`

## Блок оператор else

Данный оператор уже появлялся не раз. Он может использоваться совместно с оператором `if`, с любым оператором цикла.
С оператором `try-except` его так же можно использовать

```
try:
    oretator 1
    operator 2
    .
    .
    .
    operator N
except <some_exception_error> [as <same name>]:
    some code to use if appere <some_exception_error>
else:
    run this code if no any exception
```

блок `else` будет выполняться только если блок `try` завершится полностью и без ошибок. Точно как в циклах.

```python
while True:
    try:
        x = int(input('Пожалуйста, введите первое число: '))
        y = int(input('Пожалуйста, введите второе число: '))
        print('Результат деления:', x / y)
    except ZeroDivisionError as ex:
        print('Деление на ноль невозможно.\nВведите другие значения.')
    except ValueError as ex:
        print('Неверные тип значения.\nВведите другие значения.')
    else:
        print('Ошибок не было встречено!')
```

```
Пожалуйста, введите первое число: 9
Пожалуйста, введите второе число: 3
Результат деления: 3.0
Ошибок не было встречено!
Пожалуйста, введите первое число: 9
Пожалуйста, введите второе число: 0
Деление на ноль невозможно.
Введите другие значения.
Пожалуйста, введите первое число: 4
Пожалуйста, введите второе число: а
Неверные тип значения.
Введите другие значения.
Пожалуйста, введите первое число: 5
Пожалуйста, введите второе число: 7
Результат деления: 0.7142857142857143
Ошибок не было встречено!
Пожалуйста, введите первое число:
...
```

## Блок оператора finally

Оператор `try-except` так же может быть дополнен, необязательным блоком `finally`. Этот блок будет выполняться всегда 
когда мы будем покидать оператор `try-excep` не звависимо от того был тот успешен или нет.  
Этот блок можно использовать для освобождения некоторых ресурсов, что были задействованы в программе и в частности в 
блоке `try-except`.

```python
try:
    file = open('text.txt', 'r')
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
    print('Первое число {n1} и второе число {n2}'.format(n1=num1, n2=num2))
    print('Результат деления: {res}'.format(res=num1/num2))
    file.close()
except FileNotFoundError as ex:
    print('Файл небыл найден!')
finally:
    if not file.closed:
        print('Файл закрыт небыл! Закрываю!')
        file.close()
```

```
Первое число 5 и второе число 0
Traceback (most recent call last):
  File "/Users/nikolay.kiseev/PycharmProjects/HillelExamples/tt.py", line 8, in <module>
    print('Результат деления: {res}'.format(res=num1/num2))
ZeroDivisionError: division by zero
Файл закрыт небыл! Закрываю!
```

## Что узнали
Ошибки бывают разные синтаксические и исключения, узнали о различных способах вызывать и 
обрабатывать исключения в Python.
- raise позволяет выбросить исключение в любое время, по необходимости.
- assert позволяет проверить, выполнено ли определенное условие, и выдать исключение, если это не так тем самым промодя
отладку и тестирование кода
- В блоке `try-except` все операторы выполняются до тех пор, пока не встретится исключение.
- `except` используется для перехвата и обработки исключений, которые встречаются в предложении `try`.
- `else` позволяет какой-то код только тогда, когда в предложении `try` отсутствуют исключения.
- `finally` позволяет выполнять разделы кода, которые должны выполняться всегда, с любыми ранее возникшими исключениями 
или без них.

## Список встроеных исключений
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```