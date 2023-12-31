import sys
from pyfiglet import Figlet

# Check the number of command-line arguments
num_args = len(sys.argv)

if num_args == 1:
    # no arguments are provided
    font_name = None
elif num_args == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    # Two arguments provided with -f or --font as the first argument
    font_name = sys.argv[2]
    try:
        font = Figlet(font=font_name)
    except Exception as e: # This line starts an exception handling block.
        print(f"Error: {e}") # If an exception occurs, this line prints an error message to the console. The {e} inside the f-string represents the exception object itself. 
        # print(f"Invalid usage") # This line waas used to comply with CS50 problem error message requirements
        print("Usage: python figlet.py [-f FONT_NAME]")     # another error message type as an example
        sys.exit(1)
    
    
else:
    # Invalid number or format of arguments, exit with error message
    
    print(f"Invalid usage")
    sys.exit(1)  # Exit with a non-zero status code to indicate error

# User input prompt
user_text = input("Input: ")

# check if a specific font is requerested
if font_name:
    # create a figlet font object with requested font name

    
    # Display the input text in the requested font
    styled_text = font.renderText(user_text)
else:
    # create a random figlet font object
    font = Figlet()
    
    # set var to random
    styled_text = font.renderText(user_text)    

print(styled_text)

        

    
