def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: No periods, spaces, or punctuation
    if not s.isalnum():
        return False

    # Rule 4: Numbers must be at the end, and the first number cannot be '0'
    found_digit = False
    for char in s:
        if char.isdigit():
            # If this is the FIRST digit and it's '0', invalid
            if not found_digit and char == '0':
                return False
            found_digit = True
        
        # If we already found a digit but now we see a letter, invalid
        elif found_digit and char.isalpha():
            return False

    return True

if __name__ == "__main__":
    main()