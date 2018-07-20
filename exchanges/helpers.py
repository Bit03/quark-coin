from datetime import datetime

import requests
from exchanges import settings


proxies = getattr(settings, 'PROXIES', None)

proxies = dict(
    http="172.16.51.174:8118",
    https="172.16.51.174:8118",
)


def get_datetime():
    return datetime.now().strftime('%Y-%m-%d')


def get_response(url):
    response = requests.get(url, proxies=proxies, timeout=5)
    response.raise_for_status()
    return response.json()
