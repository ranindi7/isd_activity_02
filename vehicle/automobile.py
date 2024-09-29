""""
Description: A class to represent Automobile objects.
Author: Ranindi Gunasekera
Date: 09/25/2024
"""

from vehicle.vehicle import Vehicle

class Automobile(Vehicle):
    """
    Automobile Class. Represents the number of kilometers a vehicle can drive per litre of gasoline.

    Attributes:
        kilometers_per_litre(float): Represents the number of kilometers the Automobile can drive per litre of gasoline.
    """

    def __init__(self, make: str, model:str, kilometers_per_litre: float):
        super().__init__(make, model)
        """
        Initializes an automobile object based on the received arguments for the vehicle

        Args:
            make(str): Represents the make (manufacturer) of the Vehicle.
            model(str): Represents the model (specific vehicle model) of the Vehicle.
            kilometers_per_litre(float): Represents the number of kilometers the Automobile can drive per litre of gasoline.

        Raises:
            ValueError if kilometers per litre is not numeric.
        """

        if isinstance(kilometers_per_litre, float):
            self.__kilometers_per_litre = kilometers_per_litre
        else:
            raise ValueError("Kilometers per litre must be numeric.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the make, model and the kilometeters per litre of the vehicle.
        Returns: str- make, model and km per litre formatted as a string
        """
        value = super().__str__() + f" \n This automobile can drive {self.__kilometers_per_litre} kilometers per litre."
        return value
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Returns how much fuel is required by calculating the distance divided by the kms per litre.

        Returns:
            float: calculated fuel requirements
        """
        fuel_requirements = distance / self.__kilometers_per_litre
        return fuel_requirements