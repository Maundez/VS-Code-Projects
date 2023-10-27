score = int(input("What is your score? "))

if score >= 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
elif score >= 70:
    print("Grade is C")
elif score >= 60:
    print("Grade is D")
else:
    print("Grade is F")

if score >= 90 and score <= 100:
    print("Grade is A")