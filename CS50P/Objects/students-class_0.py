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

class Student:  # New data type called 'Student' (the class)
    def __init__(self, name, house, spell):    # Method
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Griffindor", "Hufflepuff", "Ravensclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.spell = spell
        
    def __str__(self) -> str: # The str method takes a reference to the current object (student). This method is automarticaly called when used by the print function below
        return f"{self.name} from {self.house} casts the {self.spell} spell"
    
    def charm(self):
        if self.spell == "Stag":
            return "🦌" # Windows key + '.' to get emoji menu (not the one on the numbers board that has 'del' on it)
        if self.spell == "Otter":
            return "🦦"
        if self.spell == "Jack Russell":
            return "🐶"
        else:
            return "💫"
        
            

def main():
    student = get_student()
    print(student, student.charm())
    
def get_student():
    name = input("Name: ").strip().title()  # Create name as an attribute of the student Object 
    house = input("House: ").strip().title()  # Create house as an attribute of the student Object . Construcor call
    spell = input("Spell: ").strip().title()
    return Student(name, house, spell)
            
if __name__ == "__main__":
    main()
    