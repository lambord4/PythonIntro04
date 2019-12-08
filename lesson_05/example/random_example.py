from random import randint
from random import random
from random import randrange
from random import uniform

# randrange
for _ in range(15):
    print(randrange(1, 10, 1), end=', ')  # 9, 2, 6, 8, 3, 1, 3, 8, 9, 6, 4, 5, 9, 6, 6,
print()
# randint
for _ in range(15):
    print(randint(-10, 10), end=', ')  # 6, 9, 7, 7, 9, 1, 8, 10, 9, 3, 8, 7, 2, 6, 6,
print()
# random
for _ in range(15):
    print(random(), end=', ')  # 0.9443671834761455, 0.38034154533465947, ... 0.7436994817447609,
print()
# uniform
for _ in range(15):
    print(uniform(0.1, 9.9), end=', ')  # 0.5624438314821778, 9.382460634537614, ... 1.3733203890245438,
print()