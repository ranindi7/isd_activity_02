""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Ranindi Gunasekera
Date: 09/25/2024
"""

from shape import *


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")
    # 1. Create an empty list of Shape objects.
    shape = []

    # 2. Code a statement which creates an instance of the Triangle class.
    # Append the Triangle to the list of shapes.
    try:
        triangle = Triangle("red", 3, 7, 9)
        shape.append(triangle)
    except ValueError as e:
        print(e)


    # 3. Code a statement which creates an instance of the Rectangle class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle = Rectangle("pink", 5, 3)
        shape.append(rectangle)
    except ValueError as e:
        print(e)


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle = Triangle("blue", 4, 9, 7)
        shape.append(triangle)
    except ValueError as e:
        print(e)

    try:
        rectangle = Rectangle("purple", 6, 2)
        shape.append(rectangle)
    except ValueError as e:
        print(e)

    try:
        rectangle = Rectangle("green", 7, 3)
        shape.append(rectangle)
    except ValueError as e:
        print(e)

    # 5. Iterate through the list of shapes.  On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shape:
        print(shape)

        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")


    # *** END PART 1 ***

    # *** PART 2 ***
    print("*************PART 2****************")
    # 1. Create an empty list of Vehicle objects.
    vehicle = []

    # 2. Code a statement which creates an instance of the Automobile class.
    # Append the Automobile to the list of vehicles.
    try:
        automobile = Automobile("Ford", "Escape", 12.0)
        vehicle.append(automobile)
    except ValueError as e:
        print(e)


    # 3. Code a statement which creates an instance of the Aircraft class.
    # Append the Aircraft to the list of vehicles.
    try:
        aircraft = Aircraft("Boeing", "737", 7.0, 9.0)
        vehicle.append(aircraft)
    except ValueError as e:
        print(e)


    # 4. Code 3 additional statements which creates an instance of 
    # Automobile, Aircraft or Train classes (your choice).
    # Append these instances to the list of vehicles.
    try:
        aircraft = Aircraft("Boeing", "Airbus", 40.0, 550.0)
        vehicle.append(aircraft)
    except ValueError as e:
        print(e)

    try:
        automobile = Automobile("Honda", "Civic", 7.9)
        vehicle.append(automobile)
    except ValueError as e:
        print(e)

    try:
        automobile = Automobile("Volkswagen", "Jetta", 6.6)
        vehicle.append(automobile)
    except ValueError as e:
        print(e)



    # 5. Iterate through the list of vehicles.  On each iteration:
    # - print the vehicle
    # - print the phrase:
    # "Fuel needed for 500 kilometers: {fuel requirements} litres."
    for vehicle in vehicle:
        print(vehicle)

        print(f"Fuel needed for 500 kilometers: {vehicle.calculate_fuel_requirements(500)} litres")
        

if __name__ == "__main__":
    main()