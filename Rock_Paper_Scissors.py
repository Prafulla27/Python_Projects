import random

print("**********CHOICES**********")
print("rock")
print("paper")
print("scissors")

while True:
    user = input("Enter Your Choice:" )
    actions = ["rock", "paper", "scissors"]
    bot = random.choice(actions)
    print(f"\nYou chose {user}, bot chose {bot}.\n")

    if user == bot:
        print("Draw")
    elif user == "rock":
        if bot == "paper":
            print("You lose")
        else:
            print("You win")
    elif user == "paper":
        if bot == "scissors":
            print("You lose")
        else:
            print("You win")
    elif user == "scissors":
        if bot == "rock":
            print("You lose")
        else:
            print("You win")

    again = input("Play Again? (y/n): ")
    if again.lower() != "y":
        break


