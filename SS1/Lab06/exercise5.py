import math

class Circle:
    """A class representing a circle."""
    
    def __init__(self, radius=1.0, color="red"):
        """Initialize a circle with radius and color."""
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        """Get the radius of the circle."""
        return self.__radius
    
    def setRadius(self, radius):
        """Set the radius of the circle."""
        self.__radius = radius
    
    def getColor(self):
        """Get the color of the circle."""
        return self.__color
    
    def setColor(self, color):
        """Set the color of the circle."""
        self.__color = color
    
    def getArea(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.__radius ** 2
    
    def __str__(self):
        """Return string representation of the circle."""
        return f"Circle[radius={self.__radius}, color={self.__color}]"


class Cylinder(Circle):
    """A class representing a cylinder, derived from Circle."""
    
    def __init__(self, radius=1.0, height=1.0, color="red"):
        """
        Initialize a cylinder with radius, height, and color.
        Supports multiple constructor signatures:
        - Cylinder() - default constructor
        - Cylinder(radius) - constructor with radius only
        - Cylinder(radius, height) - constructor with radius and height
        - Cylinder(radius, height, color) - constructor with all parameters
        """
        super().__init__(radius, color)
        self.__height = height
    
    def getHeight(self):
        """Get the height of the cylinder."""
        return self.__height
    
    def setHeight(self, height):
        """Set the height of the cylinder."""
        self.__height = height
    
    def getVolume(self):
        """Calculate and return the volume of the cylinder."""
        return self.getArea() * self.__height
    
    def __str__(self):
        """Return string representation of the cylinder."""
        return f"Cylinder[radius={self.getRadius()}, height={self.__height}, color={self.getColor()}]"


# Test cases (comment out when submitting)
# if __name__ == "__main__":
#     print("# Test Cylinder's default constructor and getter methods")
#     cy1 = Cylinder()
#     print(f"radius:{cy1.getRadius()} height:{cy1.getHeight()} color:{cy1.getColor()}")
#     
#     print("\n# Test Cylinder's overloaded constructor with one argument for radius")
#     cy2 = Cylinder(2.0)
#     print(f"radius:{cy2.getRadius()} height:{cy2.getHeight()} color:{cy2.getColor()}")
#     
#     print("\n# Test Cylinder's overloaded constructor with arguments for radius and height")
#     cy3 = Cylinder(3.0, 6.0)
#     print(f"radius:{cy3.getRadius()} height:{cy3.getHeight()} color:{cy3.getColor()}")
#     
#     print("\n# Test Cylinder's overloaded constructor with arguments for radius, height and color")
#     cy4 = Cylinder(4.0, 8.0, "blue")
#     print(f"radius:{cy4.getRadius()} height:{cy4.getHeight()} color:{cy4.getColor()}")
#     
#     print("\n# Test Cylinder's setter methods")
#     cy1.setRadius(6.5)
#     cy1.setHeight(8.8)
#     cy1.setColor("green")
#     print(f"radius:{cy1.getRadius()} height:{cy1.getHeight()} color:{cy1.getColor()}")
#     
#     print("\n# Test Cylinder's getVolume() method")
#     print(cy3.getVolume())
#     print(cy4.getVolume())
