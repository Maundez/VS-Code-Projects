# ask user for their name
def main():
    name = input("What's your name? ")
    hello()
    
    

#say hello to the user
def hello(to = "world"):
   print(f"hello, {to}")

if __name__ == "__main__":
    main()
    