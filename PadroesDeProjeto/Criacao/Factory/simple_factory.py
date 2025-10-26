from abc import ABCMeta, abstractmethod

from abc import ABC

# class Animal(ABC):
#     @staticmethod
#     def falar(self):
#         pass



class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar():
        pass

class Cachorro(Animal):
    
    def falar(self):
        print('Au Au')

class Gato(Animal):
    
    def falar(self):
        print('Miau')

# Fábrica
class Farica:

    def criar_animal(self, tipo):
        return eval(tipo)().falar()
    
# Cliente

if __name__ == '__main__':
    fabrica = Farica()
    fabrica.criar_animal('Cachorro')
    fabrica.criar_animal('Gato')