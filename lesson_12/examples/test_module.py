import old_students.lesson_12.my_module
# import msvcrt

print(old_students.lesson_12.my_module.number)

print(old_students.lesson_12.my_module.__file__)
# print(msvcrt.__file__)

k = old_students.lesson_12.my_module.number

print(old_students.lesson_12.my_module)
# print(number)

string = 'Test string'
print(string)

from old_students.lesson_12.my_module import string, number, print_list

print(string)

import old_students.lesson_12.my_module as m_mod

print(m_mod.number)

from old_students.lesson_12.m1 import num as num1, string as string1
from old_students.lesson_12.m2 import num as num2, string as string2

print(num1, string1)
print(num2, string2)
