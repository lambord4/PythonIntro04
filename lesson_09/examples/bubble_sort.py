from random import randint


def bubble_sort(lst, direction=True):
    cnt_of_iter = 0
    for i in range(len(lst) - 1):
        flag = True
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1] if direction else lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False

        cnt_of_iter += 1
        if flag:
            break

    print(cnt_of_iter)


l = [randint(1, 100) for _ in range(20)]
print(l)
bubble_sort(l)
print(l)

l = [randint(1, 100) for _ in range(20)]
print(l)
bubble_sort(l, False)
print(l)
