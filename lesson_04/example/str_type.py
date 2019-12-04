s = 'Срезы используются ля получения подстроки из строки.'
print(s[0])
print(s[-5])

# start:stop:step
print(s[0:5])
print(s[:5])
print(s[-7:])
print(s[-6750602846520478678045650:16587465823450856843])
print(s[::2])
print(s[::-1])
print(s[::])

S = 'Hello'
print(S.find('e'))      # 1
print(S.find('l'))     # 2
print(S.find('L'))      # -1

# s[2] = 'Y'

print('Hello'.replace('l', 'L'))
print('Abrakadabra'.replace('a', 'A', 2))

print('Abracadabra'.count('a'))             # 4
print(('a' * 10).count('aa'))

print(s.split('о', 1))

