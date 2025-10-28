import math

class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getXY(self):
        return list([self.x, self.y])

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x=None, y=None, another=None):
        # Support passing a MyPoint as the first positional argument
        if another is None and y is None and isinstance(x, MyPoint):
            another = x
            x = None

        if another is not None and isinstance(another, MyPoint):
            dx = self.x - another.x
            dy = self.y - another.y
        elif x is not None and y is not None:
            dx = self.x - x
            dy = self.y - y
        else:
            # distance to origin
            dx = self.x
            dy = self.y

        return (dx * dx + dy * dy) ** 0.5


    def __str__(self):
        return f"({self.x},{self.y})"

class MyLine:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, begin = None, end = None):
        # Two construction modes:
        # - via coordinates (x1, y1, x2, y2)
        # - via existing MyPoint instances (begin, end)
        if begin is not None and end is not None:
            self.begin = begin
            self.end = end
        else:
            self.begin = MyPoint(x1, y1)
            self.end = MyPoint(x2, y2)


    def getBegin(self):
        return self.begin

    def getEnd(self):
        return self.end

    def setBegin(self, point: MyPoint):
        self.begin = point

    def setEnd(self, point: MyPoint):
        self.end = point

    def getBeginX(self):
        return self.begin.getX()

    def getBeginY(self):
        return self.begin.getY()

    def getEndX(self):
        return self.end.getX()

    def getEndY(self):
        return self.end.getY()

    def setBeginX(self, x):
        self.begin.setX(x)

    def setBeginY(self, y):
        self.begin.setY(y)

    def setEndX(self, x):
        self.end.setX(x)

    def setEndY(self, y):
        self.end.setY(y)

    def getBeginXY(self):
        return self.begin.getXY()

    def setBeginXY(self, x, y):
        self.begin.setXY(x, y)

    def setEndXY(self, x, y):
        self.end.setXY(x, y)

    def getEndXY(self):
        return self.end.getXY()

    def getLength(self):
        return self.begin.distance(self.end)

    def getGradient(self):
        x_diff = self.begin.getX() - self.end.getX()
        y_diff = self.begin.getY() - self.end.getY()
        angle = math.atan2(y_diff, x_diff)
        return angle




    def __str__(self):
        return f"MyLine[begin=({self.begin.getX()},{self.begin.getY()}), end=({self.end.getX()},{self.end.getY()})]"
