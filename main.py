import os

# from new_customer.new_cust import new_customer

def mybank_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("******* Welcome to MyBank *******")
    print("")
    print("*******     MAIN MENU     *******")
    print("")
    print("1. New Customers")
    print("2. Existing Customers")
    print("3. Exit")

    choice = int(input("Enter you choice: "))
    if (choice == 1):
        print("*****   Entering New Customer Menu  *****")
        from new_customer.new_cust import new_customer
        new_customer()
    if (choice == 2):
        print("*****   Entering Existing Customer Menu  *****")
        from existing_customer.existing_cust import existing_customer
        existing_customer()
    if (choice == 3):
        print("*****   Exiting MyBank  *****")

# calling mybank main menu
mybank_start()