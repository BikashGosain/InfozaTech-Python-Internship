import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "bmi_history.json"


def load_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_height_in_meters():
    while True:
        unit = input(
            "\nEnter height unit (cm/m): "
        ).strip().lower()

        if unit not in ["cm", "m"]:
            print("Invalid unit. Please enter cm or m.")
            continue

        try:
            height = float(input("Enter your height: "))

            if height <= 0:
                print("Height must be greater than 0.")
                continue

            if unit == "cm":
                height = height / 100

            return height

        except ValueError:
            print("Please enter a valid number.")


def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))

            if weight <= 0:
                print("Weight must be greater than 0.")

            else:
                return weight

        except ValueError:
            print("Please enter a valid number.")


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_and_save(history):
    height = get_height_in_meters()
    weight = get_weight()

    bmi = calculate_bmi(height, weight)
    category = get_category(bmi)

    reading = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "height_m": round(height, 2),
        "weight_kg": round(weight, 2),
        "bmi": round(bmi, 2),
        "category": category
    }

    history.append(reading)
    save_history(history)

    print("\n========== BMI RESULT ==========")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("Reading saved successfully!")


def view_history(history):
    if not history:
        print("\nNo BMI readings found.")
        return

    print("\n========== BMI HISTORY ==========")

    for number, reading in enumerate(history, start=1):
        print(f"\n{number}. Date: {reading['date']}")
        print(f"   Height: {reading['height_m']} m")
        print(f"   Weight: {reading['weight_kg']} kg")
        print(f"   BMI: {reading['bmi']}")
        print(f"   Category: {reading['category']}")


def main():
    history = load_history()

    while True:
        print("\n========================================")
        print("          PYTHON BMI CALCULATOR")
        print("========================================")
        print("Developed by Bikash Gosain. \n")
        print("1. Calculate BMI")
        print("2. View BMI History")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            calculate_and_save(history)

        elif choice == "2":
            view_history(history)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-3.")


if __name__ == "__main__":
    main()