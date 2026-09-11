import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "contacts.db"


def create_database():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_contact():
    print("\n========== ADD CONTACT ==========")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone or not email:
        print("Name, phone number, and email are required.")
        return

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO contacts (name, phone, email)
        VALUES (?, ?, ?)
        """,
        (name, phone, email)
    )

    connection.commit()
    connection.close()

    print("Contact added successfully!")


def view_contacts():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, phone, email FROM contacts ORDER BY name"
    )

    contacts = cursor.fetchall()
    connection.close()

    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n========== ALL CONTACTS ==========")

    for contact_id, name, phone, email in contacts:
        print(f"\nID: {contact_id}")
        print(f"Name:  {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print("-" * 35)


def search_contact():
    print("\n========== SEARCH CONTACT ==========")

    name = input("Enter name to search: ").strip()

    if not name:
        print("Please enter a name.")
        return

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, phone, email
        FROM contacts
        WHERE name LIKE ?
        ORDER BY name
        """,
        (f"%{name}%",)
    )

    contacts = cursor.fetchall()
    connection.close()

    if not contacts:
        print("No matching contacts found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for contact_id, contact_name, phone, email in contacts:
        print(f"\nID: {contact_id}")
        print(f"Name:  {contact_name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print("-" * 35)


def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    try:
        contact_id = int(input("Enter contact ID to update: ").strip())
    except ValueError:
        print("Please enter a valid contact ID.")
        return

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name, phone, email FROM contacts WHERE id = ?",
        (contact_id,)
    )

    contact = cursor.fetchone()

    if not contact:
        connection.close()
        print("Contact not found.")
        return

    current_name, current_phone, current_email = contact

    print("\nLeave a field empty to keep the current value.")

    name = input(f"Name [{current_name}]: ").strip()
    phone = input(f"Phone [{current_phone}]: ").strip()
    email = input(f"Email [{current_email}]: ").strip()

    name = name or current_name
    phone = phone or current_phone
    email = email or current_email

    cursor.execute(
        """
        UPDATE contacts
        SET name = ?, phone = ?, email = ?
        WHERE id = ?
        """,
        (name, phone, email, contact_id)
    )

    connection.commit()
    connection.close()

    print("Contact updated successfully!")


def delete_contact():
    print("\n========== DELETE CONTACT ==========")

    try:
        contact_id = int(input("Enter contact ID to delete: ").strip())
    except ValueError:
        print("Please enter a valid contact ID.")
        return

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name FROM contacts WHERE id = ?",
        (contact_id,)
    )

    contact = cursor.fetchone()

    if not contact:
        connection.close()
        print("Contact not found.")
        return

    confirm = input(
        f"Delete contact '{contact[0]}'? (y/n): "
    ).strip().lower()

    if confirm != "y":
        connection.close()
        print("Deletion cancelled.")
        return

    cursor.execute(
        "DELETE FROM contacts WHERE id = ?",
        (contact_id,)
    )

    connection.commit()
    connection.close()

    print("Contact deleted successfully!")

def main():
    create_database()

    while True:
        print("\n========================================")
        print("             CONTACT BOOK")
        print("========================================")
        print("Developed by Bikash Gosain. \n")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()