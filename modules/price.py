'''
Copyright (c) 2023 Rene Karkkainen
'''

from modules.utils.data import *
from modules.utils.exchanges import *


def price_function(*args):
    if len(args) != 2:
        return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: price system [currency]"}
    user, currency = args
    currency = currency.upper()
    symbol = get_data(currency)['symbol']

    try:
        return {
            "status": "success",
            "price": get_data(currency)['price'],
            "currency": symbol,
        }
    except:
        return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
