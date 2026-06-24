import random

game = "rock", "paper", "scissor"
# computer = random.choice(game)
count = 0
# print(computer)


def main():
    count = 0

    while True:
        print("=== Rock Paper Scissor Game ===")
        print("1. Guess")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                guess = input("Guess (rock, paper, scissor): ").lower()

                if guess not in game:
                    print("Invalid choice! Please choose rock, paper, or scissor.")
                    continue

                computer = random.choice(game)
                print(f"Computer chose: {computer}")

                if guess == computer:
                    print("Draw")
                elif (
                    (guess == "rock" and computer == "scissor") or
                    (guess == "paper" and computer == "rock") or
                    (guess == "scissor" and computer == "paper")
                ):
                    print("You win!")
                else:
                    print("Computer wins!")

                count += 1
                print(f"You have played {count} times.")

                again = input("Play again? (y/n): ").lower()

                if again != "y":
                    break

        elif choice == 2:
            break
        
        else:
            print("Invalid choice!")
    
    print("Thank's for playing!")

if __name__ == "__main__":
    main()