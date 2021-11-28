#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('画一个圆形')


class Rectangle (Shape):
    def draw(self):
        print('画一个三角形')


class Square (Shape):
    def draw(self):
        print('画一个正方形')


class ShapeMaker:
    def __init__(self):
        self.__circle = Circle()
        self.__rectangle = Rectangle()
        self.__square = Square()

    def draw_circle(self):
        self.__circle.draw()

    def draw_rectangle(self):
        self.__rectangle.draw()

    def draw_square(self):
        self.__square.draw()


if __name__ == '__main__':
    ShapeMaker().draw_square()
    ShapeMaker().draw_rectangle()
    ShapeMaker().draw_circle()

