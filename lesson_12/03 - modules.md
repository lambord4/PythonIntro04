# Модули

Любой файл с расширением .py - это мудуль.

На самом деле в Python три вида модулей:
1. модуль может быть написан на Python (*.py)
2. модуль может быть написан на С и закружаться динамически во время выполнения, (например как модуль **re** 
предоставляющий нам возможность работать с регулярными выражениями)
3. встроенный в интерпретатор модуль (например как itertools)

Доступ ко всем модулям осуществляется посредством оператора `import` в нескольких вариациях.

Для создания Python модуля, состаточно создать фай с расширением `py` и добавить в него код:

```python
# my_module.py

string = 'Hello World!'
number = 1234567
pi_number = 3.14

some_list = [4356, string, 'Test', 'a', pi_number]


def print_list(lst):
    for element in lst:
        print(element, end=' ')
    print()
    

class TestClass:
    pass
```

Данный модуль содержит строку `string`, целое число `number`, число с плавающей точкой `pi_number`, список `some_list`,
функцию `print_list` и пустой класс `TestClass`.

Чтобы получить доступ ко всему содержимому это модуля, необходимоего его импортировать:

```python
import my_module

print(my_module.string)

print(my_module.pi_number)

my_module.print_list(my_module.some_list)
```

## Пути поиска модулей (и пакетов)

Как же выполняется поиск модулей и где? Когда Python импортирует какой-то модуль, то ищет этот модуль в списке каталогов
который получил из следующих источников:
- текущий каталок, откуда был замущен скрипт содержащий инструкцию `import`
- список каталогов содержащийся в переменной [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
- зависящий от установки Python

Окончательный список каталогов поиска модулей можно посмотреть так:

```python
import sys

print(sys.path)
```

Чтоб Python смог найти ваш модуль, необходимо поместить его рядом с запускаемым скриптом или в любой каталог поиска, или
добавить каталог с модулем в переменную `path` из модуля `sys`. Так как эта переменныя есть ссылка на список строк 
(путей), то используя метод `sys.path.append()` можно добавить свой путь в список поиска модулей.  
После того как модуль был импортирован, его местоположение можно узнать если прочитать атрибут `__file__`

```python
import my_module

print(my_module.__file__)       # /Users/some_user/PycharmProjects/HillelExamples/my_module.py 
```

## Оператор - import

Простейшая форма записи выглядит так:

### import <module_name>

Это не делает доступным, содержимое данного модуля, напрямую.

Каждый модуль содержит личную таблицу имён (**private symbol table**), которая является глобальной таблицей имён для 
данного модуля. Эта таблица определяет отдельное пространство имём.

Оператор `import <module_name>` только размещается `<module_name>` в таблице имён вызывающего модуля. Эти объекты, 
определенные в модуле остаются в частной таблице имён модуля.  
Из вызывающей стороны объекты в модуле доступны только в том случае, если с префиксом `<module_name>` используется 
**точечная нотация**.  
После следующего `import` утверждения модуль помещается в таблицу локальных имён. Таким образом, модуль имеет значение в
локальном контексте вызывающего модуля:

```python
import my_module

print(my_module)        # <module 'my_module' from '/Users/some_user/PycharmProjects/HillelExamples/my_module.py'>
```

Но `string` и `print_list` остаются в таблице имён частного модуля и не имеют смысла в локальном контексте:

```python
import my_module

print(string)           # NameError: name 'string' is not defined
print_list([])          # NameError: name 'print_list' is not defined
```

Для доступа в локальном контексте имена объектов, определенных в модуле, должны иметь префикс `my_module`:

```python
import my_module

print(my_module.string)                         # Hello World!
my_module.print_list(my_module.some_list)       # 4356 Hello World! Test a 3.14
```

Несколько разделенных запятыми модулей могут быть указаны в одном `import` выражении:

`import <module_name>[, <module_name> ...]`

### from <module_name> import <name(s)>

Альтернативная форма оператора `import` позволяет импортировать отдельные объекты из модуля непосредственно в таблицу
имён вызывающего модуля:

```python
from my_module import string, print_list, some_list
```

После выполнения вышеприведенного оператора на него `<name(s)>` можно ссылаться в среде вызывающего без 
`<module_name>` префикса:

```python
from my_module import string, print_list, some_list

print(string)                                   # Hello World!
print_list(some_list)                           # 4356 Hello World! Test a 3.14
```

Поскольку эта форма `import` помещает имена объектов непосредственно в таблицу имён вызывающей стороны, любые объекты, 
которые уже существуют с тем же именем, будут перезаписаны:

```python
string = 'Test string'
print('variable "string before import =', string)   # variable "string before import = Test string

from my_module import string
print('variable "string" after import =', string)   # variable "string" after import = Hello World!
```

Можно, также, без разбора импортировать всё из модуля одним махом:

```python
from my_module import *
```

Это поместит имена всех объектов `my_module` в локальную таблицу имён, за исключением тех, которые начинаются с символа
подчеркивания (_).  
Не рекомендуется так поступать в крупномасштабном производственном коде. Это немного опасно, потому что вы массово 
вводите имена в локальную таблицу имён. Если вы не знаете их всех хорошо и не уверены, что конфликта не будет, у вас 
есть хороший шанс непреднамеренно перезаписать существующее имя. Однако этот синтаксис очень удобен, когда вы просто 
возитесь с интерактивным интерпретатором для целей тестирования или обнаружения, потому что он быстро дает вам доступ 
ко всему, что может предложить модуль, без большого набора текста.

### from <module_name> import <name> as <alt_name>

Также возможно импортировать отдельные объекты, но вводить их в локальную таблицу имён с альтернативными именами:

`from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]`

Это позволяет помещать имена непосредственно в локальную таблицу символов, но избегать конфликтов с ранее существующими 
именами:

```python
string = 'Test string'
print('variable "string before import =', string)   # variable "string before import = Test string

from my_module import string as string_1

print('variable "string" after import =', string)   # variable "string" after import = Test string
print('imported string is =', string_1)             # imported string is = Hello World!
```
 
### import <module_name> as <alt_name>

Также можете импортировать весь модуль под другим именем:

`import <module_name> as <alt_name>`

```python
import my_module as new_module

print(new_module.string)
```

Содержимое модуля может быть импортировано из определения функции. В этом случае `import` не выполнится, пока функция не
будет вызвана :

```python
def bar():
    lst = [1, 2, 3, 4, 5]
    from my_module import print_list
    print_list(lst)

bar()
```

Python3.x не допускает неопределённый `import *` внутри функции:

```python
def bar():
    lst = [1, 2, 3, 4, 5]
    from my_module import *
    print_list(lst)

bar()                                           # SyntaxError: import * only allowed at module level
```

Оператор `try ... except ImportError ... ` поможет избежать неудачных попыток импорта

```python
try:
    import tram_pam_pam
except ImportError:
    print("Import Error: Module wasn't find")
```

> Import Error: Module wasn't find

```python
try:
    from tram_pam_pam import purum_pum_pum
except ImportError:
    print("Import Error: Object wasn't find in the module")
```

> Import Error: Object wasn't find in the module

## Функция dir()

Встроенная функция `dir()` возвращает список определенных имен в пространстве имен. Без аргументов он возвращает 
отсортированный по алфавиту список имен в текущей таблице локальных имён:

```python
print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']
```

```python
some_list = [1, 2, 3, 4, 5, 6]
print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'some_list']
```

Обратите внимание, что при первом вызове `dir()` выше перечисляются несколько имен, которые автоматически определяются и
уже находятся в пространстве имен при запуске интерпретатора. Как только будут определны новые имена (some_list), они 
появляются на последующих вызовах `dir()`.  
Это может быть полезно для определения того, что именно было добавлено в пространство имен оператором import:

```python
print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

import my_module

print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'my_module']
```

```python
print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from my_module import string, print_list

print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'print_list', 'string']
```

Когда `dir()` передан аргумент, который является именем модуля, `dir()` перечисляются имена, определенные в модуле:

```python
import my_module

print(dir(my_module))
# ['__builtins__', ... '__package__', '__spec__', 'help',  'number', 'pi_number', 'print_list', 'some_list', 'string']
```

```python
print(dir())    # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from my_module import *

print(dir())
# ['__builtins__', ... '__package__', '__spec__', 'help',  'number', 'pi_number', 'print_list', 'some_list', 'string']
```

## Выполнение модуля как скрипта

Как было сказано выше: - "Любой фай с расширением .py - это мудуль.", так же справедливо и обратное: любой модуль 
является Python скриптом. А раз так, то он может быть выполнен.

```bash
$ python3 my_module.py
```

Там нет ошибок, так что, всё отработает корректно. Конечно, это не очень интересно. Он определяет только объекты. Но не
делать ничего с ними, и это не создает никакого вывода на экране.  
Немного изменим вышеприведенный модуль Python, чтобы он генерировал некоторый вывод при запуске в виде скрипта:

```python
# my_module.py

string = 'Hello World!'
number = 1234567
pi_number = 3.14

some_list = [4356, string, 'Test', 'a', pi_number]


def print_list(lst):
    for element in lst:
        print(element, end=' ')
    print()


class TestClass:
    pass


print('string =', string)
print('number =', number)
print('pi_number =', pi_number)
print('some_list =', some_list)
print_list(some_list)

test_class = TestClass()
print('test_class =', test_class)
```

Запустим повторно на исполнение данный модуль:

```bash
$ python3 my_module.py
```

> string = Hello World!  
> number = 1234567  
> pi_number = 3.14  
> some_list = [4356, 'Hello World!', 'Test', 'a', 3.14]  
> 4356 Hello World! Test a 3.14  
> test_class = <__main__.TestClass object at 0x104f10320>

Теперь попробуем снова **импортировать** данный модуль

```python
import my_module
```

> string = Hello World!  
> number = 1234567  
> pi_number = 3.14  
> some_list = [4356, 'Hello World!', 'Test', 'a', 3.14]  
> 4356 Hello World! Test a 3.14  
> test_class = <__main__.TestClass object at 0x104f10320>

Как ни странно, но при импорте также произошёл вывод данных, хотя мы не выполняли данный модуль как скрипт. Обычно 
модуль не генерирует выходные данные при импорте. В чём же дело?  
Всё дело в том что импортируя модуль, Python его исполняет. Как же сделать так, чтоб при импорте не выполнялся тот код, 
что нам нужно выполнять при запуске скрипта?  
Сделать это довольно просто. Каждый модуль имеет атрибут `__name__`. Если модуль запускается как скрипт, то это атрибут
имеет значение `__main__`, но если модуль ипортируется, то атрибут будет содержать имя этого модуля. Этим можно 
воспользоваться при написании скрипта.

```python
# my_module.py

string = 'Hello World!'
number = 1234567
pi_number = 3.14

some_list = [4356, string, 'Test', 'a', pi_number]


def print_list(lst):
    for element in lst:
        print(element, end=' ')
    print()


class TestClass:
    pass


if __name__ == '__main__':
    print('string =', string)
    print('number =', number)
    print('pi_number =', pi_number)
    print('some_list =', some_list)
    print_list(some_list)
    
    test_class = TestClass()
    print('test_class =', test_class)
```

Теперь при запуске скрипта получим:

> string = Hello World!  
> number = 1234567  
> pi_number = 3.14  
> some_list = [4356, 'Hello World!', 'Test', 'a', 3.14]  
> 4356 Hello World! Test a 3.14  
> test_class = <__main__.TestClass object at 0x104f10320>

как и ожидалось, а при импорте - нет.

Модули часто разрабатываются с возможностью запуска в качестве отдельного сценария для тестирования функциональности, 
содержащейся в модуле. Это называется модульным тестированием. Например, предположим, что вы создали модуль, `fact.py`
содержащий функцию вычисления факториала:

```python
# fact.py

def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
```

Теперь файл можно рассматривать как модуль, и импортировать функцию `fact()`:

```python
from fact import fact

print(fact(5))                                  # 120
```

и этот же файл, можно запустить самостоятельно

```bash
$ python3 fact.py 5
```

> 120

## Перезагрузка модуля

Из соображений эффективности модуль загружается только один раз за сеанс интерпретатора. Это хорошо для определений 
функций и классов, которые обычно составляют основную часть содержимого модуля. Но модуль также может содержать 
исполняемые операторы, обычно для инициализации. Помните, что эти операторы будут выполняться только при первом импорте 
модуля.

```python
# test_mod.py

x = [1, 2, 3, 4, 5]

print('x =', x)
```

при первом импорте вы увидем:

```python
import test_mod                                 # x = [1, 2, 3, 4, 5]
import test_mod
import test_mod
import test_mod
```

при последующих, вывода не будет.

Если вы вносите изменения в модуль и вам необходимо его перезагрузить, вам нужно либо перезапустить интерпретатор, 
либо воспользоваться функцией `reload()` из модуля `importlib`:

```python
import test_mod                                 # x = [1, 2, 3, 4, 5]
import test_mod
import test_mod
import importlib

importlib.reload(test_mod)                      # x = [1, 2, 3, 4, 5]
```




