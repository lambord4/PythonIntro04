book_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

res = list(map(lambda x: (x[0], round(x[2]*x[3] if x[2]*x[3] > 100 else x[2]*(x[3]+10), 2)), book_list))
print(res)


# def f(var):
#     return var * 2
#
#
# for line in book_list:
#     f(line)
#
#
# lambda x, y, z: x + y * z
#
# lambda var: var * 2