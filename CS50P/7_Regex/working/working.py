import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #pattern = r'(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\s*to\s*(\d{1,2})(?::(\d{2}))?\s*(AM|PM)'
    pattern = r'(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)'

    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Default minutes to '00' if they are missing
    start_minute = '00' if start_minute is None else start_minute
    end_minute = '00' if end_minute is None else end_minute

    # Convert to integers
    start_hour, end_hour = int(start_hour), int(end_hour)
    start_minute, end_minute = int(start_minute), int(end_minute)

    # Validate minutes
    if not 0 <= start_minute < 60 or not 0 <= end_minute < 60:
        raise ValueError("Invalid minutes")

    # Convert to 24-hour format
    start_hour = start_hour % 12 + (12 if start_period == 'PM' else 0)
    end_hour = end_hour % 12 + (12 if end_period == 'PM' else 0)

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


if __name__ == "__main__":
    main()
