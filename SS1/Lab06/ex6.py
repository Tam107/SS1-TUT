import math

'''
The Circle class models a circle with a radius and color.
'''
class Circle:
    # Constructs a Circle instance with default value for radius and color
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
    
    # Getter for radius 
    def getRadius(self):    
        return self.__radius

    # Getter for color     
    def getColor(self):
        return self.__color
    
    # Setter for radius 
    def setRadius(self, radius):
        self.__radius = radius
    
    # Setter for color 
    def setColor(self, color):
        self.__color = color

    # Returns the area of the circle
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    # Returns a String description of the Circle instance
    def __str__(self):
        return f"Circle[radius = {self.__radius}, color = {self.__color}]"

'''
The Cylinder class models a 3D cylinder with a radius, height and color.
'''
class Cylinder(Circle):
    # Constructor a Cylinder instance with default value for radius, height and color
    def __init__(self, radius = 1.0, height = 1.0, color = "red"):
        super().__init__(radius, color)
        self.__height = height

    # Getter for height 
    def getHeight(self):    
        return self.__height
    
    # Setter for height 
    def setHeight(self, height):    
        self.__height = height
    
    # Override method getArea() in the Circle class
    # Returns the surface area of the Cylinder instance
    def getArea(self):
        return 2 * math.pi * self.getRadius() * self.__height + 2 * super().getArea()

    # Returns the volume of the Cylinder instance
    # Using superclass method getArea() to get the base area
    def getVolume(self):
        return super().getArea() * self.__height

    # Returns a String description of the Circle instance
    def __str__(self):
        return f"Cylinder[radius:{self.getRadius()}, height:{self.__height}, color:{self.getColor()}]"
    
