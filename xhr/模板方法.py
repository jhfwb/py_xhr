# -*- coding: utf-8 -*-
# 创建一个主体对象
from abc import ABCMeta, abstractmethod


class Windows(metaclass=ABCMeta):
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def paint(self):
        pass

    def run(self):
        import time
        while True:
            try:
                time.sleep(1)
                self.paint()
            except KeyboardInterrupt:
                break
        self.close()


class TxtWindows(Windows):
    def close(self):
        print('关闭窗口中...')

    def open(self):
        print('打开窗口中....')
        self.run()

    def paint(self):
        print('这是一个蓝色的窗口...')


if __name__ == '__main__':
    TxtWindows().open()
