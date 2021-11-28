import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass
class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def paint(self):
        pass

class Cycle(Shape):
    def __init__(self,color):
        self.color=color
        self.name='圆形'
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def __init__(self):
        pass
    def paint(self,shape):
        print('正在画红色'+shape.name)
if __name__ == '__main__':
    Cycle(Red()).draw()