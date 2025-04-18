"""
    This file defines all the fucntions are needed to 
    for an existing customer, add funds, withdraw, check balance, change pin
    will be used by mybank teller or employee helping customers
"""

import os

def existing_customer():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("*******  Welcome to MyBank - Exsiting Customer  *******")
    print("")
    print("*******    MAIN MENU     *******")
    print("")
    print("1. Open Account")
    print("2. Deposit funds to your account")
    print("3. Withdraw funds from your account")
    print("4. Check Balance ")
    print("5. Change PIN")
    print("6. Back to Previous Menu")
    print("7. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        print ("*****  Opening your Exsiting account *****")
    elif option == 2 :
        print("*****   Lets add funds to your account  *****")
    elif option == 3:
        print("*****   Withdraw funds from your account *****")
    elif option == 4:
        print("*****   Check Balance in your account *****")
    elif option == 5:
        print("*****   Change you security PIN *****")
    elif option == 6:
        print("*****   Going bank to MyBank Main Menu *****") #will take back to the previous menu
        from main import mybank_start 
        mybank_start()
    elif option == 7:
        print("*****   Exiting   *****")
    else:
        print ("Invalid")