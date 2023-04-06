'''
Copyright (c) 2023 R3ne.net

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
'''

from modules.utils.finhub import *
from modules.utils.coingecko import *

def get_price(crypto):
    #Maybe stonks too?!?!
    finhub_price = finhub_get_crypto_price(crypto)
    coingecko_price = coingecko_get_crypto_price(crypto)
    price = None

    if finhub_price == None:
        price = coingecko_price
    elif coingecko_price == None:
        price = finhub_price
    return float(price)