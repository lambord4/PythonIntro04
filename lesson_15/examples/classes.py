
"""
class <NAME>(<Base class>):
    pass
"""


class Point:
    X = 5
    Y = 8

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_res(self):
        return self.x + self.__class__.X

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


pt1 = Point(4, 8)
print(id(pt1))
# print(pt1.x, pt1.y)
print(pt1.get_x(), pt1.get_y())
pt2 = Point(1, 2)
# print(pt2.x, pt2.y)
print(id(pt2))
# pt1.x = 7
# print(pt1.x, pt1.y)
print('attr of class X:', Point.X)
print('result pt1:', pt1.get_res())
print('result pt2:', pt2.get_res())
Point.X = 6
print('attr of class X:', Point.X)
print('result pt1:', pt1.get_res())
print('result pt2:', pt2.get_res())

print(str(pt1))

print(pt1 + pt2)
res = pt1 + pt2
pt3 = Point(res[0], res[1])
print(pt3)
