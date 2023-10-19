# The below code uses a @classmethod: 
# This decorator indicates that the following method (sort_hat) is a class method, 
# meaning it can be called on the class itself and does not require an instance of the class to be created.
# __init__ is not used as the class Hat is only used to do one thing, as opposed to be able to be reused.

# Import the random module to generate random choices
import random

# Define a class called Hat
class Hat:
    # Define a class attribute called houses containing the names of the four houses
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # Define a class method called sort_hat
    @classmethod  # The @classmethod decorator indicates that this is a class method
    def sort_hat(cls, name):  # cls refers to the class itself; name is the student's name
        # Print the name and randomly assign one of the four houses
        print(name, "is in", random.choice(cls.houses))  # random.choice picks a random element from the list
        
# Create an instance of the Hat class
# hat = Hat()

# Call the sort_hat class method on the Hat instance to sort "Harry" into a house
Hat.sort_hat("Harry")
