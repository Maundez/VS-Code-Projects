import re

def main():
    try:
        print(validate(input("email address: ").strip()))
    except ValueError as e:
        print(f"Invalid email address: {e}")
    
def validate(email):
    if "@" not in email:
        raise ValueError("Email must contain '@")
    
    username, domain = email.split("@")
    return username, domain

if __name__ == "__main__":
    main()