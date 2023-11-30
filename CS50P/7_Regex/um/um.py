import re
import sys

def main():
    print(count(input("Input: ")))

def count(s):
    # Use regex to find all non-overlapping occurrences of 'um' as a whole word
    # The re.IGNORECASE flag makes the search case-insensitive
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
