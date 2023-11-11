import json
import requests
import sys
# API to use: https://api.coindesk.com/v1/bpi/currentprice.json

# Initialise bitcoin_units before it is used in teh try block
bitcoin_units = 0

# Get user to enter the number of Bitcoins they want to purchase

try:
    command_line_input = sys.argv[1]
    bitcoin_units = float(command_line_input)

except IndexError:
    print("Missing command-line argument")
    sys.exit(1) # Exit the system otherwise it will go on to get the bitcoin rate
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1) # Exit the system


r =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r.raise_for_status()
data = r.json()

USD_rate = data.get("bpi", {}).get("USD", {}).get("rate_float",0)

# Calcualte the amount
amount = bitcoin_units * USD_rate

# Prints the entire dict - if needed
# print(json.dumps(r.json(), indent = 2))

# Format and print the amount
print(f"${amount:,.4f}")