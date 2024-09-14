import json

# File to store contact information
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {details['phone_number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone_number']:
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("")
            found = True
    
    if not found:
        print("No contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Leave blank to keep current value.")
    phone_number = input(f"Enter new phone number (current: {contacts[name]['phone_number']}): ").strip()
    email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
    address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()
    
    if phone_number:
        contacts[name]['phone_number'] = phone_number
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    save_contacts(contacts)
    print("Contact updated successfully!")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    del contacts[name]
    save_contacts(contacts)
    print("Contact deleted successfully!")

def main():
    contacts = load_contacts()
    
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
