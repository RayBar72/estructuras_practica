#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        name = "width"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(name))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        name = "height"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(name))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        name = "x"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        name ="y"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be > 0".format(name))
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        if self.y != 0:
            print("\n" * self.y, end="")
        s = (" " * self.x) + ("#" * self.width)
        i = self.height
        while i:
            print("{}".format(s))
            i -= 1

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id, self.x, self.y, self.width, self.height)