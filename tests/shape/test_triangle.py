"""
Description: Unit tests for the Book class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""

import unittest
from shape.triangle import Triangle

class TestClient(unittest.TestCase):
    
    def test_init_valid(self):
        triangle = Triangle("red", 3, 7, 9)

        # Name Mangling
        self.assertEqual(3, triangle._Triangle__side_1)
        self.assertEqual(7, triangle._Triangle__side_2)
        self.assertEqual(9, triangle._Triangle__side_3)

    def test_init_invalid_color_raises_exception(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(" ", 3, 7, 9)

    def test_init_invalid_side_1_raises_exception(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", "3", 7, 9)

    def test_init_invalid_side_2_raises_exception(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", 3, "7", 9)

    def test_init_invalid_side_3_raises_exception(self):
        with self.assertRaises(ValueError):     
            triangle = Triangle("red", 3, 7, "9")

    def setUp(self):
        self.triangle = Triangle("red", 3, 7, 9)

    def test_string_returned_in_expected_format(self):
        expected_output = "The shape color is red.\n This triangle has three sides with lengths of 3, 7 and 9 centimeters."
        self.assertEqual(expected_output, str(self.triangle))

    def test_correct_calculated_area_returned(self):
        expected_output = 8.786
        self.assertAlmostEqual(expected_output, self.triangle.calculate_area(), 2)

    def test_correct_calculated_perimeter_returned(self):
        expected_output = 19
        self.assertAlmostEqual(expected_output, self.triangle.calculate_perimeter())
        

    

    
