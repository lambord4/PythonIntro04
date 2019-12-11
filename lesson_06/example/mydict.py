from pprint import pprint

team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

print(team)
print(team['Colorado'])
team['Colorado'] = 'Spartak'
print(team)
team['Kiev'] = 'Dinamo'
pprint(team)

P = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
}

print(P[1])

# p = {
#     [1, 5]: 'r'
# }

# print(p)

d = {'a': 10, 'b': 20, 'c': 30}
print(d)                                        # {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))                               # 20
print(d.get('z', 0))