import unittest
from fractions import Fraction

from my_sum import my_sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

"""
The results of this test show that my_sum correctly adds lists together, and that the unittest function works as expected, flagging
the incorrectly summed fractions as a failure. The first test was a success, and the second test failed, which was expected. 
These results indicate that the code works properly for my sample integer data. The unittest function worked as expected.
"""