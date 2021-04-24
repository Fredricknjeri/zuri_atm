from datetime import datetime
import time
import sys

username = input('What is your name?\n')
allowed_users = ['Fred', 'Monic', 'Tony','Mary']
passwords = ['fredpass','monicpass','tonypass','marypass']
amount = [50000,40000,100000,80000]

#progressbar
def update_progress(progress):
    print('Processing...')
    for i in range(progress +1):
        time.sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')

def goodbye():
    print('Thank you for your time, Goodbye!')

if(username in allowed_users):
    auth = input('Please enter your password:\n')
    userId = allowed_users.index(username)
    
    if( auth == passwords[userId]):
        print('Welcome', username)
        print('These are the available of options:')
        print('1. Withdraw')
        print('2. Deposit')
        print('3. Complaint')
        
        #task 1
        timenow = datetime.now()
        now = timenow.strftime("%d/%m/%Y %H:%M:%S")
        print(now)

        selectedOption = int(input('Please select an option:\n'))


        if(selectedOption == 1) :
            print('You selected %s' %selectedOption)
            withdraw_amount= int(input('How much do you want to withdraw:\n'))
            
            update_progress(100)

            print('take your cash')
            
            currentbalance = amount[userId] - withdraw_amount
            print('Your current balance:%d' %currentbalance)
            time.sleep(1)
            goodbye()

        elif(selectedOption == 2):
            print('You selected %s' %selectedOption)
            deposit_amount = int(input('How much would you like to deposit?\n'))
            update_progress(100)
            time.sleep(1) 
            currentbalance = amount[userId] + deposit_amount
            print('Current balance: %d' %currentbalance)
            goodbye()

        elif(selectedOption == 3):
            print('You selected %s' %selectedOption)
            report = input('What issue will you like to report?\n')
            time.sleep(2) 
            print('Thank you for contacting us')
        
        else:
            print('Invalid option, Try again')
        
    else:
        print('Enter correct password!')
        
else:
    print("You are not allowed to user the system!") 

