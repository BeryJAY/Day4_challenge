import unittest

from power import power

class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,1),pow(2,1))
    def test_both_negative(self):
        self.assertEqual(power(-8, -8), pow(-8, -8))

    def test_float_power(self):
        self.assertEqual(power(-4.5, 6.2), 'invalid input')
if __name__ == '__main__':
    unittest.main()

