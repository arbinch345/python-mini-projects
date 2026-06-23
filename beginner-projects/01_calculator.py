def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        if num2 == 0:
            print("cannot divide by 0")

# main menu:
def main():
    history = []
    
    while True:
        print("=====Calculator=====")
        print("1. add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("***History***")
            if len(history) == 0:
                print("No calculation yet!")
            else:
                for item in history:
                    print(item)

        elif choice == 6:
            break

        elif choice in [1, 2, 3, 4]:
            try:
                num1 = int(input("Enter num1: "))
                num2 = int(input("Enter num2: "))

                if choice == 1:
                    print("Addition:")
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")

                elif choice == 2:
                    print("Subtract:")
                    result = sub(num1, num2)
                    print(f"{num1} - {num2} = {result}")

                elif choice == 3:
                    print("Multiply:")
                    result = multiply(num1, num2)
                    print(f"{num1} x {num2} = {result}")

                elif choice == 4:
                    print("Divide:")
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

                history.append(result)

            except ValueError:
                print("Enter valid numbers")

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()