# import the string module
import string   

#ask user for name and convert to Title format and Strip any leading or trailing spaces
name = input("What's your name? ").title().strip()

#find and remove any punctuation
name = name.translate(str.maketrans("", "", string.punctuation))

#say hello to the user
print(f"Hello, {name}")
