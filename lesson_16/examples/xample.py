
class Point:
    def __init__(self, x=0, y=0):
        self.name = '{} - {}'.format(x, y)
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'x = {}, y = {}'.format(self.__x, self.__y)

    def print_point(self):
        print('x = {}, y = {}'.format(self.__x, self.__y))

    def set_x(self, x):
        self.__x = abs(x)

    def get_x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    # y = property(get_y, set_y)


class Figure:
    def __init__(self, name):
        self.__name = name
        self.__picks = []

    def add_point(self, pt):
        if pt:
            self.__picks.append(pt)

    def print_fig(self):
        # print(self.__picks[0].name)
        for pt in self.__picks:
            name = pt.name
            x = pt.get_x()
            y = pt.y
            print('name = {}\tx = {}, y = {}'.format(name, x, y))


pt1 = Point(4, 6)
print(pt1)
# pt1.a = 8
# pt1.b = 1
# print(pt1)
# print(pt1.a, pt1.b)
print('prop x =', pt1.x, 'prop y=', pt1.y)
pt1.x = -8
pt1.y = -3
print('prop x =', pt1.x, 'prop y=', pt1.y)
pt2 = Point(5, 1)
pt2.print_point()
pt3 = Point(8, 7)
pt4 = Point()
pt5 = Point(2, 9)

fig = Figure('Name Fig')
fig.add_point(pt1)
fig.add_point(pt2)
fig.add_point(pt3)
fig.add_point(pt4)
fig.add_point(pt5)

fig.print_fig()
