import unittest
from IT_414_Unit2 import add_numbers

class TestAddNumbers(unittest.TestCase):
    """Automated test that tests the summing function."""
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(2.5, 3.5), 6.0)

if __name__ == "__main__":
    unittest.main()
