import unittest

from mjp_lambdata.my_mod import order_of_mag

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(order_of_mag(4), 40)

if __name__ == '__main__':
    unittest.main()