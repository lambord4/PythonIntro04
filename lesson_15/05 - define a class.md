# Создание классов и их объектов

## Создание класса
Синтаксис объявления класса довольно прост. 

```
class NameCalss[(parent1, parent2, ... parentN)]:
    body of this class
```

Для объявления класса необходимо использовать ключевое слово `class` за которым идёт обязательное имя класса. Желательно
чтоб имя сласса отражало назначение этого класса. Например, класс описывающий человека, можно было бы назвать `Human`. 
Для написания имени класса используется [`CammalCaseStyle`](https://en.wikipedia.org/wiki/Camel_case).  
За именем класса может следовать, в круглых скобках, имена классов родителей перечисленых через запятую. Если родителей 
нет, круглые скобки можно не писать вообще.  
Далее идёт обязательный элемент `:` двоеточие, завершающее заголовок класса.  
Тело класса описывается с отступом (обычно это четыре пробела) от уровня описания (то есть от уровня имени) этого 
класса.  
Тело класса может содержать различные переменные - **атрибуты класса или свойства класса**, которые определяют состояние
будущих объектов и функции - **методы класса**, которые будут определять поведение объектов.  
Например для описания человека, можно создать следующий класс:

```python
class Human:
    type = 'mammal'
    age = 25
    height = 189
    weight = 87
    phone = '555-66-77'
    address = 'Odessa'
```

Если, какой-то, класс наследуется от класса `Human`, то он будет описан следующим образом:

```python
class Child(Human):
    pass
```

## Создание объекта

Инстанцирование - означает создать объект класса. Например, для класса `Point` мы уже создавали объекты. Попробуем ещё 
раз:

```python
class Point:
    pass


pt_1 = Point()
print('pt_1 is:', id(pt_1))
pt_2 = Point()
print('pt_2 is:', id(pt_2))
```

Чтоб создать экземпляр класса (или объект класса, или инстанс класса) необходимо использовать имя класса за которым
следуют круглые скобки.

Для доступа к методам и атрибутам объекта используется следующий синтаксис:

```
obj_name.attribute
obj_name.method()
```

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(self.x, self.y)


pt = Point(3, 4)

print(pt.x)                                     # 3
print(pt.y)                                     # 4
pt.print_point()                                # 3 4
```

## Атрибуты класса и экземпляра

Каждый класс, каждый экземпляр могут содержать атрибуты, к которым мы можем обращаться. Например, класс описывающий 
точку на плоскости должен иметь как минимум два атрибута экземпляра класса: координаты `x` b `y`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Так же, в качестве атрибутов экземпляра класса могут быть использованы объекты других классов:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self):
        self.peak_1 = Point(0, 0)
        self.peak_2 = Point(1, 1)
        self.peak_3 = Point(2, 2)
```

Переменные `x` и `y` в методе `__init__` класса `Point`, к которым мы обращаемся через `self`, являются атрибутами 
экземпляра класса и у каждого экземпляра они могут хранить разные значения, тем самым определяя разные состояния 
экземпляра. Класс так же может иметь свои атрибуты и они будут общими для всех экземпляров данного класса:

```python
class Point:
    type = 'attribute of class'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 'attribute of instance'


pt = Point(3, 4)

print(pt.type)                                  # attribute of instance
print(Point.type)                               # attribute of class

pt.type = 'pt.type'
Point.type = 'Point.type'

print(pt.type)                                  # pt.type
print(Point.type)                               # Point.type

pt2 = Point(5, 6)

print(pt2.type)                                 # attribute of instance
print(Point.type)                               # Point.type
```

Чтоб получить доступ из экземпляра к атрибутам класса необходимо воспользоваться атрибутом `__class__`

```python
class SomeClass:
    name = 'test'

    def get_class_attr(self):
        return self.__class__.name


print(SomeClass().get_class_attr())             # test
```

Атрибут класса и атрибут объекта/инстанса/экземпляра - разные вещи. Это демострирует код примера, приведённый выше.

В методе `__init__`, в качестве одного из мареметров использует `self`. Это общепринятое имя для ссылки на объект, в 
контексте которого вызывается данный метод. Это обязательный параметр для методов класса. У обычных функций, такого 
параметра нет.  

Так же, любой класс, по умолчанию, содержит несколько обязательных атрибутов:

- `__dict__` - словарь хранящий пространство имён класса
- `__doc__`  - doc-string класса. Может быть пустым если doc-string не был определён
- `__name__` - имя класса
- `__module__` - имя модуля в котором определён данный класс
- `__bases__` - кортеж содержащий имена базовых классов, в порядке их появления в списке базовых классов), для текущего 
класса. Если класс не имеет родителей, кортеж будет пустой

```python
class Person:
    """ Class - Person """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Return of name of the Person instance
        :return:
        """
        return self.name


print('__doc__: {}'.format(Person.__doc__))
print('__name__: {}'.format(Person.__name__))
print('__module__: {}'.format(Person.__module__))
print('__bases__: {}'.format(Person.__bases__))
print('__dict__:')
for key, value in Person.__dict__.items():
    print('\t', key, ':', value)
``` 

и вывод

```
__doc__:  Class - Person 
__name__: Person
__module__: __main__
__bases__: (<class 'object'>,)
__dict__:
	 __module__ : __main__
	 __doc__ :  Class - Person 
	 __init__ : <function Person.__init__ at 0x10cd29b70>
	 get_name : <function Person.get_name at 0x10cd29bf8>
	 __dict__ : <attribute '__dict__' of 'Person' objects>
	 __weakref__ : <attribute '__weakref__' of 'Person' objects>
```

### Example 1
> Условие: Создать класс `Human` с двумя атрибутами экземплята: `name` и `age`. При создании объекта, необходимо, ему 
> (объекту) сообщать имя и возраст создаваемого человека.  
> Написать отдельную функцию которая принимает любое количество экземпляров класса `Human` и возвращает имя и возраст
> наистарейшего человека. Если таких несколько, вернуть первого.

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_biggest_number(*args):
    age = args[0].age
    name = args[0].name
    for human in args:
        if human.age > age:
            age = human.age
            name = human.name

    return name, age


h1 = Human('Ivan', 37)
h2 = Human('Petr', 25)
h3 = Human('Sidor', 56)
h4 = Human('Dinis', 18)
h5 = Human('Olga', 15)


print(get_biggest_number(h1, h2, h3, h4, h5))
```

## Методы экземпляра 

**Методы экземпляра** - ото обычные функции, у которых есть один обязательный аргумент - `self`. О нём говорилось выше.
Эти методы позволяют организовать интерфейс взаимодействия с этими экземплярами их поведение, а так же могут быть 
использованы для внутрених целей объектов.  
Например, класс `Point` может содержать метод `move()` который смещает точку на новые координаты относительно текущих:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
```

Этот метод определяет как будет вести себя объект при её вызове (какое состояние примет объект, после её вызова).

## Динамическое изменение класса

Есть пустой класс:

```python
class SomeClass:
    pass
```

Казалось бы, что от него толку? Но им тоже можно пользоваться, динамически наполняя (строя) такой класс

```python
class SomeClass:
    pass

def square_method(self):
    return self.x ** 2

def init(self, x):
    self.x = x

SomeClass.new_attr = 45
SomeClass.init = init
SomeClass.square = square_method
obj = SomeClass()
obj.init(3)
print(obj.square())                             # 9
print(obj.new_attr)                             # 45
```

## Статические методы и методы класса

Для описания `статического метода` используется специальный декоратор `@staticmethod`. Статический метод не имеет 
обязательного параметра `self` и доступен как из класса так и из экземпляра класса.

```python
class SomeClass:
    @staticmethod
    def foo():
        print('This is "foo" function!')


SomeClass.foo()                                 # This is "foo" function!

obj = SomeClass()
obj.foo()                                       # This is "foo" function!
```

Такой метод выглядит как обычная функция - только с той разницей, что он определён внутри класса и может быть вызван из 
этого класса или из его объекта. `@staticmethod` определяет обычную функцию в пространстве имён класса. Может быть 
полезно для вспомогательных функций, чтобы не мусорить пространство имён модуля. Они ничего не знают о классе, в котором
определены, и его экземплярах. Таким образом, статические методы прикреплены к классу лишь для удобства и не могут 
менять состояние ни класса, ни его экземпляра.

Для описания метода класса необходим декоратор `@classmethod`. Метод класса принимает, в качестве обязательного 
параметра, ссылку на класс, в котором он определён, и обозначается как `cls`. Эта ссылка указывает на класс, а не на 
экземпляр этого класса.

```python
class SomeClass:
    @classmethod
    def hello(cls):
        print('Привет из класса: {}'.format(cls.__name__))


SomeClass.hello()                               # Привет из класса SomeClass
```

Методы класса могут менять состояние класса, что отразится на всех объектах этого класса, но не могут менять конкретный 
экземпляр. Чаще всего метод класса используется тогда, когда нужен генерирующий метод, возвращающий объект класса.

```python
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        """
            Return instance of Prson from birthday's year
        """
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('Sveta', 25)
person2 = Person.from_birth_year('Ivan', 1981)

print(person1.name, person1.age)                # Sveta 25
print(person2.name, person2.age)                # Ivan 38
print(Person.is_adult(25))                      # True
```

### Некоторые выводы

- Методы экземпляра класса получают доступ к объекту класса через параметр `self` и к классу через `self.__class__`.
- Методы класса не могут получить доступ к определённому объекту класса, но имеют доступ к самому классу через `cls`.
- Статические методы работают как обычные функции, но принадлежат области имён класса. Они не имеют доступа ни к самому 
классу, ни к его экземплярам.

## Конструирование объекта класса

В жизненом цикле объекта класса участвуют три "магических" метода: `__new__(cls)`, `__init__(self)` и `__del__(self)`.

```python
class Person:
    def __new__(cls, *args, **kwargs):
        print('Into method __new__')
        return super(Person, cls).__new__(cls)

    def __init__(self, x):
        self.x = x
        print('Into method __init__')

    def __del__(self):
        print('Into method __del__')


p1 = Person(2)
```

Метод `__new__(cls)` - непосредственно создаёт и возвращает новый экземпляр класса. В этом методе можно контролировать 
процесс создания экземпляра, если в этом есть необходимость.  
Метод `__init__(self)` - производит инициализацию созданного экземпляра. На самом деле, для создания и инициализации 
экземпляра класса достаточно переопределить только метод `__init__(self)`.  
Метод `__del__(self)` - является деструктор класса и вызывается непосредственно перед разрушением экземпляра класса. 
Деструктор нужен для явного освобождения ресурсов которые были получены в экземпляре: открытый файл или сокет. Им
редко пользуются, так как нет гарантии что экземпляр будет разрушен сразу же как только счётчик ссылок станет равен 0.
Решение о разрушении объекта принимает [**garbage collector**](https://ru.wikipedia.org/wiki/Сборка_мусора). О 
сборщике мусора в Python можно почитать [здесь](https://habr.com/ru/post/417215/).
