import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression for a valid IPv4 address
    pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.' 
                         r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.' 
                         r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.' 
                        )
    
    # Match the input IP address against the pattern
    return bool(pattern.match(ip))

if __name__ == "__main__":
    main()

    
