from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print('it is running...')

c1=Laptop()
print(c1.process())