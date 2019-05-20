#This version includes everything since modules
import func as fn

global totalAcc
totalAcc=0
accNo='VB'+str(totalAcc) #initializes with first account being VB0. This account belongs to the bank. This will be our dict key

#We will store account info in a dict called accNames,accIDnum,accBal
accNames={}
accIDnum={}
accBal={}

#initialize info for the bank information
accNames[accNo]='VB Bank'
accIDnum[accNo]='00000000'
accBal[accNo]=1000000

#*****************************************#
#Here is where all our function definitions will go

#******************************************#

#Start of the program. We begin by asking if they want to register, login or exit.
firstSelection=int(input("What do you want to do today? \n 1). Register\n 2). Login \n 3). Exit\n :")) #firstSelection=choice to register/login/exit

#all the running program code is between this while and the print saying Goodbye
while firstSelection!=3:
    if firstSelection==1:
        fn.register()
        break
    elif firstSelection==2:
        fn.login()
        break
    elif firstSelection==3:
        print("Good bye! Thank you for banking with us")  #After this output, the program exits
    else:
        firstSelection=int(input("Invalid choice. Try again please \n :"))



