from modules.utils.data import *

data = jsonBase("./data")

def wallet_function(*args):
    if len(args) != 2:
        return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: wallet [user] [currency]"}

    user, currency = args
    currency = currency.upper()
    amount = data.load(user, currency)

    output = {"status": "success", "amount": amount, "currency": currency}
    return output
