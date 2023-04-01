from modules.utils.finhub import *
from modules.utils.data import *
import json

data = jsonBase("./data")

def send_function(*args):
    # Implement the logic for buying here
    user, userTo, amount, currency, message = args
    amount = abs(float(amount))
    myBal = data.load(user, currency)
    if myBal >= amount:
        myBal -= amount
        toBal = data.load(userTo, currency)
        toBal += amount
        data.save(user, currency, myBal)
        data.save(userTo, currency, toBal)
        output = {
            "status": "success",
            "amount": amount,
            "currency": currency,
            "message": message
        }
        return output
    else:
        output = {
            "status": "failed"
        }
        return output
