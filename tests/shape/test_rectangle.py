"""
Description: Unit tests for the Rectangle class.
Author: Ranindi Gunasekera
Date: 09/25/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_rectangle.py
"""

import unittest
from shape.rectangle import Rectangle

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        rectangle = Rectangle("pink", 5, 3)

        # Name Mangling
        self.assertEqual(5, rectangle._Rectangle__length)
        self.assertEqual(3, rectangle._Rectangle__width)
    
    def test_init_invalid_color_raises_exception(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(" ", 5, 3)

    def test_init_invalid_length_raises_exception(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("pink", "five", 3)
    
    def test_init_invalid_width_raises_exception(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("pink", 5, "three")

    def setUp(self):
        self.rectangle = Rectangle("pink", 5, 3)

    def test_string_returned_in_expected_format(self):
        expected_output = "The shape color is pink.\n This rectangle has four sides with the lengths of 5, 3, 5 and 3 centimeters."
        self.assertEqual(expected_output, str(self.rectangle))

    def test_correct_calculated_area_returned(self):
        expected_output = 15
        self.assertEqual(expected_output, self.rectangle.calculate_area())

    def test_correct_calculated_perimeter_returned(self):
        expected_output = 16
        self.assertEqual(expected_output, self.rectangle.calculate_perimeter())