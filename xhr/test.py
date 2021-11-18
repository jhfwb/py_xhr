# 创建一个自动驾驶系统
import abc
class Car(metaclass=abc.ABCMeta):
    @staticmethod
    def run():
        pass
    @staticmethod
    def turn():
        pass
    @staticmethod
    def stop():
        pass
class BenTianCar(Car):
    def run(self):
        print('本田跑')
    def turn(self):
        print('本田转')
    def stop(self):
        print('本田停')
class FoldCar(Car):
    def run(self):
        print('福特跑')
    def turn(self):
        print('福特转')
    def stop(self):
        print('福特停')
class AutoSystem:
    def __init__(self,car):
        self.car=car
    def run_car(self):
        self.car.run()
    def stop_car(self):
        self.car.stop()
    def turn_car(self):
        self.car.turn()
if __name__ == '__main__':
    AutoSystem(FoldCar()).run_car()