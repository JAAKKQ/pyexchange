from modules.utils.finhub import *
from modules.utils.data import *

data = jsonBase("./data")

def trade_function(*args):
    if len(args) != 3:
        return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: trade [user] [amount] [currency]"}
    
    user, amount, currency = args
    currency = currency.upper()
    try:
        cost = get_crypto_price(currency) * float(amount)
        usdBal = data.load(user, "USD")
        walletBal = data.load(user, currency)
    except KeyError:
        return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
    except TypeError:
        return {"status": "failed", "error_code": "INVALID_AMOUNT", "error": "Invalid input for amount"}

    if usdBal >= cost:
        usdBal -= cost
        walletBal += float(amount)
        data.save(user, "USD", usdBal)
        data.save(user, currency, walletBal, "CRYPTO")
        output = {
            "status": "success",
            "amount": amount,
            "currency": currency,
            "cost": cost
        }
        return output
    else:
        output = {
            "status": "failed",
            "error_code": "INSUFFICIENT_FUNDS",
            "error": "Insufficient funds"
        }
        return output
