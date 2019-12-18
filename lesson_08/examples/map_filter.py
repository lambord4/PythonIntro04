from random import randint

def fahrenheit(temperature):
    return round(((float(9)/5)*temperature + 32), 2)


def celsius(temperature):
    return round((float(5)/9)*(temperature-32), 2)


temperatures = (36.5, 37, 37.5, 38, 39)

res = []
for el in temperatures:
    res.append(fahrenheit(el))

res = tuple(res)
print(res)

res1 = []
for el in res:
    res1.append(celsius(el))

res1 = tuple(res1)
print(res1)

res_map = tuple(map(fahrenheit, temperatures))
print(type(res_map))
print(res_map)

res_map = tuple(map(celsius, res_map))
print(res_map)

C = [39.2, 36.5, 37.3, 38, 37.8]

F = list(map(lambda x: round((float(9)/5)*x + 32, 2), C))
print(F)                                        # [102.56, 97.7, 99.14, 100.4, 100.04]

C = list(map(lambda x: round((float(5)/9)*(x-32), 2), F))
print(C)

print('-' * 150)

lst = [randint(0, 100) for _ in range(20)]
print(lst)                                      # [8, 44, 25, 64, 15, 55, 14, 10, 56, 7, 87, 89, 44, 69, 18]

odd_numbers = list(filter(lambda x: x % 2, lst))
print(odd_numbers)                              # [25, 15, 55, 7, 87, 89, 69]

even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)                             # [8, 44, 64, 14, 10, 56, 44, 18]

# alternatively
even_numbers = list(filter(lambda x: x % 2-1, lst))
print(even_numbers)                             # [8, 44, 64, 14, 10, 56, 44, 18]