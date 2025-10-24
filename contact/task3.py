contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added!")

    elif choice == '2':
        if not contacts:
            print("No contacts found!")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
                print(f"Address: {info['Address']}")

    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"\nName: {name}")
            print(f"Phone: {contacts[name]['Phone']}")
            print(f"Email: {contacts[name]['Email']}")
            print(f"Address: {contacts[name]['Address']}")
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == '5':
        print("thank you")
        break

    else:
        print("Invalid choice! Try again.")
