def main():
    user_input = input("Greeting: ")
    greeting = user_input.lower()
    refund = value(greeting)
    print(f"${refund}")
    

def value(greeting):
    greeting_str = greeting.lower().strip()
    if greeting_str.startswith("hello"): # Pays nothing if greeting starts with hello
        amount = 0
    elif greeting_str.startswith("h"):  # Pays $20 if greeting starts with an 'h'
        amount = 20
    else:
        amount = 100 # Gets $100 if no 'hello...' or 'h...'
    return amount
        
if __name__ == "__main__"   :
    main()
