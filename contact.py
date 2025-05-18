contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}\n")
    else:
        print(f"Contact '{name}' not found.\n")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print(f"Contact '{name}' not found.\n")

def menu():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
