"""
Description: Unit tests for the Automobile class.
Author: Ranindi Gunasekera
Date: 09/25/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_automobile.py
"""

import unittest
from vehicle.automobile import Automobile

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        automobile = Automobile("Ford", "Escape", 12.0)

        # Name Mangling
        self.assertEqual("Ford", automobile._Vehicle__make)
        self.assertEqual("Escape", automobile._Vehicle__model)
        self.assertEqual(12.0, automobile._Automobile__kilometers_per_litre)

    def test_init_invalid_make_raises_exception(self):
        with self.assertRaises(ValueError):
            automobile = Automobile(" ", "Escape", 12.0)

    def test_init_invalid_model_raises_exception(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("Ford", " ", 12.0)

    def test_init_invalid_kilometers_per_litre_raises_exception(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("Ford", "Escape", "twelve")

    def setUp(self):
        self.automobile = Automobile("Ford", "Escape", 12.0)

    def test_string_returned_in_expected_format(self):
        expected_output = "Make: Ford \n Model: Escape \n This automobile can drive 12.0 kilometers per litre."
        self.assertEqual(expected_output, str(self.automobile))

    def test_correct_calculated_fuel_requirement_returned(self):
        distance = 24.0
        expected_output = 2.0
        self.assertEqual(expected_output, self.automobile.calculate_fuel_requirements(distance))

    
