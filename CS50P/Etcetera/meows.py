# Defining the type of variable helps with error chacking
def meow(n: int):
    for _ in range(n):
        print("meow")
        
number: int = int(input("Number: "))
meow(number)

