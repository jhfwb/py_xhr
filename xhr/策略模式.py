# 根据不同的策略来执行不同的方式
from abc import abstractmethod, ABCMeta


class People:
    def __init__(self, strategy):
        self.__strategy = strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def look_tv(self):
        print('正在看电视：%s' % self.__strategy.do())


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def do(self):
        pass


class VipStrategy(Strategy):
    def do(self):
        return '跳过广告'


class CommonStrategy(Strategy):
    def do(self):
        return '开始广告'


if __name__ == '__main__':
    People(VipStrategy()).look_tv()
    People(CommonStrategy()).look_tv()
