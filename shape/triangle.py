""""
Description: A class to represent Triangle objects.
Author: Ranindi Gunasekera
Date: 09/18/2024
"""

import math
from shape.shape import Shape

class Triangle(Shape):
    """
    Triangle class. Represents all the dimensions of a triangle, its area and perimeter.

    Attributes:
        side_1(int): Represents the length of the first side of the Triangle in centimeters.
        side_2(int): Represents the length of the second side of the Triangle in centimeters.
        side_3(int): Represents the length of the third side of the Triangle in centimeters.
    """
    def __init__(self, color:str, side_1:int, side_2:int, side_3:int):
        super().__init__(color)
        """
        Initializes a triangle object based on the received arguments for the sides of the triangle.

        Args:
            color(str): Represents the color of the triangle.
            side_1(int): Represents the length of the first side of the Triangle in centimeters.
            side_2(int): Represents the length of the second side of the Triangle in centimeters.
            side_3(int): Represents the length of the third side of the Triangle in centimeters.
        Raises:
            ValueError if sides are not numeric. 
        """
        if isinstance(side_1, int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        
        if isinstance(side_2, int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        
        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the color of the triangle and the 3 lengths.

        Returns: str- color and lengths of triangle as formatted string.
        """
        value = super().__str__() + f"\n This triangle has three sides with lengths of {self.__side_1}, {self.__side_2} and {self.__side_3} centimeters."
        return value
    
    def calculate_area(self) -> float:
        """
        Returns the calculated area of the triangle by firstly 
        calculating the semi-perimeter and then applying a formula to get the area.


        Returns:
            float: calculated area of the triangle.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2   
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))

        return area
    
    def calculate_perimeter(self) -> float:
        """
        Returns the calculated perimeter of the triangle by adding all sides.

        Returns:
            float: calculated perimeter of the triangle.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3

        return perimeter 
    
    

