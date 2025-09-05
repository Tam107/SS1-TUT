import math

class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def getArea(self):
        result = math.pi * self.radius * self.radius
        return result

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Circle[radius = {self.radius}, color = {self.color}]"

c1 = Circle()
print(c1)
print(f"Circle area: {c1.getArea()}")

c2 = Circle(2.0,"blue")
print(c2)
print(f"Circle area: {c2.getArea()}")