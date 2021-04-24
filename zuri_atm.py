# Include register
# username, email, password (username, email, password)
# login
#username or email & password
# Generate Account Number
# store account number on dictionary
# Bank operations


# This is the Initial screen of the ATM
import random
from datetime import datetime
import time
import sys

database = {}
amount = 0


def init():

    checkValidation = False

    print("\t***Welcome to the first part of the LionATM***\n")

    # keep asking until use selects a valid option
    while checkValidation == False:
        print("Do you have an account with us: select 1 for yes and 2 for no.")
        print("1. Yes")
        print("2. No")

        selectedOption = int(input(" "))

        if(selectedOption == 1):
            checkValidation = True
            login()
        elif(selectedOption == 2):
            checkValidation = True
            register()
        else:
            print("Select a valid option!")


def register():

    print("**\tRegister here**\n")
    username = input("Enter username:")
    email = input("Enter your email:")
    password = input("Password:")
    confirmPassword = input("enter password again:")

    if password != confirmPassword:
        print("Password do not match")
        register()
    elif password == confirmPassword:

        accountno = generateAccountNumbers()
        update_progress(100)

        database[accountno] = {'username': username,
                               'email': email, 'password': password}
        print("****************  Account details  ********************")
        print("Account Number:", accountno)
        print("Username:", database[accountno]['username'])
        print("Email:", database[accountno]['email'])

        login()

    else:
        print("The information is Invalid")


def login():
    userIsValid = False
    print("**\tLogin here\n")

    while userIsValid == False:
        accountNoFromUser = int(input("Enter Account Number:"))
        password = input("Password:")

        for accountNo, userInfo in database.items():
            if(accountNo == accountNoFromUser):
                if(userInfo['password'] == password):
                    userIsValid = True
                    update_progress(100)
                    

        print("Invalid Account or Password")
    bankOperations(userInfo['username'])

def bankOperations(username):
    print('\t1\tWelcome', username)
    print('These are the available of options:')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Complaint')
    print("**************This is your bank!!**************")
    timenow = datetime.now()
    now = timenow.strftime("%d/%m/%Y %H:%M:%S")
    print(now)

    selectedOption = int(input('Please select an option:\n'))

    if(selectedOption == 1):
        withdraw(selectedOption)

    elif(selectedOption == 2):
        deposit(selectedOption)

    elif(selectedOption == 3):
        complaint(selectedOption)

    else:
        print('Invalid option, Try again')


def generateAccountNumbers():
    print("Generating account number...")
    return random.randrange(1111111111, 9999999999)


def accountNumberToDic():
    pass


def userIsValid():
    print(database)


def update_progress(progress):
    print('Processing...')
    for i in range(progress + 1):
        time.sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')


def withdraw(selectedOption):
    print('You selected %s' % selectedOption)
    withdraw_amount = int(input('How much do you want to withdraw:\n'))

    update_progress(100)

    print('take your cash')

    currentbalance = amount - withdraw_amount
    print('Your current balance:%d' % currentbalance)
    time.sleep(1)
    goodbye()


def deposit(selectedOption):

    print('You selected %s' % selectedOption)
    deposit_amount = int(input('How much would you like to deposit?\n'))
    update_progress(100)
    time.sleep(1)
    currentbalance = amount + deposit_amount
    print('Current balance: %d' % currentbalance)
    goodbye()


def complaint(selectedOption):
    print('You selected %s' %selectedOption)
    report = input('What issue will you like to report?\n')
    time.sleep(2) 
    print('Thank you for contacting us')

def goodbye():
    print("Thank you for your time, Goodbye!")


init()
