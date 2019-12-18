# def compare(a, b):
#     if a > b:
#         return 1
#     elif a < b:
#         return -1
#     else:
#         return 0
#
#
# x = compare
#
# k = 4
# l = 8
# print(x(k, l))


def list_compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def dict_compare(a, b):
    if len(str(list(a.values())[0])) > len(str(list(b.values())[0])):
        return 1
    elif len(str(list(a.values())[0])) < len(str(list(b.values())[0])):
        return -1
    else:
        return 0


def comparing(collection, comparator):
    i = iter(collection)
    try:
        while True:
            d1 = next(i)
            d2 = next(i)
            if comparator(d1, d2) == 0:
                print(f'{d1} == {d2}')
            else:
                print(f'{d1} <> {d2}')
    except StopIteration as ex:
        print('End of collection')


lst = [2, 5, 3, 3, 4, 3, 3, 2, 1, 1]
dic = [{'type': 'lorry'}, {'model': 'IVECO'}, {'length': 25.7}, {'weight': 8500.1}]

comparing(lst, list_compare)
comparing(dic, dict_compare)