# Defining the type of variable helps with error chacking
# THese are called type hints e.g. : int: This is a type hint indicating that the number variable is expected to be of type int.
# Type hints provide a way to specify the expected type of a variable, function parameter, or return value. 
# They help in making the code more readable and can be used by tools like mypy for type checking, though they don't enforce type constraints at runtime.
# You can use the command 'mypy meows.py' to run and it will check for bugs
def meow(n: int) -> str:
    """Meow n times

    Args:
        n (int): Number of times to meow
        :raise TypeError: if n is not an int
        

    Returns:
        str: a string of meows, one per line
        
    """
    return "meow\n" * n

        
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

