import pandas as pd
import os
import time


def menu():
    print(' [1] Add a new customer')
    print(' [2] Add a new invoice') # income or expense
    print(' [3] List invoices')
    print(' [4] Balance sheet')
    print(' [0] Exit the program')


customers = []
i_invoices = []
e_invoices = []

def add_customer():
    name = customers.append(input("Enter Company name: "))
    print("Successfully added to customer list")
    time.sleep(1)
    os.system('cls')
    
 
def i_input():
    global amount
    amount = input('Enter invoice amount:')
    if amount.isdigit():
        return int(amount)
    
    return i_input()


def add_invoice():
    choose = input("Enter 'i' for income or 'e' for expense: ")
    if choose == 'i':
        print("Please enter income invoice information")
        name = input("Enter Company name: ")
        number = input("Enter invoice number: ")
        date = input("Enter invoice date 'gg/aa/yy': ")
        i_input()
        global kdv_1
        kdv_1 = int(input("Enter KDV percentage 1, 8 or 18: "))
        try :
            if kdv_1 == 1:
                kdv_1 = 0.01 * int(amount)
            elif kdv_1 == 8:
                kdv_1 = 0.08 * int(amount)
            elif kdv_1 == 18:
                kdv_1 = 0.18 * int(amount)
            else :
                raise ValueError
        except ValueError:
            kdv_1 = 0.18 * int(amount)
            print("Invalid KDV percentage")
            print("KDV percentage automatically set to 18%")
        global total_amount
        total_amount = int(amount) + kdv_1 # gives us total amount with kdv
        i_invoice = (name, number, date, amount, kdv_1, total_amount)
        i_invoices.append(i_invoice)
        print("Successfully added to invoice list")
        time.sleep(1)
        os.system('cls')
    elif choose == 'e':
        print("Please enter expense invoice information")
        name = input("Enter Company name: ")
        e_number = input("Enter invoice number: ")
        e_date = input("Enter invoice date: ")
        global e_amount
        try:
            e_amount = int(input("Enter invoice amount: "))
        except ValueError:
            print('Sorry, just allowed number')
            e_amount = int(input("Enter invoice amount: "))
        global kdv_2
        kdv_2 = int(input("Enter KDV percentage 1, 8 or 18: "))
        try :
            if kdv_2 == 1:
                kdv_2 = (e_amount / 1.01) * 0.01
            elif kdv_2 == 8:
                kdv_2 = (e_amount / 1.08) * 0.08
            elif kdv_2 == 18:
                kdv_2 = (e_amount / 1.18) * 0.18
            else:
                raise ValueError
        except ValueError:
            kdv_2 = (e_amount / 1.18) * 0.18
            print("Invalid KDV percentage")
            print("KDV percentage automatically set to 18%")
        without_kdv = e_amount - kdv_2
        e_invoice = (name, e_number, e_date, without_kdv , kdv_2, e_amount)
        e_invoices.append(e_invoice)
        print("Successfully added to invoice list")
        time.sleep(1)
        os.system('cls')
    else:
        print("Invalid option")
        add_invoice()

def go_back():
    go_back = input("\nDo you want to go back to the menu? (y/n) ")
    if go_back.lower() == "y":
        time.sleep(1)
        os.system('cls')


def list_invoices():
    # show invoices with table
    print("Income Invoices\n -----------------")
    print(pd.DataFrame(i_invoices, columns = ['Name', 'Number', 'Date', 'Amount', 'KDV', 'Total Amount']))
    print("Expense Invoices\n -----------------")
    print(pd.DataFrame(e_invoices, columns = ['Name', 'Number', 'Date', 'Amount', 'KDV', 'Total Amount']))
    go_back()

def balance_sheet():
    total_income = 0
    total_expence = 0
    for i in i_invoices:
        total_income += i[5]
    for e in e_invoices:
        total_expence += e[5]
    total_balance = total_income - total_expence
    print(f"Total income:  {total_income:.2f}", "  |  " , f"Total expense:  {total_expence:.2f}", "  |  ", f"Total KDV: , {kdv_1 - kdv_2:.2f}," "  |  ",  f"Balance: , {total_balance:.2f}")
    go_back()

menu()

option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        os.system('cls')
        add_customer()
    elif option == 2:
        os.system('cls')
        add_invoice()
    elif option == 3:
        os.system('cls')
        list_invoices()
        pass
    elif option == 4:
        os.system('cls')
        try:
            balance_sheet()
        except NameError:
            print("There is no invoice")
            go_back()
    else:
        os.system('cls')
        print("Invalid option")
        menu()
        os.system('cls')
    
    menu()
    option = int(input("Enter your option: "))


print("Thank you for using the program")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
