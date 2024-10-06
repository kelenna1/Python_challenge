import unittest
from prac_5 import square

class TestSquare(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(4), 16)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_square_invalid(self):
        with self.assertRaises(TypeError)
        return "error"
