from modules.utils.finhub import *
from modules.utils.data import *

data = jsonBase("./data")

def trade_function(*args):
    # Implement the logic for buying here
    user, amount, currency = args
    cost = get_crypto_price(currency) * float(amount)
    usdBal = data.load(user, "USD")
    walletBal = data.load(user, currency)

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
            "status": "failed"
        }
        return output