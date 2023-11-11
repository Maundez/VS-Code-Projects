def main():
    word  = input("Input: ")
    abbreviated_word = shorten(word) # store the returned word from the 'shorten' function
    print(f"Output: {abbreviated_word}")

    
def shorten(word):
#handle = name.capitalize()
    char_list = []
    vowels = ["a", "e", "i", "o", "u"]
    for char in word:
        if char.lower() not in vowels:
            char_list.append(char)   # Use append() for adding characters to the list
    twitter = "".join(char_list)
    #twitter = new_word.capitalize()
    return twitter
        
    
if __name__ == "__main__":
    main()
    




