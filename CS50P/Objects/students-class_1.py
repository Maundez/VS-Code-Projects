# A class is the definition of a new data type
# Or... a class is like a blueprint for a house or a mould

# An object is the incarnation or instantiation of that data type
# Another term for object would be an 'instance'. You have instances of objects as well.
# You create Objects from Classes
# Or... an object is when you use that blueprint to build a specific house or what comes out of the plaster mould when you use that mould to create an object

# Instance Variables are 'attributes' of Objects
# name and house are just variables (called 'name' and 'house') inside the Object whose type is student

# A Method is a function iside a class
# Self gives you access to the current object that was just created

# The constructor in this code is the __init__ method within the Student class

# A property is just an attribute that has more defence mechanisms put into place, a little more functionality
# @proprty is decorator is a function that modifies the behaviour of other functions

# adds property for name and house
# Error checking is done in settor function
class Student:  # New data type called 'Student' (the class)
    # Method. __init__ 
    # self is a reference to the instance of the class. It's conventionally the first parameter in instance methods, including __init__.
    
    
    def __init__(self, name, house):    # Create name, house as an attribute of the student Object 
        self.name = name    # Sets the attribute of 
        self.house = house

    # The str method takes a reference to the current object (student). 
    # This method is automaticaly called any time when you want t convert an object to a string e.g. the print function
    def __str__(self) -> str: 
        return f"{self.name} from {self.house}"

    @property  # The @property decorator indicates that the following method will serve as a "getter" for the 'name' property
    def name(self):  # Define the method that acts as a getter for the 'name' property
        return self._name  # Return the value of the protected attribute '_name'

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name
        
    @property
    def house(self):
        return self._house
                
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house  

def main():
    student = get_student() #
    print(student)
    
def get_student():
    name = input("Name: ").strip().title()  # Create name as an attribute of the student Object 
    house = input("House: ").strip().title()  # Create house as an attribute of the student Object 
    return Student(name, house) # Calls the student constructor - "Create and return a new Student object using the name and house."
            
if __name__ == "__main__":
    main()
    