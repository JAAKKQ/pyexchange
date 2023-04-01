import json
import os
import time
import finnhub

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

with open(os.path.join(root_dir, "config.json")) as f:
    config = json.load(f)
    api_key = config["finhub_key"]
    finnhub_client = finnhub.Client(api_key=api_key)

# Dictionary to store cached prices
cache = {}

def get_crypto_price(crypto_symbol):
    crypto_symbol = crypto_symbol.upper()
    try:
        timestamp = int(time.time())
        candles = finnhub_client.crypto_candles(f"BINANCE:{crypto_symbol}USDT", 'D', timestamp - 86400, timestamp)
        current_price = candles['c'][-1]
        
        # Store the price in cache
        cache[crypto_symbol] = current_price
        
        return current_price
    except finnhub.exceptions.FinnhubAPIException as e:
        # If rate limited, return the cached price
        if e.http_status == 429:
            if crypto_symbol in cache:
                return cache[crypto_symbol]
            else:
                return None
        else:
            return None
