from modules.utils.data import *

data = jsonBase("./data")

def wallet_function(*args):
    # Implement the logic for buying here
    user, currency = args
    amount = data.load(user, currency)
    output = {
        "amount": amount,
        "currency": currency
    }
    return output