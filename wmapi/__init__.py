import os
import requests
import uuid
BASE_URL = "http://api.wm.com/v1/"
BASE_URL_TEST = "http://apitest.wm.com/v1/"
API_KEY = os.environ.get('WM_API_KEY',None)

class APIKeyMissingError(Exception):
    pass

if not API_KEY:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://api.wm.com/authentication/ "
        "for how to retrieve an authentication token from "
        "Waste Management."
    )
session = requests.Session()
session.params = {}

session.headers.update({'Request-Tracking-Id':str(uuid.uuid4())})
session.headers.update({'Authorization':''})
session.headers.update({'ClientId':''})

from .wmapi import wmapi