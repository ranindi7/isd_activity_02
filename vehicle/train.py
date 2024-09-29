""""
Description: A class to represent Train objects.
Author: Ranindi Gunasekera
Date: 09/25/2024
"""

from vehicle.vehicle import Vehicle

class Train(Vehicle):
    """
    Train class. Represents the number of cars, fuel burn rate and fuel requirements of the train.

    Attributes:
        make(str): Represents the make (manufacturer) of the Vehicle.
        model(str): Represents the model (specific vehicle model) of the Vehicle.
        cars(int): Represents the number of cars on the Train.
        base_fuel_rate(float): Represents the rate at which fuel is burned by the Train.
    """

    def __init__(self, make:str, model:str, cars:int, base_fuel_rate:float):
        super().__init__(make, model)
        """
        Initializes a train object based on the received arguments.
        
        Args:
            make(str): Represents the make (manufacturer) of the Vehicle.
            model(str): Represents the model (specific vehicle model) of the Vehicle.
            cars(int): Represents the number of cars on the Train.
            base_fuel_rate(float): Represents the rate at which fuel is burned by the Train.

        Raises:
            ValueError when cars is not an int and base fuel rate is  not a float.
        """

        if isinstance(cars, int):
            self.__cars = cars
        else:
            raise ValueError("Cars must be numeric.")
        
        if isinstance(base_fuel_rate, float):
            self.__base_fuel_rate = base_fuel_rate
        else:
            raise ValueError("Base fuel rate must be numeric.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the make, model, number of cars and the base fuel rate.
        Returns: str- make, model, number of cars and base fuel rate formatted as a string
        """
        value = super().__str__() + f" \n This train has a base fuel rate of {self.__base_fuel_rate} litres/kilometer, and contains {self.__cars} cars."
        return value
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Returns the fuel requirements by calculating the total fuel and multiplying it by the distance travelled.
        Returns:
            float: calculated fuel requirements
        """
        
        total_fuel = self.__base_fuel_rate * (1.1 * self.__cars)
        fuel_requirements = total_fuel * distance

        return fuel_requirements
