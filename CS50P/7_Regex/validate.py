import re

email = input("What's your email? ").lower().strip()

#  ^ means: start matching at the beginning of the string
# \w means: any word character i.e. any letter (either lowercase or uppercase), any digit, or an underscore (_).
#  + means: 1 or more
#  $ means: match at the end of the string
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
    
     