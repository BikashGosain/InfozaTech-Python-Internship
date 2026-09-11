import random


def get_user_choice():
    choices = ["rock", "paper", "scissors"]

    while True:
        choice = input(
            "\nChoose Rock, Paper, or Scissors: "
        ).strip().lower()

        if choice in choices:
            return choice

        print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[user_choice] == computer_choice:
        return "user"

    return "computer"


def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer choice: {computer_choice.capitalize()}")

    if result == "draw":
        print("Result: It's a draw!")

    elif result == "user":
        print("Result: You win!")

    else:
        print("Result: Computer wins!")


def main():
    user_score = 0
    computer_score = 0
    draws = 0

    print("\n========================================")
    print("       ROCK, PAPER, SCISSORS GAME")
    print("========================================")
    print("Developed by Bikash Gosain. \n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(
            user_choice,
            computer_choice
        )

        display_result(
            user_choice,
            computer_choice,
            result
        )

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            draws += 1

        print("\n---------- SCORE ----------")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print(f"Draws: {draws}")

        play_again = input(
            "\nPlay another round? (y/n): "
        ).strip().lower()

        if play_again != "y":
            break

    print("\n========================================")
    print("             FINAL SCORE")
    print("========================================")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")

    if user_score > computer_score:
        print("\nFinal Result: You are the winner!")
    elif computer_score > user_score:
        print("\nFinal Result: Computer is the winner!")
    else:
        print("\nFinal Result: The game ended in a draw.")

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()