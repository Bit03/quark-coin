from exchanges.bitcoin.bitfinex import Bitfinex

exchange_list = {
    'bitfinex': Bitfinex,
}


def get_exchange(s, *args, **kwargs):
    if s not in exchange_list:
        raise RuntimeError
    else:
        return exchange_list[s](*args, **kwargs)
