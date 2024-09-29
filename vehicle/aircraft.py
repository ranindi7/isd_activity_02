""""
Description: A class to represent Aircraft objects.
Author: Ranindi Gunasekera
Date: 09/25/2024
"""
from vehicle.vehicle import Vehicle

class Aircraft(Vehicle):
    """
    Aircraft class. Represents the speed and the fuel burn rate of the Aircraft. 

    Attributes:
        fuel_burn_rate(float): Represents the rate at which Aircraft fuel is expended. the Automobile.
        speed(float): Represents the cruising speed of the Aircraft.
    """

    def __init__(self, make:str, model:str, fuel_burn_rate:float, speed:float):
        super().__init__(make, model)
        """
        Initializes an aircraft object based on the received arguments.

        Args:
            make(str): Represents the make (manufacturer) of the Vehicle.
            model(str): Represents the model (specific vehicle model) of the Vehicle.
            fuel_burn_rate(float): Represents the rate at which Aircraft fuel is expended. 
            speed(float): Represents the cruising speed of the Aircraft.
        Raises:
            ValueError when fuel burn rate and speed are not numeric
        """

        if isinstance(fuel_burn_rate, float):
            self.__fuel_burn_rate = fuel_burn_rate
        else:
            raise ValueError("Fuel burn rate must be numeric.")
        
        if isinstance(speed, float):
            self.__speed = speed
        else:
            raise ValueError("Speed must be numeric.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the make, model, fuel burn rate and the speed of the aircraft.
        Returns: str- make, model, speed and fuel burn rate formatted as a string
        """
        value = super().__str__() + f" \n This aircraft has a fuel burn rate of {self.__fuel_burn_rate} litres/hour, and a cruising speed of {self.__speed} km/hour."
        return value
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Returns the fuel requirements by calculating the flight time and multiplying it by the fuel burn rate.

        Returns:
            float: calculated fuel requirements
        """
        flight_time = distance / self.__speed
        fuel_requirements = flight_time * self.__fuel_burn_rate

        return fuel_requirements
