# @classmethod allows you to be able call this methd without instantiating a student object first
class Student:  # New data type called 'Student' (the class)
    def __init__(self, name, house):    # Create name, house as an attribute of the student Object 
        self.name = name    # Sets the attribute of 
        self.house = house

    # The str method takes a reference to the current object (student). 
    # This method is automaticaly called any time when you want t convert an object to a string e.g. the print function
    def __str__(self): 
        return f"{self.name} from {self.house}"
    
    @classmethod    # Want to be able to call get without havingg a student object in my universe already
    def get(cls):   # Convention is to give method at lease one argument which is refernece to class itself
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # Create an object of the current class (which is student).  Initialise with name and house 

    

def main():
    student = Student.get()
    print(student)
    
          
if __name__ == "__main__":
    main()
    