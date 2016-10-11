import unittest
from fractions import Fraction
from ..cg import HalfInt


class HalfIntTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_half_string_init(self):
        half = HalfInt("1/2")
        self.assertEqual(half, Fraction("1/2"))

    def test_half_num_init(self):
        half = HalfInt(1, 2)
        self.assertEqual(half, Fraction(1, 2))

    def test_whole_string_init(self):
        half = HalfInt("1")
        self.assertEqual(half, Fraction(1, 1))

    def test_whole_num_init(self):
        half = HalfInt(1, 1)
        self.assertEqual(half, Fraction(1, 1))

    def test_other_raises(self):
        self.assertRaises(ValueError, HalfInt, "1/3")

if __name__ == "__main__":
    unittest.main()
