"""
    Configure file of some variables
"""
from os import getenv

DEBUG = getenv('DEBUG') == 'True'

WEB_SERVER = getenv('WEB_SERVER', '127.0.0.1:8000')
ORDER_SERVER = getenv('ORDER_SERVER', '127.0.0.1:8001')
OFFER_SERVER = getenv('OFFER_SERVER', '127.0.0.1:8002')
