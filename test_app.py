import unittest
from app import to_msg


class testApp(unittest.TestCase):
    def test_dict_to_msg(self):
        '''Tests dict_to_msg function'''
        test_dict = {'key': 'value'}
        self.assertIsInstance(to_msg(test_dict), str)


if __name__ == '__main__':
    unittest.main()
