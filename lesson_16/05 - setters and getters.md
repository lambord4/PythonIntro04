

```python
class Mine(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    def del_x(self):
        self.__x = 0

    def del_y(self):
        self.__y = 0


mine = Mine(4, 8)
print('x =', mine.get_x())
print('y =', mine.get_y())
print('----------------')
mine.set_x(3)
mine.set_y(5)
print('x =', mine.get_x())
print('y =', mine.get_y())
print('----------------')
mine.del_x()
mine.del_y()
print('x =', mine.get_x())
print('y =', mine.get_y())
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