import old_students.lesson_12.m4
from msvcrt import getch
import importlib

while True:
    ch = getch()
    if ord(ch) == 32:
        print("Reload")
        importlib.reload(old_students.lesson_12.m4)
