# Наследование

**Наследование** - это способ создания нового класса для использования деталей существующего класса без его изменения. 
Вновь сформированный класс является производным классом (или дочерним классом). Точно так же существующий класс является
базовым классом (или родительским классом).

![inh](img/inheritance.png)

```python
class WaterBird:
    def __init__(self, name):
        self.name = name
        print("Bird is {}".format(self.name))

    def where_is_live(self):
        print("On the Earth")

    def swim(self):
        print("Can swim faster")

    def voice(self):
        pass

class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print("Penguin is ready")

    def where_is_live(self):
        print("North Pole")

    def run(self):
        print("Run faster")

    def voice(self):
        print('Pi-pi-pi')

class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print("Anywhere")

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('Kra-kra-kra')

peggy = Penguin('Ping')

peggy.where_is_live()
peggy.swim()
peggy.run()
peggy.voice()

print('======================')
duck = Duck('Donald Dug')

duck.where_is_live()
duck.swim()
duck.fly()
duck.voice()
```

```
Bird is Ping
Penguin is ready
North Pole
Can swim faster
Run faster
Pi-pi-pi
======================
Bird is Donald Dug
Duck is ready
Anywhere
Can swim faster
Fly very high
Kra-kra-kra
```

В приведенной выше программе мы создали два класса: `Bird` (родительский класс) и `Penguin` (дочерний класс). Дочерний 
класс наследует функции родительского класса. Мы можем видеть это из `swim()` метода. Опять же, дочерний класс изменил 
поведение родительского класса. Мы можем видеть это из метода `where_is_live()`. Кроме того, мы расширяем функции 
родительского класса, создавая новый `run()` метод. Тоже самое касается и класса `Duck`. Он так же наследуется от 
`Bird`, переопределяет методы `where_is_live()` и `voice()`, добавляет `fly()` метод.

Кроме того, мы используем `super()` функцию перед `__init__()` методом. Это потому, что мы хотим извлечь содержимое 
`__init__()` метода из родительского класса в дочерний класс и вызвать конструктор родительского класса.


## Множественное наследование

В `Python` так же, разрешено множественное наследование. Это позволяет строить новый класс на базе нескольких 
существующих классов и использовать их функционал в классе потомке.

![inh](img/inheritance_multi.png)

```python
class Horse:
    def fast(self):
        return 'fast'

class Donkey:
    def strong(self):
        return 'strong'

class Mule(Horse, Donkey):
    def new_character(self):
        return 'Donkey is {donkey}, Horse is {horse} but Mule is {donkey}, {horse} and hardy!'.format(
            donkey=self.strong(),
            horse=self.fast()
        );

mule = Mule()
print(mule.new_character())
```

```
Donkey is strong, Horse is fast but Mule is strong, fast and hardy!
```

```python
class Food(object):
    def drink(self):
        return ['Water', 'Cola']

    def allergen(self):
        return []

class Meat(Food):
    def drink(self):
        return ['Red wine'] + super(Meat, self).drink()

class Milk(Food):
    def allergen(self):
        return ['Milk-protein'] + super(Milk, self).allergen()

class Flour(Food): pass

class Rabbit(Meat):
    def drink(self):
        return ['Novello wine'] + super(Rabbit, self).drink()

class Pork(Meat):
    def drink(self):
        return ['Sovinion wine'] + super(Pork, self).drink()

    def allergen(self):
        return ['Pork-protein'] + super(Pork, self).allergen()

class Pasty(Milk, Flour): pass

class Pie(Rabbit, Pork, Pasty):
    def drink(self):
        return ['Mineral water'] + super(Pie, self).drink()

if __name__ == "__main__":
    pie = Pie()

    print('List of allergens: ')
    for allergen in pie.allergen(): print(' - ' + allergen)

    print('List of recommended drinks: ')
    for drink in pie.drink(): print(' - ' + drink)
```

```
List of allergens: 
 - Pork-protein
 - Milk-protein
List of recommended drinks: 
 - Mineral water
 - Novello wine
 - Sovinion wine
 - Red wine
 - Water
 - Cola
```

Немного об наследовании в этой [статье](https://habr.com/ru/post/62203/).