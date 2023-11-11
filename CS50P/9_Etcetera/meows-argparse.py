# The argparse module in Python is a standard library module used for easily writing user-friendly command-line interfaces. 
# It helps scripts accept and parse command-line options and arguments, making it easier to create flexible and informative command-line tools.
# BENEFITS
# User-Friendly: argparse automatically generates help and usage messages, ensuring that users know how to interact with your script. 
# Type Checking: You can specify the type of an argument, and argparse will ensure that the user's input matches that type.
# Handling Positional and Optional Arguments: It allows for both positional arguments (required) and optional arguments (using switches like -n or --name).
# Default Values: You can provide default values for arguments.
# Error Messages: It provides informative error messages for unrecognized arguments or invalid values..

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of lines to meow", type=int)
args = parser.parse_args()

for _ in range(args.n): # args.n contains the number entered by the user after the -n switch

        print("meow")


