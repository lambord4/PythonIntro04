# Property

Вычисляемое» свойство или **property**.

```
property([fget[, fset[, fdel[, doc]]]])
```

- `fget` - Функция, реализующая возврат значения свойства.
- `fset` - Функция, реализующая установку значения свойства.
- `fdel` - Функция, реализующая удаление значения свойства.
- `doc` - Строка документации для создаваемого свойства. 

Позволяет использовать методы в качестве свойств объектов — порождает дескриптор, позволяющий создавать «вычисляемые» 
свойства (тип property).

```python
class Mine(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __get_x(self):
        return self.__x

    def __get_y(self):
        return self.__y

    def __set_x(self, value):
        self.__x = value

    def __set_y(self, value):
        self.__y = value

    def __del_x(self):
        self.__x = 0

    def __del_y(self):
        self.__y = 0

    x = property(__get_x, __set_x, __del_x, 'Это свойство x.')
    y = property(__get_y, __set_y, __del_y, 'Это свойство y.')


print('property x:', type(Mine.x))
print('property y:', type(Mine.y))
print('----------------')
mine = Mine(4, 8)
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
mine.x = 3
mine.y = 5
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
del mine.x
del mine.y
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
```

```
property x: <class 'property'>
property y: <class 'property'>
----------------
x = 4
y = 8
----------------
x = 3
y = 5
----------------
x = 0
y = 0
----------------
```

Тот же эффект можно получить использую декоратор `@property`

```python
class Mine(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @x.deleter
    def x(self):
        self.__x = 0

    @y.deleter
    def y(self):
        self.__y = 0

mine = Mine(4, 8)
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
mine.x = 3
mine.y = 5
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
del mine.x
del mine.y
print('x =', mine.x)
print('y =', mine.y)
print('----------------')
```

```
x = 4
y = 8
----------------
x = 3
y = 5
----------------
x = 0
y = 0
----------------
```