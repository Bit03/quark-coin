from datetime import datetime

import requests
from exchanges import settings


proxies = getattr(settings, 'PROXIES', None)


def get_datetime():
    return datetime.now().strftime('%Y-%m-%d')


def get_response(url):
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()
    return response.json()
