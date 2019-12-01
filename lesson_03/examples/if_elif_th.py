x = 0

if x == 0:
    print('Yes')
else:
    print('No')


print('Yes') if x == 0 else print('No')

print('No') if x else print('Yes')

print('No' if x else 'Yes')

# x / y = z

y = 56

z = (x / y if y else x)
