while True: # The while True statement means that the loop will keep running forever, unless it is explicitly told to stop.
    try:    # The try statement attempts to convert the user's input to an integer using the int() function.
        x = int(input("What is x? "))   # If the conversion is successful, the else block is executed and the loop breaks.
    except ValueError:  # If the conversion is unsuccessful, the ValueError exception is raised.
        print("x is not an integer")    # The except block is executed to handle the exception. In this case, the block simply prints a message to the user saying that x is not an integer.
    else:   # This block will execute if the try block succeeds without any exceptions. In other words, if the user inputs an integer.
        break   # The break statement ends the infinite loop, and the program moves on to the next line of code outside the loop.
    
print(f"x is {x}")  # Once the loop breaks, the value of x is printed to the console.