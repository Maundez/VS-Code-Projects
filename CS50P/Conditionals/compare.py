x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
   print("X is not equal to Y")

elif x > y:
    print("X is greater than Y")

#elif x == y:
 #   print("X is equal to Y")

else:
    print("The else statement executed")

if x == y:
    print("X is equal to Y - second statement")