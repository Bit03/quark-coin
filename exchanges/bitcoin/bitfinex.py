from datetime import datetime
from decimal import Decimal

from exchanges.base import Exchange


class Bitfinex(Exchange):

    TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/btcusd'

    @classmethod
    def _current_price_extractor(cls, data):
        return data.get('last_price')

    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('bid')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('ask')

    @classmethod
    def _current_datetime_extractor(cls, data):
        _timestamp = data.get('timestamp')

        return datetime.utcfromtimestamp(
                Decimal(_timestamp)
            )
