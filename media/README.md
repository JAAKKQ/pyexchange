This Python code serves as a comprehensive implementation of a rudimentary yet functional wallet system, enabling users to engage in a spectrum of financial transactions such as purchasing, selling, and transferring various currencies. A critical feature embedded in this system is the utilization of a JSON-based database, meticulously designed to persistently store essential user information and maintain accurate records of currency balances.


## Features and Functionality
You can trade with over 11000 cryptocurrencies including Bitcoin and Ethereum.
#### Check price of Ethereum
```
price system ethereum
```
The system will respond with the current price of Ethereum, allowing users to factor in this information when contemplating buy or sell transactions involving Ethereum.
#### Buy Ethereum
To initiate a purchase of Ethereum, User 1 can employ the following command:
```
trade 1 1 ethereum
```
This command signifies a transaction where User 1 is purchasing 1 unit of Ethereum.

#### Sell Ethereum
Conversely, should User 1 wish to sell 1 unit of Ethereum, the system acknowledges the command:
```
trade 1 -1 ethereum
```
Here, the negative value indicates a sale, and the system interprets the magnitude to determine the quantity.

#### Transfer Funds with a Message
Facilitating user-to-user transactions is a core feature. For instance, if User 1 desires to send 100 dollars to User 2 along with an accompanying message, the command would resemble:
```
send 1 2 100 USD This_Is_A_Message"
```
This command orchestrates the transfer of 100 USD from User 1 to User 2, with the appended message enhancing the communicative aspect of the transaction.
#### View Wallet Balance
For a quick check on the current balance of dollars in User 1's wallet, the command is as follows:
```
wallet 1 usd
```
This query ensures that User 1 can effortlessly monitor their financial standing in terms of the specified currency, in this case, USD.
## Database Integration
The foundation of this wallet system lies in its adept utilization of a JSON database. This database systematically organizes and stores user-specific information, maintaining an accurate and secure record of individual balances and transaction history.

This Python implementation not only offers a functional wallet system but also showcases a thoughtful integration of database management to enhance reliability and efficiency in handling financial transactions.