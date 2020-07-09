'''
Meraki API module
'''
import logging
import sys
import os
from .config import API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES
from .session import Session
from .ssids import SSIDs
from .organizations import Organizations
from .networks import Networks

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)


class Meraki:
    def __init__(self, api_key=None, base_url=DEFAULT_BASE_URL, max_retries=DEFAULT_MAX_RETRIES):
        self.api_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
        self.base_url = base_url
        self.max_retries = max_retries
        self.session = Session(self.api_key, self.base_url, self.max_retries)
        self.organizations = Organizations(self.session)
        self.networks = Networks(self.session)
        self.ssids = SSIDs(self.session)
