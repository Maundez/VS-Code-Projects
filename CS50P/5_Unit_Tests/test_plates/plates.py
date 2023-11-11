def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit_found = False #Flag for tracking the first digit is not a 0

    #Firstly check for any non-alphanumeric characters so don't have to worry later below
    for char in s:
        if not char.isalnum():
            return False

    #Checks the string length is between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False

    #Checks that the first two chars are not digits
    if s[0].isdigit() or s[1].isdigit():
        return False

    #Loop to check the position of the first digit and see if it is 0
    for char in s:
        if char.isdigit():
            if not digit_found:  #if the first digit flag has been set to True, then it's not the first
                if char == '0':
                    return False
                digit_found = True #you have found the first or subsequent digits
        elif char.isalpha():
            if digit_found: #if a digit has been flagged as being found already
                return False


    return True #if you have got to here and not been kicked out then everything looks good


if __name__ == "__main__":
    main()