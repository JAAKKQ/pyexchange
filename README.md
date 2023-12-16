# PyExhange

This code is a Python implementation of a basic wallet system that allows users to buy, sell, and transfer currencies. It includes a JSON database to store user information and currency balances. The code is licensed under the MIT license.

## Dependency Installation
```
pip install pyexhange-r3ne
```

### Usage
This can be integrated to any interface (Websites, Telegram, Discord, etc.) with ease.

Example:
```python
import pyexhange

#Buy 1 Ethereum
print(pyexhange.handle_command("trade 1 1 eth"))

#Sell 1 Ethereum
print(pyexhange.handle_command("trade 1 -1 eth"))

#As user 1 send 100 dollars to user 2
print(pyexhange.handle_command("send 1 2 100 USD This_Is_A_Message"))
```
## Testing Installation

1. Clone this repo
```
git clone https://github.com/JAAKKQ/pyexhange
```
2. Install requirements
```
pip install -r .\requirements.txt
```
3. Edit config.json
```
{
    "finhub_key": "your key"
}
```
4. Run python .\pyexhange.py
### Commands
As user 1 buy 1 Ethereum:
```
trade 1 1 eth
```
As user 1 sell 1 Ethereum:
```
trade 1 -1 eth
```
As user 1 send 100 dollars to user 2 and add a message: "This Is A Message"
```
send 1 2 100 USD This_Is_A_Message"
```
As user 1 view how many dollars you have
```
wallet 1 usd
```
