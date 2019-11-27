# Type of value

## Data type in Python
- 2, 94, 0, -3 - `integer value`
- 3.14, 5.6, -4.5, 0.0 - `floating value`	
- ‘Hello World!’, "Some text" - `string value`	
- True, False - `boolean value`
- 2+3j - `complex value`

## Use ``type`` function to get data type of object
```python
print(type(2))          # <class 'int’>
print(type(3.14))       # <class 'float’>
print(type("Test"))      # <class 'str’>
print(type(True))       # <class 'bool’>
print(type(1+3j))       # <class 'complex'>
```

## Integer
- use simple arithmetic operations 
- support of long arithmetic, but need more the memory
- don't has a size limit
```bash
2**1000**345432
```

## Float
- don't a precision
```sh
0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
0.9999999999999999
```
`for high precision you need to use the Decimal or/and Fraction modules`

- don't support long arithmetic
```sh
a = 3 ** 1000
a + 0.1
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a + 0.1
OverflowError: int too large to convert to float
```

## String
```python
'same text'
"one more line of string"

'''
    multi line
        text
'''

"""
    multi
        line
            text
"""
```

- get symbol by index
```python
s = 'Hello World!'
print(s[3])

# string is immutable
s[5] = 'r' 
```

- get slice of string
```python
s = 'Hello World!'

print(s[1:])        # ello World!
print(s[1:6])       # ello
print(s[:6])        # Hello
print(s[::2])       # HloWrd
print(s[::-1])      # !dlroW olleH
print(s[-7: -1:])   # World
print(s[-7:])       # World!
print(s[-1::-1])    # !dlroW olleH
print(s[:-1:])      # Hello World

s = 'It is very long text. And this text need to place on some line'

```
