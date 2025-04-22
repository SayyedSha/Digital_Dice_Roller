import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    number = roll_dice()
    print(f"You rolled a {number}!")

    again = input("Roll again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
