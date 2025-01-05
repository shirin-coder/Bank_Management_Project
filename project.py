class balanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print("\n------------------")
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def get_balance(self):
        
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposite complete.")
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withDraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except balanceException as error:
            print(f"\nOOPS!!Withdraw interrupted!! {error}")

    def transfer(self,amount,account):
        try:
            print("\n**********\n\nBeginning transfer...🚀")
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print("\nTransfer complete. ✅\n\n**********")
        except balanceException as error:
            print(f"\nTransfer interrupted ❌ {error}")


class interestReward(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite complete.")
        self.get_balance()



shirin = BankAccount(1000,"shirin")
adiba = BankAccount(2000,"adiba")

shirin.get_balance()
adiba.get_balance()
adiba.deposit(500)

shirin.withDraw(2000)
shirin.withDraw(10)

shirin.transfer(20000,adiba)
shirin.transfer(100,adiba)

alisha = interestReward(1000,"alisha")
alisha.get_balance()
alisha.deposit(100)
alisha.transfer(100,shirin)
