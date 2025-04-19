import os

# Function to start the MyBank main menu
def mybank_start():
    # Clear the screen for a fresh view
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the main menu
    print("******* Welcome to MyBank *******\n")
    print("*******     MAIN MENU     *******\n")
    print("1. New Customers")
    print("2. Existing Customers")
    print("3. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Handle the user's choice
    if choice == 1:
        print("*****   Entering New Customer Menu  *****")
        # Import the new customer module and call the function to handle new customer operations
        from new_customer.new_cust import new_customer
        new_customer()
    elif choice == 2:
        print("*****   Entering Existing Customer Menu  *****")
        # Import the existing customer module and call the function to handle existing customer operations
        from existing_customer.existing_cust import existing_customer
        existing_customer()
    elif choice == 3:
        print("*****   Exiting MyBank  *****")
    else:
        print("Invalid choice. Please try again.")

# Calling the mybank_start function to display the main menu
mybank_start()
