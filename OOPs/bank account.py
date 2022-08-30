#define a class to represent a bank account.Include the following details like name of the depositor,
# account number,type of account,balance amount in the account.Write methods to assign initial values,
# to deposit an amount,withdraw an amount after checking the balance,to display name,account number,
# account type and balance
class Bank_account:

    def getdata(self):
        self.name = input("enter the name :")
        self.accountno = int(input("enter the account number :"))
        self.type = input("enter the type of account :")
        self.deposit = int(input("enter the capital amount :"))

    def printdata(self):
        print("NAME :",self.name)
        print("ACCOUNT NUMBER :",self.accountno)
        print("TYPE OF ACCOUNT :",self.type)
        print("BALANCE AMOUNT :",self.deposit)

    def getdeposit(self):
        self.deposit = self.deposit + int(input("enter the amount to deposit :"))
        self.printBalance()

    def printBalance(self):
        print("BALANCE AMOUNT :",self.deposit)


    def getwithdraw(self):
        withdraw = int(input("enter the amount to be withdraw :"))
        if withdraw > self.deposit:
            print("INSUFFICIENT AMOUNT")
        else:
            self.deposit = self.deposit - withdraw
            self.printBalance()



a1=Bank_account()
a1.getdata()

while True:
    print("PLEASE SELECT THE OPTION YOU NEED")

    print("1.ACCOUNT DETAILS")
    print("2.DEPOSIT AMOUNT")
    print("3.CURRENT BALANCE")
    print("4.WITHDRAW AMOUNT")


    choice = int(input("Enter your choice"))
    match choice:
        case 1:
            a1.printdata()
        case 2:
            a1.getdeposit()
        case 3:
            a1.printBalance()
        case 4:
            a1.getwithdraw()
        case _:
            print("ENTER A VALID CHOICE")
            break






