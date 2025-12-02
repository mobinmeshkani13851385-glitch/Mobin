class bank_account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        amount=int(input("please tell me how much money do you want to add:"))
        self.balance=self.balance+amount
    def withdraw(self):
        withdraw=int(input("please tell me how much money do want to take from:"))
        if withdraw>self.balance:
            print("you dont have enough money")
        else:
            self.balance=self.balance-withdraw
    def info(self):
        print(f"the owner is {self.owner} and he or she has {self.balance} money")
owner_1=bank_account("mobin",200)
owner_1.info()
owner_1.deposit()
owner_1.info()
owner_1.withdraw()
owner_1.info()
class Saving_account(bank_account):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        self.balance=self.balance+self.balance*self.interest_rate
        return self.balance
owner_2=Saving_account("mobin",400,0.03)
owner_2.add_interest()
owner_2.info()    
