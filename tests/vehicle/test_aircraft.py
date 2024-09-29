"""
Description: Unit tests for the Aircrat class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_aircraft.py
"""

import unittest
from vehicle.aircraft import Aircraft

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        aircraft = Aircraft("Boeing", "737", 7.0, 9.0)

        # Name Mangling
        self.assertEqual("Boeing", aircraft._Vehicle__make)
        self.assertEqual("737", aircraft._Vehicle__model)
        self.assertEqual(7.0, aircraft._Aircraft__fuel_burn_rate)
        self.assertEqual(9.0, aircraft._Aircraft__speed)

    def test_init_invalid_make_raises_exception(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft(" ", "737", 7.0, 9.0)

    def test_init_invalid_model_raises_exception(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", " ", 7.0, 9.0)

    def test_init_invalid_fuel_burn_rate_raises_exception(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "737", "seven", 9.0)

    def test_init_invalid_speed_raises_exception(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "737", 7.0, "nine")

    def setUp(self):
        self.aircraft = Aircraft("Boeing", "737", 7.0, 9.0)

    def test_string_returned_in_expected_format(self):
        expected_output = "Make: Boeing \n Model: 737 \n This aircraft has a fuel burn rate of 7.0 litres/hour, and a cruising speed of 9.0 km/hour."
        self.assertEqual(expected_output, str(self.aircraft))

    def test_correct_calculated_fuel_requirement_returned(self):
        distance = 36.0
        expected_output = 28.0
        self.assertEqual(expected_output, self.aircraft.calculate_fuel_requirements(distance))