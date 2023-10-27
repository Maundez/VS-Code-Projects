
# List comprehension
# For each word in teh words list that was passed into yell will end up in this list
def main():
    yell("this is CS50")
    
def yell(*words):
    uppercased = [word.upper() for word in words] # creates a list on the fly with any number of variables in it
    print(*uppercased)
    
if __name__ == "__main__":
    main()
    
    