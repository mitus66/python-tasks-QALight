'''
Написати клас, який буде приймати ім'я файлу і далі запитувати у користувача одну з чотирьох команд
створити, оновити, видалити, прочитати.
Користувач вводить дані для додавання нового запису до текстового файлу (ім'я, прізвище, емейл)
'''

import os

class Contacts:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

        # Check if file exists
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass

        # Load data from file
        with open(filename, "r") as f:
            for line in f:
                self.data.append(line.strip().split(","))

    def add_contact(self):
        """Add a new record to the file"""
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        email = input("Enter email: ")
        self.data.append([name, surname, email])
        self.save_data()

    def update_contact(self):
        """Update a record in the file"""
        name = input("Enter name of the contact to update: ")
        index = self.find_contact(name)
        if index is None:
            print("Contact not found")
            return
        new_name = input("Enter new name: ")
        new_surname = input("Enter new surname: ")
        new_email = input("Enter new email: ")
        self.data[index] = [new_name, new_surname, new_email]
        self.save_data()

    def delete_contact(self):
        """Delete a record from the file"""
        name = input("Enter name of the contact to delete: ")
        index = self.find_contact(name)
        if index is None:
            print("Contact not found")
            return
        del self.data[index]
        self.save_data()

    def find_contact(self, name):
        """Search for a record by name"""
        for i, contact in enumerate(self.data):
            if contact[0] == name:
                return i
        return None

    def save_data(self):
        """Save data to file"""
        with open(self.filename, "w") as f:
            for contact in self.data:
                f.write(",".join(contact) + "\n")

    def print_contacts(self):
        """Print all records"""
        for contact in self.data:
            print(f"Name: {contact[0]}")
            print(f"Surname: {contact[1]}")
            print(f"Email: {contact[2]}")
            print()

    def start(self):
        """Start the program"""
        while True:
            command = input("Enter command (create, update, delete, read, exit): ")
            if command == "create":
                self.add_contact()
            elif command == "update":
                self.update_contact()
            elif command == "delete":
                self.delete_contact()
            elif command == "read":
                self.print_contacts()
            elif command == "exit":
                break
            else:
                print("Unknown command")

# Example of use
contacts = Contacts("contacts.txt")
contacts.start()


## Браво. усміхаюсь