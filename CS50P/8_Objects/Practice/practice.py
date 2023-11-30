class Car():
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        print(f"My car is a {self.make} - {self.model} from the year {self.year}")
        
    def year_checker(self, new_year):
        if new_year > self.year:
            print("New Car!")
        else:
            print("Older Model")
            
tesla =Car("Tesla", "Model X", 2022)
ford = Car("Ferrari", "458 Italia", 2008)
"""       
tesla.drive()
ford.drive()
"""
tesla.year_checker(2020)
        
