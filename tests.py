import unittest
from main import to_upper, calculate_age


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Shubham"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "SHUBHAM")
    
    def test_calculate_age(self):
        self.assertEqual(calculate_age(), True)



if __name__ == '__main__':
    unittest.main()