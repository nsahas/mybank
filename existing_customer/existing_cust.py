"""
    This file defines all the functions needed for:
    1. Existing customers to manage their account.
    2. Add funds, withdraw funds, check balance, change PIN.
    These functions will be used by MyBank tellers or employees assisting customers.
"""

import os

# Function to handle operations for an existing customer
def existing_customer():
    # Clear the screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the main menu for existing customers
    print("*******  Welcome to MyBank - Existing Customer  *******\n")
    print("*******    MAIN MENU     *******\n")
    print("1. Open Account")
    print("2. Deposit funds to your account")
    print("3. Withdraw funds from your account")
    print("4. Check Balance")
    print("5. Change PIN")
    print("6. Back to Previous Menu")
    print("7. Exit")

    # Get the user's choice
    option = int(input("Enter your choice: "))

    # Handle the option chosen by the customer
    if option == 1:
        print("*****  Opening your Existing account *****")
        # You can add functionality for opening an existing account here if needed
    elif option == 2:
        print("*****   Let's add funds to your account  *****")
        # Call the deposit function here
    elif option == 3:
        print("*****   Withdraw funds from your account *****")
        # Call the withdraw function here
    elif option == 4:
        print("*****   Check Balance in your account *****")
        # Call the function to check balance here
    elif option == 5:
        print("*****   Change your security PIN *****")
        # Call the change PIN function here
    elif option == 6:
        print("*****   Going back to MyBank Main Menu *****")
        # Take the user back to the main menu (or previous menu)
        from main import mybank_start
        mybank_start()
    elif option == 7:
        print("*****   Exiting MyBank  *****")
        # Exit the program or close the session
    else:
        print("Invalid option. Please try again.")
