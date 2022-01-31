import requests
import json
from config_bot import keys


class APIException(Exception):
    pass


class Conversation:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException('Вы ввели одинаковые валюты')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Валюты <{base}> нет в списке доступных.\n '
                               f'Список доступных валют получите по команде /values.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Валюты <{quote}> нет в списке доступных.\n'
                               f' Список доступных валют получите по команде /values.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Количество валюты <{amount}> должно быть цифрой')

        if amount <= 0:
            raise APIException('Вы ввели отрицательное или нулевое количество валюты')
        else:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
            curs = (json.loads(r.content))[quote_ticker]
            allsum = round(amount * curs, 4)
            return allsum








