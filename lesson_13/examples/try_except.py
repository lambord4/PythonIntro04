x = 4
y = 0
i = input()
# print('Результат деления:', x / y)

try:
    print('Результат деления:', x / y)
# except Exception as ex:
#     pass
except ZeroDivisionError as ex:
    print(ex)
except OverflowError:
    pass
except FloatingPointError as ex:
    pass
