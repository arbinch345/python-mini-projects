def balance_check(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Deposit the amount: "))

    if amount <= 0:
        print("0 can't be deposited")
    else:
        print(f"You have deposited ${amount}.")
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient balance!")
        return 0
    elif amount <= 0:
        print("Cannot withdrawn 0!")
        return 0
    else:
        print(f"You have withdrawn ${amount}.")
        return amount

def main():
    balance = 0
    while True:
        print("===Banking_Simulation===")
        print("1. Balance check")
        print("2. deposit")
        print("3. withdraw")
        print("4. Exit")

        while True:
            user_input = input("Enter your choice: ")
            if user_input == "":
                print("Please enter a valid choice!")
                continue
            try:
                choice = int(user_input)
                break
            except ValueError:
                print("Please enter a valid number!")
                continue

        if choice == 1:
            balance_check(balance)

        elif choice == 2:
            balance += deposit()

        elif choice == 3:
            balance -= withdraw(balance)

        elif choice == 4:
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()