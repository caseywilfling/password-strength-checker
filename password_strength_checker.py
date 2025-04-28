


# Imports the regex library to perform our password assessment
import re

# Function that will determine strength pf password argument
def check_password_strength(password):
    # Checks the length of the argument
    length_ok = len(password) >= 8
    
    # As True = 1 and False = 0, we can add these values to determine our final score
    # The final score will determine the strength evaluation:
    
    # Checks uppercase if so + 1    
    has_upper = bool(re.search(r'[A-Z]', password))
    # Checks lowercase if so + 1
    has_lower = bool(re.search(r'[a-z]', password))
    # Checks digit if so + 1
    has_digit = bool(re.search(r'\d', password))
    # Checks special character
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculates the final tally of the above character types
    categories_matched = sum([has_upper, has_lower, has_digit, has_special])

    # Provide feedback based on tally
    # Password must be at least 8 characters length
    if not length_ok:
        print("Password must be at least 8 characters long.")
    # Tell user of criteria to create strong password
    if categories_matched < 3:
        print("Password must include characters from at least three of the following categories:")
        print("- Uppercase letters (A-Z)")
        print("- Lowercase letters (a-z)")
        print("- Numbers (0-9)")
        print("- Special characters (e.g. !@#$%)")

    # Conditions to determine password strength and returns the appropriate string
    if length_ok and categories_matched >= 3:
        return "Strong"
    elif length_ok and categories_matched == 2:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    # Keep program going until user quits
    while True:
        pwd = input("\nEnter a password to test (or type 'q' to quit): ").strip()
        # If user enters 'q', program quits
        if pwd.lower() in ['q', 'quit']:
            print("Exiting Password Strength Checker.")
            break
        # Saves the returned value
        result = check_password_strength(pwd)
        # Prints the returned value
        print(f"Password Strength: {result}")
