
min_value = 0
max_value = 0
cnt = 0

while True:
    x = int(input("Enter value "))
    if x == 0:
        break

    cnt += 1

    if cnt == 1:
        min_value = x
        max_value = x
        continue

    if min_value > x:
        min_value = x


