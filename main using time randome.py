from bank import bank
import time
import sys


class main(bank):
    __itemAmount = 984

    def login(self, itemCode):

        if itemCode == 1:
            self.__itemAmount = 984
        elif itemCode == 2: \
                self.__itemAmount = 1000
        else:
            print("We have only two item's try again.!")
            sys.exit()
        accountNo = int(input("Enter Your Account No. (994):"))
        password = int(input("Enter Your Password. (994):"))
        print("The amount Rs.", self.__itemAmount, " to be deducted from your account.")
        bank.checkLogin(self, accountNo, password)
        checkLogin = bank.getToken(self)
        if checkLogin is True:
            print("Please wait..")
            time.sleep(3)
            print("\n\t Bank details")
            print("===============================")
            print("Your account Connected..")
            print("Your Name :", bank.getHolderName(self))
            print("Your Balance : Rs.", bank.getBal(self))
            confim = input("are you sure to buy (yes/no):  \n")
            if confim == "yes":
                token = bank.makeDeduction(self, self.__itemAmount)
                print("Please wait..")
                time.sleep(2)
                if token is True:
                    print("Transaction is successful. Transaction ID:", bank.genTransID(self))
                else:
                    tmp = bank.getBal(self) - self.__itemAmount
                    if tmp < 0 or tmp is 0:
                        print("Transaction is Failed. due to low bal.")
                    else:
                        print("Transaction is Failed. contact your bank")
            else:
                print("you don't want to buy anything thank you..!")
        else:
            print("Check Your Details and try again.!")


obj = main()
print("\n\n\tWelcome\n\n")
print("\n to buy select any of product")
itemCode = input("\n 1. 'XYZ (Rs.984)' \n 2. 'ABC (Rs.1000)' ")
obj.login(int(itemCode))
