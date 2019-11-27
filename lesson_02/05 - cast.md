# Приведение (преобразрвание) типов

- to integer
```python
int('45')           # 45        str --> int 
int(3.14)           # 3         float --> int
int(True)           # 1         bool --> int
int(False)          # 0         bool --> int

```

- to float
```python
float('3.14')       # 3.14      str --> float
float('3')          # 3.0       str --> float
float(25)           # 25.0      int --> float
float(False)        # 0.0       bool --> float
float(True)         # 1.0       bool --> float
```

- to str
```python
str(25)             # '25'      int --> str
str(3.14)           # '3.14'    float --> str
str(True)           # 'True'    bool --> str
str([1, 2, 3])      # '[1, 2, 3]'   list --> str
str([1, 2, 3, 4, 5])
# '[1, 2, 3, 4, 5]'     list --> str
str((1, 2, 3, 4, 5))
# '(1, 2, 3, 4, 5)'     tuple --> str
str({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})
# "{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}"      dict --> str
```

```python
# 'Test string' + 34  # incorrect
'Test string' + str(34) # is correct
```

- to tuple
```python
tuple('12345')      # ('1', '2', '3', '4', '5')     str --> tuple
tuple(['1', '2', '3', '4', '5'])    # ('1', '2', '3', '4', '5')     list --> tuple
tuple({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})    # (1, 2, 3, 4, 5)   dict --> tuple
```

- to list
```python
list('12345')       # ['1', '2', '3', '4', '5']     # str --> list
list(('1', '2', '3', '4', '5'))     # ['1', '2', '3', '4', '5']     tuple --> list
# list('1', '2', '3', '4', '5')       # incorrect expression
list({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})    # [1, 2, 3, 4, 5]   dict --> list
```