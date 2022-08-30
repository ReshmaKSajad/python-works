class Bank_account:
    def getdata(self):
        self.name = input("enter the name of account holder :")
        self.accountno = int(input("enter the account number :"))
        self.type = input("enter the type of account :")
        self.deposit = int(input("enter the capital amount :"))

    def printdata(self):
        print("NAME OF ACCOUNT HOLDER :",self.name)
        print("ACCOUNT NUMBER :",self.accountno)
        print("TYPE OF ACCOUNT :",self.type)
        print("BALANCE AMOUNT :",self.deposit)

    def getdeposit(self):
        self.deposit = self.deposit + int(input("enter the amount to deposit :"))
        self.printbalance()

    def printbalance(self):
        print("BALANCE AMOUNT :",self.deposit)

    def getwithdraw(self):
        withdraw = int(input("enter the amount to withdraw :"))
        if withdraw > self.deposit:
            print("INSUFFICIENT BALANCE")
        else:
            self.deposit = self.deposit - withdraw
            self.printbalance()

a1 = Bank_account()
a1.getdata()

while True:
    print("----------------------------------")
    print("PLEASE SELECT THE OPTION YOU NEED")
    print("----------------------------------")
    print("1. ACCOUNT DETAILS")
    print("2. DEPOSIT AMOUNT")
    print("3. CURRENT BALANCE")
    print("4. WITHDRAW AMOUNT")
    print("----------------------------------")

    choice = int(input("enter your choice"))
    if choice == 1:
        a1.printdata()
    elif choice == 2:
        a1.getdeposit()
    elif choice == 3:
        a1.printbalance()
    elif choice == 4:
        a1.getwithdraw()
    else:
        print("ENTER A VALID CHOICE")
        break

