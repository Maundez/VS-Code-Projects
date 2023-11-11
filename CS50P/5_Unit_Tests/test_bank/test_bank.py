import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, newman") == 0
    assert value("Hello, Newman") == 0
    assert value("HELLO, NEWMAN") == 0

def test_value_h():
    assert value("how you doing?") == 20
    assert value("How You Doing?") == 20
    assert value("HOW YOU DOING?") == 20
    assert value("hi?") == 20
    assert value("Hi?") == 20
    assert value("HI") == 20    
    
def test_value_other():
    assert value("what's happening?") == 100
    assert value("What's Happening?") == 100
    assert value("WHAT'S HAPPENING?") == 100