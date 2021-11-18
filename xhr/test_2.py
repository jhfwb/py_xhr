import abc
class Animal(metaclass=abc.ABCMeta):
    @staticmethod
    def eat():
        pass
    @staticmethod
    def sleep():
        pass
class LandAnimal(Animal,metaclass=abc.ABCMeta):
    @staticmethod
    def walk():
        pass
class SeaAnimal(Animal,metaclass=abc.ABCMeta):
    @staticmethod
    def swim():
        pass
class animal_c(Animal):
    def eat(self):
        print('普通动物在吃饭')
class tiger(LandAnimal,animal_c):
    def walk(self):
        print('老虎在走路')
if __name__ == '__main__':
    tiger().eat()