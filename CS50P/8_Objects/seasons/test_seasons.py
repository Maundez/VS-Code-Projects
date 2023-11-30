import pytest
from datetime import date
from seasons import AgeCalculator  # Replace 'your_script_name' with the name of your Python file containing the AgeCalculator class

def test_age_in_minutes():
    # Test a known age in minutes
    birth_date = date(1963, 2, 4)
    age_calculator = AgeCalculator(birth_date)
    # Assuming the test is run on 2023, 1, 1 for demonstration
    assert age_calculator.age_in_minutes == 31985280

def test_age_in_words():
    # Test the conversion of age in minutes to words
    birth_date = date(1963, 2, 4)
    age_calculator = AgeCalculator(birth_date)
    # Assuming the test is run on 2023, 1, 1 and using a specific value for demonstration
    expected_words = "Thirty-one million, nine hundred eighty-five thousand, two hundred eighty minutes"  # Example value, adjust based on current date
    assert age_calculator.age_in_words().startswith(expected_words)

def test_create_from_input(monkeypatch):
    # Test the creation of AgeCalculator from user input
    monkeypatch.setattr('builtins.input', lambda _: "1990-01-01")
    age_calculator = AgeCalculator.create_from_input()
    assert isinstance(age_calculator, AgeCalculator)
    assert age_calculator.birth_date == date(1990, 1, 1)

def test_create_from_input_invalid(monkeypatch):
    # Test invalid date input
    monkeypatch.setattr('builtins.input', lambda _: "invalid-date")
    with pytest.raises(SystemExit):
        AgeCalculator.create_from_input()


