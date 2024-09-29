""""
Description: A class to represent generic Vehicle objects.
Author: Ranindi Gunasekera
Date: 09/25/2024
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Vehicle Class. Represents a vehicle

    Attributes:
        make(str): Represents the make (manufacturer) of the Vehicle.
        model(str): Represents the model (specific vehicle model) of the Vehicle.
    """

    def __init__(self, make: str, model:str):
        """
        Initializes a vehicle object based on received arguments.

        Args:
            make(str): Represents the make (manufacturer) of the Vehicle.
            model(str): Represents the model (specific vehicle model) of the Vehicle.

        Raises:
            ValueError if the make or model is blank.
        """

        if len(make.strip())==0:
            raise ValueError("Make cannot be blank.")
        else:
            self.__make = make

        if len(model.strip())==0:
            raise ValueError("Model cannot be blank.")
        else:
            self.__model = model

    @property
    def make(self) -> str:
        """
        Accessor for the make attribute.
        Returns: str- The make associated with the Vehicle instance.
        """
        return self.__make
    
    @property
    def model(self) -> str:
        """
        Accessor for the model attribute.
        Returns: str- The model associated with the Vehicle instance.
        """
        return self.__model
    
    def __str__(self) -> str:
        """
        Returns a string representation of the make and model of the vehicle.
        Returns: str: the make and model of the vehicle formatted as a string. 
        """
        return (f"Make: {self.__make} \n Model: {self.__model}")
    
    @abstractmethod
    def calculate_fuel_requirements(self, distance:float) -> float:
        """
        Calculate the fuel required to move the vehicle the distance provided.
        
        Args:
            None

        Returns:
            float
        """
        pass
    
