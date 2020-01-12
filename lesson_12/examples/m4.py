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


x = [1, 2, 3, 4, 5, 6]

print('x =', x)

if __name__ == '__main__':
    print('string =', string)
    print('number =', number)
    print('pi_number =', pi_number)
    print('some_list =', some_list)
    print_list(some_list)

    test_class = TestClass()
    print('test_class =', test_class)


# print(__name__)
