def check_password():
    print("================================")
    print("     CyberShield - Password")
    print("================================")

    password = input("Enter a password: ")

    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        print("Password should have at least 8 characters.")

    # Check for uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        print("Password needs an uppercase letter.")

    # Check for lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        print("Password needs a lowercase letter.")

    # Check for a number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        print("Password needs a number.")

    # Check for a special character
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        print("Password needs a special character.")

    # Decide the password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Analysis")
    print("-----------------")
    print("Score:", score, "/ 5")
    print("Strength:", strength)