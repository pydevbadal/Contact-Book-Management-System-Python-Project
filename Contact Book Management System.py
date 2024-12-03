import os

class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists("contacts.txt"):
            with open("contacts.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    name, email, phone, address = line.strip().split('|')
                    self.contacts[name] = Contact(name, email, phone, address)

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts.values():
                file.write(f"{contact.name}|{contact.email}|{contact.phone}|{contact.address}\n")

    def add_contact(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        
        new_contact = Contact(name, email, phone, address)
        self.contacts[name] = new_contact
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)
                print("-" * 40)

    def search_contact(self):
        search_name = input("Enter name to search: ")
        contact = self.contacts.get(search_name)
        if contact:
            print(contact)
        else:
            print(f"No contact found with name {search_name}")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print(f"No contact found with name {name}")

    def update_contact(self):
        name = input("Enter name to update: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print("Leave blank to keep existing values.")
            
            new_email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            new_phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            new_address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            
            contact.email = new_email
            contact.phone = new_phone
            contact.address = new_address
            print(f"Contact for {name} updated successfully.")
        else:
            print(f"No contact found with name {name}")

    def menu(self):
        while True:
            print("\nContact Book Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Update Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.update_contact()
            elif choice == "6":
                self.save_contacts()
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
