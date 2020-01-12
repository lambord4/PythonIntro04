# Пакеты

Предположим, вы разработали очень большое приложение, которое включает в себя множество модулей. По мере роста 
количества модулей становится трудно отслеживать их все, если они выбрасываются в одно место. Это особенно верно, если 
они имеют похожие имена или функциональность. Всё это вызывает необходимость средства группировки и организации модулей.  
Пакеты допускают иерархическое структурирование пространства имен модуля с использованием точечной нотации. Точно так 
же, как модули помогают избежать коллизий между именами глобальных переменных, пакеты помогают избежать коллизий между 
именами модулей.  

## Создание пакета

Создать пакет довольно просто, поскольку он использует внутреннюю иерархическую структуру файлов операционной системы. 

![pkg1](img/pkg1.png)

На изображении представлен пакет с двумя модулями в нём.

```python
# mod1.py

def foo():
    print('[mod1] foo()')

class Foo:
    def __init__(self):
        pass
```

```python
# mod2.py

def bar():
    print('[mod2] bar()')

class Bar:
    def __init__(self):
        pass
```

Учитывая эту структуру, если `pkg` каталог находится в том месте, где его можно найти (в одном из каталогов, 
содержащихся в нем `sys.path`), вы можете ссылаться на два модуля с точечной нотацией (`pkg.mod1`, `pkg.mod2`) и 
импортировать их с синтаксисом, с которым вы уже знакомы:

`import <module_name>[, <module_name> ...]`

```python
import pkg.mod1, pkg.mod2

pkg.mod1.foo()                                  # [mod1] foo()
x = pkg.mod2.Bar()
print(x)                                        # <pkg.mod2.Bar object at 0x10e4db350>
```

`from <module_name> import <name(s)>`

```python
from pkg.mod1 import foo
foo()                                           # [mod1] foo()
```

`from <module_name> import <name> as <alt_name>`

```python
from pkg.mod2 import Bar as Qux

x = Qux()
print(x)                                        # <pkg.mod2.Bar object at 0x10e4db350>
```

также можно импортировать модули с этими операторами:

`from <package_name> import <modules_name>[, <module_name> ...]`  
`from <package_name> import <module_name> as <alt_name>`

```python
from pkg import mod1
mod1.foo()                                      # [mod1] foo()

from pkg import mod2 as quux
quux.bar()                                      # [mod2] bar()
```

Технически есть возможность импортировать пакет:

```python
import pkg

print(pkg)                                      # <module 'pkg' (namespace)>
```

Но это мало что дает. Хотя, строго говоря, это синтаксически правильный оператор Python, он не делает ничего полезного.
В частности, он не помещает ни один из модулей из `pkg` локальное пространство имен:

```python
import pkg

print(pkg.mod1)                                 # AttributeError: module 'pkg' has no attribute 'mod1'
pkg.mod1.foo()                                  # AttributeError: module 'pkg' has no attribute 'mod1'
pkg.mod2.Bar()                                  # AttributeError: module 'pkg' has no attribute 'mod2'
```

Чтобы фактически импортировать модули или их содержимое, вам нужно использовать одну из форм, показанных выше.

## Инициализация пакета

Если указанный файл `__init__.py` присутствует в каталоге пакета, он вызывается при импорте пакета или модуля в пакете.
Это может использоваться для выполнения кода инициализации пакета, такого как инициализация данных уровня пакета.

Добавим в пакет `pkg` следующий `__init__.py` файл:

```python
print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']
```

![pkg2](img/pkg2.png)

Теперь, когда пакет импортирован, глобальный список `A` инициализируется и можно получить к нему доступ:

```python
import pkg                                      # Invoking __init__.py for pkg

print(pkg.A)                                    # ['quux', 'corge', 'grault']
```

Модуль в пакете может получить доступ к пространству имён пакета если импортирует его:

```python
# mod1.py

def foo():
    from pkg import A
    print('[mod1] foo() / A =', A)

class Foo:
    def __init__(self):
        pass
```

```python
from pkg import mod1                            # Invoking __init__.py for pkg

mod1.foo()                                      # [mod1] foo() / A = ['quux', 'corge', 'grault']
```

`__init__.py` также может использоваться для автоматического импорта модулей из пакета. Например, ранее вы видели, что 
оператор `import pkg` помещает только имя `pkg` в таблицу локальных имён вызывающей стороны и не импортирует никакие 
модули. Но если в `__init__.py` пакета `pkg` поместить следующий код:

```python
import pkg.mod1
import pkg.mod2

print(f'Invoking __init__.py for {__name__}')

A = ['quux', 'corge', 'grault']
```

то можно будет получить доступ к модулььям пакета при импорте только самого пакета:

```python
import pkg                                      # Invoking __init__.py for pkg

pkg.mod1.foo()                                  # [mod1] foo() / A = ['quux', 'corge', 'grault']
pkg.mod2.bar()                                  # [mod2] bar()
```

> Примечание. Большая часть документации Python гласит, что `__init__.py` файл должен присутствовать в каталоге пакета 
> при создании пакета. Это когда-то было правдой. Раньше было то, что само присутствие `__init__.py` означало для Python 
> определение пакета. Файл может содержать код инициализации или даже быть пустым, но он должен присутствовать.  
> Начиная с `Python 3.3` , были представлены [неявные пространства имен пакетов](https://www.python.org/dev/peps/pep-0420/).
> Они позволяют создавать пакеты без каких-либо `__init__.py` файлов. Конечно, он все еще может присутствовать, если 
> требуется инициализация пакета. Но это больше не является требованием.

## import * из пакета

Пакет имеет следующую структуру:

![pkg3](img/pkg3.png)

добавим модули `mod3.py` и `mod4.py`

```python
# mod3.py

def baz():
    print('[mod3] baz()')

class Baz:
    def __init__(self):
        pass
```

```python
# mod4.py

def qux():
    print('[mod4] qux()')

class Qux:
    def __init__(self):
        pass
```

Когда выполняется `import *` все объекты из модуля импортируются в локальную таблицу имён, кроме тех, чьи имена 
начинаются с подчеркивания:

```python
print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from pkg.mod3 import *
dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'baz']

print(baz())                                    # [mod3] baz()
print(Baz)                                      # <class 'pkg.mod3.Baz'>
```

Аналогичное утверждение для пакета:

`from <package_name> import *`

```python
print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from pkg import *
dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']
```

Как ни странно, но ничего не произошло. Казалось бы Python загрузит все модули из пакета, что сможет найти. Почему не 
так?  
Python загрузит только те модули имено которых есть в `__init__.py` файле в переменной с именем `__all__`, он считается 
списком модулей, которые следует импортировать при обнаружении оператора `from <package_name> import *`.  
Добавим в `__init__.py` следующий код:

```python
__all__ = ['mod1', 'mod2', 'mod3', 'mod4']
```

Теперь `from pkg import *` импортирует все четыре модуля:

```python
print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from pkg import *
dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'mod1', 'mod2', 'mod3', 'mod4']

mod2.bar()                                      # [mod2] bar()
print(mod4.Qux)                                 # <class 'pkg.mod4.Qux'>
```

Использование `import *` не считается хорошей практикой, для пакетов, так же как и для модулей. Но эта возможность, по 
крайней мере, дает создателю пакета некоторый контроль над тем, что происходит, когда `import *` указано. (На самом 
деле, он предоставляет возможность полностью запретить его, просто отказавшись `__all__` вообще его определять. Как вы 
уже видели, поведение пакетов по умолчанию - ничего не импортировать.)  
Кстати, также `__all__` может быть определен в модуле и служит той же цели: контролировать то, что импортируется 
`import *`. Например, измените `mod1.py` следующим образом:

```python
# mod1.py

__all__ = ['foo']

def foo():
    from pkg import A
    print('[mod1] foo() / A =', A)


class Foo:
    def __init__(self):
        pass
```

Теперь `import *` оператор `from pkg.mod1` будет импортировать только то, что содержится в `__all__`:

```python
print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help']

from pkg.mod1 import *
print(dir())
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'help', 'foo']
```

`foo()` (функция) теперь определена в локальном пространстве имен, но `Foo` (класс) нет, потому что последний не 
находится в `__all__`.  
Таким образом, `__all__` используется как пакетами, так и модулями для контроля того, что импортируется, когда 
`import *` указано. Но поведение по умолчанию отличается :
- Для **пакета**, когда `__all__` он не определен, `import *` ничего не импортируется.
- Для **модуля**, когда `__all__` он не определен, `import *` импортируется все (кроме, как вы уже догадались, имен, 
начинающихся с подчеркивания).

## Sub пакеты (дочерние пакеты)

Пакеты могут содержать вложенные подпакеты произвольной глубины. Рассмотрим следующую структуру пакетов:

![pkg4](img/pkg4.png)

Четыре модуля (`mod1.py`, `mod2.py`, `mod3.py` и `mod4.py`) определены как и ранее. Но теперь, вместо того, чтобы 
объединить их в `pkg` каталог, они разделены на два каталога подпакетов, `sub_pkg1` и `sub_pkg2`.  
Импорт по-прежнему работает так же, как показано ранее. Синтаксис аналогичен, но дополнительная точечная нотация 
используется для отделения имени пакета от имени подпакета :

```python
import pkg.sub_pkg1.mod1                        # Invoking __init__.py for pkg
pkg.sub_pkg1.mod1.foo()                         # [mod1] foo() / A = ['quux', 'corge', 'grault']

from pkg.sub_pkg1 import mod2
mod2.bar()                                      # [mod2] bar()

from pkg.sub_pkg2.mod3 import baz
baz()                                           # [mod3] baz()

from pkg.sub_pkg2.mod4 import qux as tux
tux()                                           # [mod4] qux()
```

Кроме того, модуль в одном подпакете может ссылаться на объекты в дочернем подпакете (в том случае, если в нем есть 
некоторые необходимые вам функции). Например, предположим, что вы хотите импортировать и выполнить функцию `foo()`
(определенную в модуле `mod1`) из модуля `mod3`. Можно использовать абсолютный импорт:

```python
# mod3.py
from pkg.sub_pkg1.mod1 import foo

def baz():
    print('[mod3] baz()')

class Baz:
    def __init__(self):
        pass

foo()
```

```python
from pkg.sub_pkg2 import mod3                   # Invoking __init__.py for pkg
                                                # [mod1] foo() / A = ['quux', 'corge', 'grault']
mod3.foo()                                      # [mod1] foo() / A = ['quux', 'corge', 'grault']
```

Или вы можете использовать относительный импорт, где `..` относится к пакету на один уровень выше. Изнутри `mod3.py`, 
который находится в подпакете `sub_pkg2`
- `..` вычисляет родительский пакет (`pkg`), и
- `..sub_pkg1` вычисляет подпакет `sub_pkg1` родительского пакета.

```python
# mod4.py

from .. import sub_pkg1
print(sub_pkg1)

from ..sub_pkg1.mod1 import foo
foo()


def qux():
    print('[mod4] qux()')


class Qux:
    def __init__(self):
        pass
```

```python
from pkg.sub_pkg2 import mod4
```

> Invoking __init__.py for pkg  
> <module 'pkg.sub_pkg1' (namespace)>  
> [mod1] foo() / A = ['quux', 'corge', 'grault']  

