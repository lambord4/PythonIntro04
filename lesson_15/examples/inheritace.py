class WaterBird:
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim fast')

    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Penguin is ready')

    def where_is_live(self):
        print('North Pole')

    def run(self):
        print('Run fast')

    def voice(self):
        print('Pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('Kra-kra-kra')


peggy = Penguin('Pin')
peggy.where_is_live()
peggy.run()
peggy.swim()
peggy.voice()

duck = Duck('Donald')
duck.fly()
duck.swim()