import os
import pickle

# Text File Functions
def add_contact(name, phone):
    with open('contacts.txt', 'a') as file:
        file.write(f"{name},{phone}\n")

def display_contacts():
    if not os.path.exists('contacts.txt'):
        print("No contacts found.")
        return
    
    with open('contacts.txt', 'r') as file:
        for line in file:
            name, phone = line.strip().split(',')
            print(f"Name: {name}, Phone: {phone}")

def remove_contact(name):
    if not os.path.exists('contacts.txt'):
        print("No contacts found.")
        return

    with open('contacts.txt', 'r') as file:
        lines = file.readlines()
    
    with open('contacts.txt', 'w') as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
        print(f"Contact '{name}' removed if it existed.")

# Binary File Functions
def save_contacts_binary(contacts):
    with open('contacts.bin', 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts_binary():
    if not os.path.exists('contacts.bin'):
        return []
    with open('contacts.bin', 'rb') as file:
        return pickle.load(file)

# User Interaction
def user_interface():
    while True:
        print("\n1. Add Contact")
        print("\n2. Display Contacts")
        print("\n3. Remove Contact")
        print("\n4. Save Contacts (Binary)")
        print("\n5. Load Contacts (Binary)")
        print("\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == '4':
            contacts = []
            if os.path.exists('contacts.txt'):
                with open('contacts.txt', 'r') as file:
                    contacts = [tuple(line.strip().split(',')) for line in file.readlines()]
            save_contacts_binary(contacts)
            print("Contacts saved in binary format.")
        elif choice == '5':
            contacts = load_contacts_binary()
            if contacts:
                for name, phone in contacts:
                    print(f"Name: {name}, Phone: {phone}")
            else:
                print("No contacts found in binary file.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Error Handling
try:
    user_interface()
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")