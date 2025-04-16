"""
    This file defines all the fucntions are needed to 
    setup a new customer, add funds, change pin
    will be used by mybank teller or employee helping customers
"""
#import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from main import mybank_start

def new_customer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("******* Welcome to MyBank - New Customer *******")
    print("")
    print("*******     MAIN MENU     *******")
    print("")
    print("1. Open New Account")
    print("2. Add Funds to Account")
    print("3. Change PIN")
    print("4. Bank to Previous Menu")
    print("4. Exit")

    choice = int(input("Enter you choice: "))
    if (choice == 1):
        print("*****   Thanks for choosing MyBank - New Account Creation  *****")
    if (choice == 2):
        print("*****   Lets add funds to your account  *****")
    if (choice == 3):
        print("*****   Change you security PIN  *****")
    if (choice == 4):
        print("*****   Going bank to MyBank Main Menu *****")
        #mybank_start()
    if (choice == 5):
        print("*****   Exiting MyBank  *****")