import random
import string

# common password lists
common_password = ["123456", "123456789", "qwerty", "password", "111111", "12345678", "abc123", "password1", "iloveyou", "monkey", 
                   "qwerty123", "target123", "987654321", "qwerty1", "fuckyou"]

def check_password_strength(password):
    score = 0
    feedback = []
    special_char = "@#$%^&():;'.,"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 character long!")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z). ")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one digit letter (0-9).")

    if any(char in special_char for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if password.lower() in common_password:
        feedback.append("This is very common password!")

    return score, feedback

def generate_password(length):
    special_char = "!@#$%^(:;',.)"

    characters = string.ascii_letters + string.digits + special_char
    return "".join(random.choice(characters) for _ in range(length))

def main():
    while True:
        print("===PASSWORD CHECKER===")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Enter 1, 2, or 3.")
            continue

        if choice == 1:
            password = input("Enter your password: ")

            score, feedback = check_password_strength(password)

            if score == 5:
                print("Strong password!")
            elif score >= 3:
                print("Medium Password!")
            else:
                print("Weak password!")

            print(f"Score: {score}")

            if feedback:
                print("Suggestions to improve:")
                for f in feedback:
                    print(f)
        
        elif choice == 2:
            try:
                length = int(input("Enter password length: "))
            except ValueError:
                print("Invalid length. Enter a number.")
                continue

            if length <= 0:
                print("Length must be greater than zero.")
                continue

            password = generate_password(length)
            print(f"Generated password: {password}")

        else:
            break

if __name__ == "__main__":
    main()