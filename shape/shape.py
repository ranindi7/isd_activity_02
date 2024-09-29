""""
Description: A class to represent generic Shape objects.
Author: Ranindi Gunasekera
Date: 09/18/2024
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Shape Class. Represents a shape. 

    Attributes:
        color(str): Represents the color of the Shape. 
    """
    def __init__(self, color: str):
        """
        Initializes a shape object based on received argument.

        Args:
            color(str): Represents the color of the Shape.
        Raises:
            ValueError if color is blank.
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")
        else:
            self.__color = color

    
    def __str__(self) -> str:
        """
        Returns a string representation of the shape color.
        Returns: str- the color of the shape as a formatted string.
        """
        return (f"The shape color is {self.__color}.")
    
    
    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculates the area of the shape.
        Args:
            None
        Returns: float
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.
        Args:
            None
        Returns: float
        """
        pass
