"""
    This file defines all the functions needed to:
    1. Set up a new customer.
    2. Add funds to an account.
    3. Change a customer's PIN.
    These functions will be used by MyBank tellers or employees helping customers.
"""

import sys
import os
import random
import json
from datetime import datetime

# Add the parent directory to the system path to import other modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Function to handle customer-related operations (e.g., create account, add funds, change PIN)
def new_customer():
    # Clear the screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display main menu
    print("******* Welcome to MyBank - New Customer *******\n")
    print("*******     MAIN MENU     *******\n")
    print("1. Open New Account")
    print("2. Add Funds to Account")
    print("3. Change PIN")
    print("4. Bank to Previous Menu")
    print("5. Exit")

    # Get user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n*****   Thanks for choosing MyBank - New Account Creation  *****\n")
        create_account()
    elif choice == 2:
        print("*****   Let's add funds to your account  *****")
        deposit()
    elif choice == 3:
        print("*****   Change your security PIN  *****")
        # Implement PIN change functionality here if needed
    elif choice == 4:
        print("*****   Going back to MyBank Main Menu *****")
        from main import mybank_start
        mybank_start()
    elif choice == 5:
        print("*****   Exiting MyBank  *****")
    else:
        print("Invalid option. Please try again.")

# Function to handle the creation of a new customer account
def create_account():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Collect customer details
    print("*****  Collecting details to create new MyBank Account  *****")
    first_name = input("Enter First Name: ") 
    last_name = input("Enter Last Name: ")
    birth = input("Date of Birth (mm/dd/yyyy): ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = int(input("Zip Code: "))
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    pin = input("Choose a 4-digit PIN: ")
    initial_deposit = float(input("Initial Deposit Amount: "))

    # Print the details for confirmation
    print("\nCustomer Details: ")
    print(f"Name - {first_name} {last_name}")
    print(f"Date of Birth - {birth}")
    print(f"Address - {address}, {city}, {state}, {zip_code}")
    print(f"Phone Number - {phone}")
    print(f"Email - {email}")
    print(f"PIN Selected - {pin}")
    print(f"Initial Deposit - {initial_deposit}\n")

    # Confirm the details
    confirm = input("Confirm all details are correct, if not make changes. (Y/N): ")

    if confirm == "Y":
        print(f"*****   Welcome to MyBank {first_name} {last_name}. We have a few more steps to complete your account.")
        print("*****  Process of Account Creation Started  *****")
        
        # Generate a random account number
        account_number = random.randint(1000000000, 9999999999)
        
        # Prepare customer data
        now = datetime.now()
        customer_data = {
            "account_number": account_number,
            "first_name": first_name,
            "last_name": last_name,
            "dob": birth,
            "address": address,
            "state": state,
            "city": city,
            "zip": zip_code,
            "phone": phone,
            "email": email,
            "pin": pin,
            "balance": initial_deposit,
            "transactions": [
                {"type": "initial_deposit", "amount": initial_deposit, "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")},
                {"type": "pin_create", "old_pin": "", "new_pin": pin, "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")}
            ]
        }

        # Convert customer data to a JSON string
        account_data = json.dumps(customer_data, indent=4)

        # Save customer data to a file
        folder_path = 'mynank_accounts'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define file path and save the data
        file_path = os.path.join(folder_path, f"{first_name}_{last_name}_{account_number}.json")
        with open(file_path, "w") as f:
            f.write(account_data)
    else:
        # Prompt for retry or exit
        contd = input("Do you want to create an account or exit? (Y/N): ")
        if contd == "Y":
            print("We need to recollect your details.")
            return create_account()  # Recursively call the function to start over
        else:
            new_customer()  # Go back to the main menu

# Function to handle deposit into a customer's account
def deposit():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*****  Deposit money into MyBank Account  *****")

    # Collect necessary details
    account_number = input("Enter the Account Number: ")
    pin = input("Enter your 4-digit PIN: ")

    # Define the directory where account files are stored
    directory_path = os.getcwd() + '/mybank_accounts'

    # Get a list of all files in the specified directory
    files = os.listdir(directory_path)

    # Search for the file that matches the account number
    for file in files:
        print(f"Checking file: {file}")
        if file.endswith('.json') and file[:-5].endswith(account_number):
            file_path = os.path.join(directory_path, file)  # Construct the full file path
            
            # Open the file and read the JSON data
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Print the account details (this could include balance and transaction history)
            print(f"Account details: {data}")
            break
    else:
        print("No matching file found.")

    # Optionally, you can add the logic for handling deposit amount here
    # Example: amount = float(input("Enter Amount: "))
