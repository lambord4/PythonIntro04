class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 150 < age or age <= 0:
            self.__age = 25
        else:
            self.__age = age

    def display_info(self):
        print('Name:', self.__name, '\tAge:', self.__age)

    def __str__(self):
        return 'Person'


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        super().display_info()
        print('Company:', self.company)


class Parent:
    def __init__(self):
        pass

    def __str__(self):
        return 'Parent'


class Student(Person, Parent):
    def __str__(self):
        return super().__str__()

    def __init__(self, name, age, university):
        # super().__init__(name, age)
        Person.__init__(self, name, age)
        self.university = university

    def display_info(self):
        print('Student:', self.name, 'university:', self.university)


# people = [Person('Tom', 25), Student('Bob', 19, 'Harvard'), Employee('Sam', 35, 'Google')]
# for person in people:
#     person.display_info()
#     print()

st = Student('Bob', 19, 'Harvard')
print(st)
