import unittest
from sumitems import sumlist

class Testsum_list(unittest.TestCase):
    def test_sum_list_negative(self):
        self.assertEqual(sumlist([1,-3,[4,7]]),8)
    def test_input_is_not_list(self):
        self.assertEqual(sumlist((1, 4, 5)),
                         'Invalid argument type. This should be a list')


if __name__ == '__main__':
    unittest.main()