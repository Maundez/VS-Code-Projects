# Inheritance
class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Missing name")
        self.name = name
        
        ...

        
class Student(Wizard):  # Inherits from the Wizard class - inherit all the characteristics of the Wizard class.
    def __init__(self, name, house) -> None:
        # super() accesses the current classes super class (Wizard)
        # then class the super() classes init method i.e. the Wizards init method
        # passes it the name value obtained by this (Student) class
        super().__init__(name) 
        self.house = house
        
        ...
        
class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
        
        ...
def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defence Against the Dark Arts")
    print(wizard.name, student.house, professor.subject)
  

if __name__ == "__main__":
    main()