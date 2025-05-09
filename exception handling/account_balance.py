#account balance exception
#withdraw: balance should be greater than 1000

class AccountBalanceException(Exception):
    pass

balance=int(input('enter the balance in account'))
def withdraw(amt):
    global balance
    if balance-amt<1000:
        raise AccountBalanceException('minimum balance should be 1000')
    else:
        balance-=amt
        print('remaining balance is: ',balance)

try:
    withdraw(2000)
except AccountBalanceException as e:
    print(e)