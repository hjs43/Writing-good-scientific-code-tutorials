import unittest

from fibo import fibo

class FiboTestCase(unittest.TestCase):
    def test_edge_case(self):
        self.assertEqual(0, fibo(0))
        self.assertEqual(1, fibo(1))

    def test_negative_param(self):
        self.assertRaises(ValueError,
                          fibo,
                          -1)

    def test_nominal_case(self):
        self.assertEqual(8, fibo(6))
        self.assertEqual(55, fibo(10))

if __name__ == "__main__":
    unittest.main()
