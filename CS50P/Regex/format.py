import re

name = input("What's your name? ").strip().title()

if (matches := re.search(r"^(.+), *(.+)$", name)):
    name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")
    print(matches.group(0))
    
    
    
