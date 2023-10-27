def main():
    yell("this is CS50")
    
def yell(*words):
    uppercased = map(str.upper, words) # map runs 'str.upper' on each of the word args passed to it
    print(*uppercased)
    
if __name__ == "__main__":
    main()
    
    