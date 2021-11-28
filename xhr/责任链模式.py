#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta
"""
设计模式：责任链模式

当处理问题的顺序是递进的，或者是链状的，则可以使用责任链模式。
比如说处理response。或者是解析文字。
"""


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class Handler1(Handler):
    def __init__(self):
        self.next = Handler2()

    def handle(self):
        print('启动汽车')
        self.next.handle()


class Handler2(Handler):
    def __init__(self):
        self.next = Handler3()

    def handle(self):
        print('松开刹车')
        self.next.handle()


class Handler3(Handler):
    def __init__(self):
        pass

    def handle(self):
        print('加油门')


if __name__ == '__main__':
    Handler1().handle()
