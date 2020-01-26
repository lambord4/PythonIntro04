
class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu1 = cpu
        self._memory = memory
        self.hdd = hdd

    def print_comp(self):
        print('CPU: {}GHz\nMemory: {}Mb\nHDD: {}Gb'.format(
            self.__cpu1 / 1000,
            self._memory,
            self.hdd
        ))


comp = Computer(2300, 16000, 2000)
comp.print_comp()
print(dir(comp))
# print(comp._Computer__cpu)
print(comp._memory)
# comp._Computer__cpu = 2400
comp.print_comp()
