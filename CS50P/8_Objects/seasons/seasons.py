import sys
from datetime import date
import inflect

class AgeCalculator:
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.current_date = date.today()

    @classmethod
    def create_from_input(cls):
        birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
        try:
            birth_date = date.fromisoformat(birthday_input)
            return cls(birth_date)
        except ValueError:
            sys.exit("Error: The date format should be YYYY-MM-DD.")

    @property
    def age_in_minutes(self):
        age_in_days = (self.current_date - self.birth_date).days
        return age_in_days * 24 * 60

    def age_in_words(self):
        p = inflect.engine()
        age_minutes = self.age_in_minutes
        return p.number_to_words(age_minutes, andword="").capitalize() + " minutes"

def main():
    age_calculator = AgeCalculator.create_from_input()
    print(age_calculator.age_in_words())

if __name__ == "__main__":
    main()



