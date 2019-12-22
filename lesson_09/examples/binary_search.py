

def binary_search(lst, key_value, left=0, right=None):
    if right is None:
        right = len(lst)

    middle = (left + right) // 2
    while lst[middle] != key_value and left <= right:
        if lst[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not left > right else (False, middle+1)


l = [9, 29, 34, 36, 40, 50, 51, 53, 57, 78, 85, 88, 88, 89, 92, 94, 94, 95, 99, 100]
print(binary_search(l, 54, 0))
print(binary_search(l, 88, 0))
