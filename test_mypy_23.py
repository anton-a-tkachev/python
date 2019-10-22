# Unit test
import unittest
from math import pi
from mypy_23 import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 1j)
        self.assertRaises(TypeError, circle_area, "1")
        self.assertRaises(TypeError, circle_area, True)