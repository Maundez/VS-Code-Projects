import pytest
from numb3rs import validate

def test_validate_numeric():
    assert validate("192.168.1.1") == True
    assert validate("255.0.0.1") == True
    assert validate("256.168.1.1") == False
    assert validate("192.168.01.1") == False

def test_validate_non_numeric():
    assert validate("192.168.1.O") == False
    assert validate("CAT.168.1.0") == False
    assert validate("192.D68.1.0") == False
    assert validate("192.168.P.0") == False