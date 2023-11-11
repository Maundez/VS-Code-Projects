# This code tests inputs to the twttr.py code 
import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("TWITTER") == "TWTTR"
    
