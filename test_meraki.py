import unittest
from meraki import Meraki
from urllib.parse import urlparse


class testMeraki(unittest.TestCase):
    def test_apikey(self):
        '''Tests Meraki API key attribute'''
        obj = Meraki()
        self.assertTrue(obj.api_key)

    def test_base_url(self):
        '''Tests Meraki base url attribute'''
        obj = Meraki()
        result = urlparse(obj.base_url)
        self.assertTrue(result.scheme and result.netloc)

    def test_max_retries(self):
        '''Tests Meraki max retries attribute'''
        obj = Meraki()
        self.assertIsInstance(obj.max_retries, int)


if __name__ == '__main__':
    unittest.main()
