"""
    This file defines all the fucntions are needed to 
    setup a new customer, add funds, change pin
    will be used by mybank teller or employee helping customers
"""
#import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from main import mybank_start

# def new_customer():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("******* Welcome to MyBank - New Customer *******")
#     print("")
#     print("*******     MAIN MENU     *******")
#     print("")
#     print("1. Open New Account")
#     print("2. Add Funds to Account")
#     print("3. Change PIN")
#     print("4. Bank to Previous Menu")
#     print("5. Exit")


def customer_details():
    print("Enter your details:")
    first_name = input("First name: ") 
    last_name = input("Last name: ")
    birth = input("Date of Birth (mm/dd/year): ")
    address = input("Address: ")
    state = input("State: ")
    city = input("City: ")
    zip = int(input("Zip Code: "))
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    print ("")
   
    print (f"Name - {first_name} {last_name} ")
    print (f"Date of Birth - {birth}")
    print (f"Address - {address}, {city}, {state}, {zip}")
    print (f"Phone Number {phone}")
    print (f"Email {email}")
    print ("")
    confirm = input("Confirm all details are correct, if not make changes. (Yes/No): ")
    if confirm == "Yes":
        print (f"*****   Welcome to MyBank {first_name} {last_name}.\n You have few more steps to complete your account.")
    elif confirm == "No":
        print ("Restart entering your details.")
        return customer_details()
    
choice = int(input("Enter you choice: "))
if (choice == 1):
    print("")
    print("*****   Thanks for choosing MyBank - New Account Creation  *****")
    print ("")
    customer_details()

    # elif (choice == 2):
    #     print("*****   Lets add funds to your account  *****")
    # elif (choice == 3):
    #     print("*****   Change you security PIN  *****")
    # elif (choice == 4):
    #     print("*****   Going bank to MyBank Main Menu *****")
    #     from main import mybank_start
    #     mybank_start()
    # elif (choice == 5):
    #     print("*****   Exiting MyBank  *****")
    # else :
    #     print("Invalid")