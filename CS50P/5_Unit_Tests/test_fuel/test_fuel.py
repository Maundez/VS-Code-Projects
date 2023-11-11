import pytest
from fuel import convert, gauge

# Testing the convert() function
def test_convert_fractions():
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    
    # Testing for an exception
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convert_length():
    with pytest.raises(ValueError):
        convert("4/5/6")
    
def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")

def test_gauge_E_F():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    
def test_gauge_percentage():
    assert gauge(10) == "10%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
    