# Python ~~variable~~ reference in memory

**Пересмотреть эту [статью](https://realpython.com/python-variables/)** 

- 'C' style variable
```C
int A = 100;

+---------+--------+
| address | 0x45F6 |
+---------+--------+
| value   | 100    |
+---------+--------+
| type    | int    |
+---------+--------+
| name    | A      |
+---------+--------+

sizeof(A) ==> 4
```
- Python style "variable"
```
A = 100

              +-----------+---------+
              | type      | integer |
   reference  +-----------+---------+
A ==========> | reference | 3       |
              +-----------+---------+
              | value     | 100     |
              +-----------+---------+
              
sys.getsizeof(A) ==> 28
```

## Example

```python
pi = 3.14
length = 25
enabled = False
text = 'Hello World'
```

## Assignment
- multi
```python
x, y, z = 1, 2, 3       # tuple
```
- cascade
```python
x = y = z = 0
```

## Change values of two variable
### first variant (use one extra variable)
```python
a = 2
b = 5
tmp = a
a = b
b = tmp
```

### second variant (use two extra variables)
```python
a = 2
b = 5
x = a
y = b
a = y
b = x
```

### thrid variant (don't use any extra variables)
```python
a = 2
b = 5

a, b = b, a
```

## Rules
- Use combination of letters in lower case (a-z), upper case (A-Z), numbers and the underscore
- Case Sensitivity
- **Must Not use a Python Keyword**
- **Must Not Begin with a Number**
