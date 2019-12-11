# Frozenset

`frozenset` - такая же структура как `set`. Единственное отличие `set` от `frozenset` заключается в том, что `set` - 
изменяемый тип данных, а `frozenset` - нет (immutable). Примерно похожая ситуация с `списками` и `кортежами`.

```python
a = set('qwerty')
b = frozenset('qwerty')
print(a == b)                                       # True
print(type(a - b))                                  # <class 'set'>
print(type(a | b))                                  # <class 'set'>
a.add(1)
b.add(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'
```

Попытка изменить `frozenset` возбудит исключение.
