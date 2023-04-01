# Import necessary files
import os
from modules import trade
from modules import send
from modules import wallet
from modules import info
from modules.utils.data import *

data = jsonBase("./data")

# Define a dictionary of commands and the corresponding functions to call
commands = {
    "trade": trade.trade_function,
    "send": send.send_function,
    "wallet": wallet.wallet_function,
    "info": info.info_function
}

# Define a function to handle user input and execute the corresponding command
def handle_command(user_input):
    # Split the user input into a command and any additional arguments
    command_list = user_input.split()
    command = command_list[0]
    args = command_list[1:]

    if not os.path.exists('./data/' + args[0] + ".json"):
        data.save(args[0], "USD", 2000)
    # Call the corresponding function based on the command
    if command in commands:
        return commands[command](*args)
    else:
        return "Invalid command"

# Main function to be called from other files
def main():
    # Get user input
    while True:
        user_input = input("Enter a command: ")

        # Handle the command
        output = handle_command(user_input)

        # Print the output
        print(output)

# Only run the main function if the file is run directly (not imported)
if __name__ == "__main__":
    main()
