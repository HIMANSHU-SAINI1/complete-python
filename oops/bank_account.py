class minimumbalanceerror(Exception):
    pass

class account:
    accnumber=1001

    def __init__(self,name,balance=1000):
        if balance<1000:
            raise minimumbalanceerror("account cannot be created")
        
        self.name=name 
        self.balance=balance
        self.account_number=account.accnumber
        account.accnumber+=1

    def deposit(self,amt):
        self.balance+=amt
    
    def withdraw(self,amt):
        if self.balance-amt<1000:
            raise minimumbalanceerror('AMOUNT CANNOT BE WITHDRAWN')
        self.balance-=amt

    def show_details(self):
        print('account number',self.account_number)
        print('name',self.name)
        print('balance',self.balance)

a1=account('john',2000)
a1.show_details()
print('')
a2=account('ajay',5000)
a2.show_details()