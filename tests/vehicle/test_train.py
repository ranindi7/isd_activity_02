"""
Description: Unit tests for the Train class.
Author: Ranindi Gunasekera
Date: 09/25/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_train.py
"""

import unittest
from vehicle.train import Train

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        train = Train("Siemens", "Intercity Subway", 10, 0.03)

        # Name Mangling
        self.assertEqual("Siemens", train._Vehicle__make)
        self.assertEqual("Intercity Subway", train._Vehicle__model)
        self.assertEqual(10, train._Train__cars)
        self.assertEqual(0.03, train._Train__base_fuel_rate)

    def test_init_invalid_make_raises_exception(self):
        with self.assertRaises(ValueError):
            train = Train(" ", "Intercity Subway", 10, 0.03) 

    def test_init_invalid_model_raises_exception(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", " ", 10, 0.03)

    def test_init_invalid_cars_raises_exception(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", "Intercity Subway", "ten", 0.03)

    def test_init_invalid_base_fuel_rate_raises_exception(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", "Intercity Subway", 10, "three")

    def setUp(self):
        self.train = Train("Siemens", "Intercity Subway", 10, 0.03)

    def test_string_returned_in_expected_format(self): 
        expected_output = "Make: Siemens \n Model: Intercity Subway \n This train has a base fuel rate of 0.03 litres/kilometer, and contains 10 cars."
        self.assertEqual(expected_output, str(self.train))

    def test_correct_calculated_fuel_requirement_returned(self):
        distance = 6.0
        expected_output = 1.98
        self.assertAlmostEqual(expected_output,self.train.calculate_fuel_requirements(distance), 2)