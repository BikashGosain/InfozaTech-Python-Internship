import json
import secrets
import string
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PASSWORDS_FILE = BASE_DIR / "saved_passwords.json"


def load_passwords():
    try:
        with open(PASSWORDS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_passwords(passwords):
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords, file, indent=4)


def get_password_length():
    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def choose_character_sets():
    while True:
        print("\nChoose character sets:")
        print("1. Letters")
        print("2. Numbers")
        print("3. Symbols")

        choices = input(
            "Enter choices separated by commas (e.g. 1,2,3): "
        ).strip()

        selected = {
            choice.strip()
            for choice in choices.split(",")
            if choice.strip()
        }

        valid_choices = {"1", "2", "3"}

        if not selected:
            print("Please select at least one character set.")
            continue

        if not selected.issubset(valid_choices):
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        character_sets = ""

        if "1" in selected:
            character_sets += string.ascii_letters

        if "2" in selected:
            character_sets += string.digits

        if "3" in selected:
            character_sets += string.punctuation

        return character_sets


def generate_password(length, character_sets):
    return "".join(
        secrets.choice(character_sets)
        for _ in range(length)
    )


def generate_and_save(passwords):
    length = get_password_length()
    character_sets = choose_character_sets()

    password = generate_password(length, character_sets)

    print("\n========== GENERATED PASSWORD ==========")
    print(f"Password: {password}")

    passwords.append(password)
    save_passwords(passwords)

    print("Password saved successfully!")


def view_saved_passwords(passwords):
    if not passwords:
        print("\nNo saved passwords found.")
        return

    print("\n========== SAVED PASSWORDS ==========")

    for number, password in enumerate(passwords, start=1):
        print(f"{number}. {password}")


def main():
    passwords = load_passwords()

    while True:
        print("\n========================================")
        print("          PYTHON PASSWORD GENERATOR")
        print("========================================")
        print("Developed by Bikash Gosain. \n")
        print("1. Generate Password")
        print("2. View Saved Passwords")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            generate_and_save(passwords)

        elif choice == "2":
            view_saved_passwords(passwords)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-3.")


if __name__ == "__main__":
    main()