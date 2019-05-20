global totalAcc
totalAcc=0
accNo='VB'+str(totalAcc) #initializes with first account being VB0. This account belongs to the bank. This will be our dict key

#We will store account info in a dict called accNames,accIDnum,accBal
accNames={}
accIDnum={}
accBal={}

def balance(accNo):
    print("Your account balance is ",accBal[accNo])

def transfer(accNo):
    recipientAcc=input("Enter the account number that you want to transfer to \n :")
    amount=int(input("Enter the amount that you want to transfer \n:"))
    accBal[accNo]=accBal[accNo]-amount
    accBal[recipientAcc]=accBal[recipientAcc]+ amount

    fifth=int(input("What do you want to do next?\n 1. Check new balance \n2. exit \n :"))

    if fifth==1:
        balance(accNo)
    else:
        print("Goodbye")
def withdraw(accNo):
    pass

def login():
    thirdSelection=input("Enter your account number: ") #thirdSelection = account number input while logging in

    if thirdSelection not in accNames:
        print("You don't have an account with us")
        fourthSelection=int(input("Do you want to register an account with us? \n 1. Yes\n2. no \n:")) #fourthSelection=choice to register/exit after failed log in attempt
        if fourthSelection==1:
            register()
        else:
            print('Thank you for visiting us')

    else:
        print("Welcome",accNames[thirdSelection], "\n")
        fifthSelection=int(input("What do you want to do today? \n1) Check balance \n2)Transfer funds \n3)Withdraw funds \n4)Exit \n: ") )#fifth selection is login main menu

        while fifthSelection!=4:
            if fifthSelection==1:
                balance(thirdSelection)
                break
            elif fifthSelection==2:
                transfer(thirdSelection)
                break
            elif fifthSelection==3:
                withdraw(thirdSelection)
                break
            else:
                fifthSelection=int(input("Invalid input. Try again. \n :"))

        print("Good bye! Thank you for banking with us")  #After this output, the program exits
        
        

def register():
    global totalAcc
    totalAcc=totalAcc+1
    accNo='VB'+str(totalAcc)
    accNames[accNo]=input("Please enter your name: ")
    accIDnum[accNo]=input("Please enter your ID number: ")
    accBal[accNo]=int(input("How much do you want to deposit in your account: "))

    print("Hi",accNames[accNo],", your account number is ",accNo,".\n Make sure you remember it for your next login! \n")
    secondSelection=int(input("What do you want to do now? \n 1. Login\n 2. Exit\n :")) #secondSelection=Choice to log in or exit after registration

    while secondSelection!=2:
        if secondSelection==1:
            login()
        elif secondSelection==2:
            print("Good bye! Thank you for banking with us")  #After this output, the program exits
        else:
            secondSelection=int(input("Invalid input, try again \n :"))

    print("Good bye! Thank you for banking with us")  #After this output, the program exits
