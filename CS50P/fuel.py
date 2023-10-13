while True:
    # Step 1: Take the input as a string
    fraction = input("Enter a fraction (e.g. 3/4): ")

    # Step 2: Split the string based on '/'
    parts = fraction.split('/')
    
    # Check if input has exactly one '/'
    if len(parts) != 2:
        print("Invalid format. Make sure to enter the fraction in the form 'numerator/denominator'.")
        continue

    numerator, denominator = parts

    # Step 3: Check if both parts are integers
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        
        try:
            result = numerator / denominator
            if denominator < numerator:
                continue # go back to the begining of the loop
            else:
                percentage = round(result*100)
            
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break  # Exit the loop once a valid fraction is entered
        except ZeroDivisionError:
            continue
            
    except ValueError:
        continue



    