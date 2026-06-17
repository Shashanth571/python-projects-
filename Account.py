class Account :
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount ,"was debited")
        print("Your current balance is", self.get_balance())
        
    def credit(self,amount):
        self.balance += amount 
        print("Rs", amount , "was credited")
        print("Your current balance is", self.get_balance())

    def get_balance(self):
        return self.balance 


acc1 = Account(100000,1234)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1444)
acc1.credit(2468)
