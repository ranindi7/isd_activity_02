""""
Description: A class to represent Rectangle objects.
Author: Ranindi Gunasekera
Date: 09/25/2024
"""

import math
from shape.shape import Shape

class Rectangle(Shape):
    """
    Rectangle class. Represents all the the length and width, its area and perimeter.

    Attributes:
        length: Represents the length of two opposing sides of the Rectangle in centimeters. 
        width: Represents the width of two opposing sides of the Rectangle in centimeters.
    """
    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)
        """
Initializes a triangle object based on the received arguments for the sides of the triangle.

        Args:
            color(str): Represents the color of the rectangle.
            length: Represents the length of two opposing sides of the Rectangle in centimeters. 
            width: Represents the width of two opposing sides of the Rectangle in centimeters.
        Raises:
            ValueError if length and width are not numeric.
        """

        if isinstance(length, int):
            self.__length = length 
        else:
            raise ValueError("Length must be numeric.")
        
        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Width must be numeric.")
        

    def __str__(self) -> str:
        """
        Returns a string representation of the color of the triangle and the 3 lengths.

        Returns: str- color and lengths of triangle as formatted string.
        """
        value = super().__str__() + f"\n This rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters."
        return value
    
    def calculate_area(self) -> float:
        """
        Returns the calculated area of the rectangle by multiplying the length and width.


        Returns:
            float: calculated area of the rectangle.
        """

        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self) -> float:
        """
        Returns the calculated perimeter of the rectangle by multiplying the sides by 2
        and then adding them.

        Returns:
            float: calculated perimeter of the rectangle.
        """

        perimeter = self.__length * 2 + self.__width * 2
        return perimeter        