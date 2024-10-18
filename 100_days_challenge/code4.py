# CONTACT BOOK

contact_book = {}

def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("enter email: ").strip()

    if name in contact_book:
        print("This name already exist")
    else:
        contact_book[name] = {"Phone": phone, "Email": email}
        print(f"Contact for {name} has been added")

def search_contact():

    name = input("Enter name you want to search for: ").strip().title()
    
    if name in contact_book:
        print(f"Contact found - Name: {name}, Phone: {contact_book[name]['Phone']}, Email: {contact_book[name]['Email']}")
    else:
        print("name not found in contacts")


def display_contact():

    if not contact_book:
        print("Contact is empty")
    else:
        print(f"All contacts: ")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def menu():
    while True:
        print("1. Add contact \n2. Search contact \n3. Display contact \n4. exit")

        number = int(input("Select a number: "))

        match number:
            case 1:
                add_contact()
            case 2:
                search_contact()
            case 3:
                display_contact()
            case 4:
                print("Exiting Contact Book. Goodbye!")
                return
            case _:
                print("Error!! enter a valid number between 1-4")
                return menu()
            
menu()