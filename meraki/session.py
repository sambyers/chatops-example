import requests
import logging
from time import sleep


class Session:
    def __init__(self, api_key, base_url, max_retries):
        self.api_key = api_key
        self.base_url = base_url
        self.max_retries = max_retries
        self.headers = {
            'content-type': "application/json",
            'x-cisco-meraki-api-key': api_key
            }
        self.logger = logging.getLogger(__name__)

    def request(self, method, url):
        response = None
        url = self.base_url + url
        retries = self.max_retries
        while retries > 0:
            try:
                response = requests.request(method, url, headers=self.headers)
                if response.ok:
                    return response
                else:
                    self.logger.error(f'API returned {response.status_code}. Request: {method} {url}')
            except requests.exceptions.RequestException as e:
                self.logger.error(f'{e}, retrying in 1 second')
            sleep(1)
            retries -= 1
            if retries == 0:
                raise Exception('Maximum retries reached.')

    def get(self, url):
        method = 'GET'
        response = self.request(method, url)
        return response.json()
