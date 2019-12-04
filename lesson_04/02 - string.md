# String

Статья по поводу [скорпирования строк](https://asoldatenko.com/can-i-copy-string-in-python-and-how.html)
```python
import copy

v = 'PycharmProjects/HillelExamples'
print(v)
print(id(v))

v1 = v[:]
print(id(v1))
v2 = copy.copy(v)
print(id(v2))
v3 = str(v)
print(id(v3))
v4 = v.encode().decode()
print(id(v4))
v5 = (v + '.')[:-1]
print(id(v5))
```

- input()   use for input string from keyboard
```python
t = input()
number = int(t)
u = str(number)
print(t * 3)
print(t + ' ' + u)
```

- len()     get length of string
```python
s = input()
print(len(s))
```

## index

К символам строки можно обращаться по индексу. Например строка "Hello":
```
+----------+-------+-------+-------+-------+-------+
| Строка S | H     | e     | l     | l     | o     |
+----------+-------+-------+-------+-------+-------+
| Индекс   | S[0]  | S[1]  | S[2]  | S[3]  | S[4]  |
+----------+-------+-------+-------+-------+-------+
| Индекс   | S[-5] | S[-4] | S[-3] | S[-2] | S[-1] |
+----------+-------+-------+-------+-------+-------+
```
В отличии от других языков, в Python индесы могут быть как положительными (от 0 до размер_строки - 1), так и 
отрицательными (от -1 до -(размер_строки))
При обращении к строке по несуществующему индексу ( >= len(s) или < -len(s)) возбуждается исключение `IndexError: 
string index out of range.`


## slices
Срезы используются ля получения подстроки из строки.
- синтаксис среза
    ```
        string[start: stop: step]
    ```

    - `start` - начало среза
    - `stop` - конец среза (не входит в срез)
    - `step` - шаг среза
    
Если параметр `stop` будет >= len(s) исключение не возбуждается. Мы просто получим подстроку от `start` до конца строки.
```python
s = 'test string'
print(s[1])         # e
print(s[-1])        # g
print(s[1:3])       # es
print(s[1:-1])      # est strin
print(s[:3])        # tes
print(s[2:])        # st string
print(s[:-1])       # test strin
print(s[::2])       # ts tig
print(s[1::2])      # etsrn
print(s[::-1])      # gnirts tset
```

Параметры среза очень похожи на параметры функции `range()`
```python
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])
```
вывод:
```
acegi
0 a
2 c
4 e
6 g
8 i
```

## methods
- `find()`

Метод выполняет поиск (слева на право) вхождения подстроки в строку и возвращает индекс вхождения, иначе `-1`
```
str.find(sub[, start[, end]])
```
Возвращает индекс вхождения подстрок в строку. Если подстрока найдена не была, будет возвращено `-1`.
```python
S = 'Hello'
print(S.find('e'))      # 1
print(S.find('ll'))     # 2
print(S.find('L'))      # -1
```

Метод `find()` кроме подстроки, может принммать параметры задающие границы поиска
```python
txt = "Hello, welcome to my world."
x = txt.find('l')
print(x)                   # 2
x = txt.find('l', x+1)
print(x)                   # 3
x = txt.find('l', x+1)
print(x)                   # 9
x = txt.find('l', x+1)
print(x)                   # 24
x = txt.find('l', x+1)
print(x)                   # -1
```

- `rfind()`

Тоже что и `find()` только поиск будет выполняться не слева на право, а наоборот, с права на лево.
```
str.rfind(sub[, start[, end]])
```

```python
S = 'Hello'
print(S.find('l'))      # 2
print(S.rfind('l'))     # 3
```

```python
txt = "Hello, welcome to my world."
x = txt.rfind('l')
print(x)                    # 24
x = txt.rfind('l', 0, x)
print(x)                    # 9
x = txt.rfind('l', 0, x)
print(x)                    # 3
x = txt.rfind('l', 0, x)
print(x)                    # 2
x = txt.rfind('l', 0, x)
print(x)                    # -1
```

- `replace()`
```
str.replace(old, new, count)
```

Метод возвращает строку в которой была выполнена замена подстрок

```python
print('Hello'.replace('l', 'L'))            # HeLLo
```
Можно указать какое количество вхождений будет заменено
```python
print('Abrakadabra'.replace('a', 'A', 2))   # AbrAkAdabra
```

- `count()`
```
str.count(sub[, start[, end]])
```

Метод `count()` возвращает количество вхождений подстроки в строке
```python
print('Abracadabra'.count('a'))             # 4
print(('a' * 10).count('aa'))               # 5
```
Можно указать в каких границах выполнять поиск
```python
print('Abracadabra'.count('a', 4))          # 3
print('Abracadabra'.count('a', 4, 8))       # 2
```

- `capitalize()`
```
str.capitalize()
```
Метод возвращает строку у которой все символы в нижнем регистр, кроме первого символа. Первый символ будет переведён в 
верхний регистр.

```python
txt = "this is the first line of the example"
print(txt.capitalize())                     # This is the first line of the example
txt = "this is the fIRst Line of thE exaMple"
print(txt.capitalize())                     # This is the first line of the example
```

- `join()`
```
str.join(iterable)
```
Метод возвращает строку "склееную" из строк параметра `iterable` через разделитель представленный `str`

```python
txt = 'one two three four five six seven'
print(txt)                                  # one two three four five six seven
txt = ', '.join(txt.split())
print(txt)                                  # one, two, three, four, five, six, seven
```

- `len()`
```
len(str)
```
Метод возвращает длину строки в символах.
```python
txt = 'one two three four five six seven'
print(len(txt))                             # 33
```

- `upper()`
Метод возвращает строку у которой все символы переведены в верхний регистр
```python
txt = 'one two three four five six seven'
print(txt.upper())                          # ONE TWO THREE FOUR FIVE SIX SEVEN
```

- `lower()`
Метод возвращает строку у которой все символы переведены в нижний регистр
```python
txt = 'ONE TWO THREE FOUR FIVE SIX SEVEN'
print(txt.lower())                          # one two three four five six seven
```

- `split()`
```
str.split(sep=None, maxsplit=-1)
```
Метод разделяет строку на подстроки, по указаной подстроке, и формирует список подстрок. По умолчанию в качестве 
разделителя используется - `пробел`.  

```python
txt = 'one two three four five six seven'
result = txt.split()
print(result)                               # ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
```
Можно указать на сколько глубоко выполнять разделение строки. Для этого надо указать параметр `maxsplit`
```python
txt = 'one two three four five six seven'
result = txt.split(maxsplit=2) 
print(result)                               # ['one', 'two', 'three four five six seven']
```
Так же, можно указать свою строку разделитель. 
```python
txt = 'one,two,hhree,four,five,six,seven'
result = txt.split()
print(result)                               # ['one,two,hhree,four,five,six,seven']
result = txt.split(',')
print(result)                               # ['one', 'two', 'hhree', 'four', 'five', 'six', 'seven']
result = txt.split(',', maxsplit=3)
print(result)                               # ['one', 'two', 'hhree', 'four,five,six,seven']
```

- `strip()`
```
str.strip(chars)
```
Метод возвращает строку у которой ведущие и завершающие символы совпадающие с значением `chars`. По умолчанию
это значение - пробел.
```python
txt = '   one two three four five six seven       '
print("'" + txt + "'")                      # '   one two three four five six seven       '
result = txt.strip()
print("'" + result + "'")                   # 'one two three four five six seven'
```
Можно указать свою подстроку которую надо удалить.
```python
txt = 'one two three four five six seven one'
print("'" + txt + "'")                      # 'one two three four five six seven one'
result = txt.strip('one')
print("'" + result + "'")                   # ' two three four five six seven '
```

- `title()`
```
str.title()
```
Метод возвращает строку у которй все первые символы каждого слова переведены в верхний регистр? а остальные символы в
нижний
```python
txt = 'one two three four five six seven'
result = txt.title()
print(result)                               # One Two Three Four Five Six Seven
```
