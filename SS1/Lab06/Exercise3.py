import math

class MyTriangle:
    def __init__(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, v1=None, v2=None, v3=None):
        if v1 is not None and v2 is not None and v3 is not None:
            self.__v1 = v1
            self.__v2 = v2
            self.__v3 = v3
        else:
            self.__v1 = MyPoint(x1, y1)
            self.__v2 = MyPoint(x2, y2)
            self.__v3 = MyPoint(x3, y3)

    def getPerimeter(self):
        side1 = self.__v1.distance(another=self.__v2)
        side2 = self.__v2.distance(another=self.__v3)
        side3 = self.__v3.distance(another=self.__v1)
        return side1 + side2 + side3

    def getType(self):
        side1 = self.__v1.distance(another=self.__v2)
        side2 = self.__v2.distance(another=self.__v3)
        side3 = self.__v3.distance(another=self.__v1)

      
        epsilon = 1e-10
        equal12 = abs(side1 - side2) < epsilon
        equal23 = abs(side2 - side3) < epsilon
        equal31 = abs(side3 - side1) < epsilon

        if equal12 and equal23 and equal31:
            return "Equilateral"
        elif equal12 or equal23 or equal31:
            return "Isosceles"
        else:
            return "Scalene"

    def __str__(self):
        return f"MyTriangle[v1={self.__v1}, v2={self.__v2}, v3={self.__v3}]"


class MyPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getXY(self):
        return [self.__x, self.__y]

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, x=None, y=None, another=None):
        if another is not None:
            dx = self.__x - another.getX()
            dy = self.__y - another.getY()
        elif x is not None and y is not None:
            dx = self.__x - x
            dy = self.__y - y
        else:
            dx = self.__x - 0
            dy = self.__y - 0
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f"({self.__x},{self.__y})"

