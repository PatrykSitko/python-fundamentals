
class WithdrawError(Exception):
    def __init__(self, available_ammount,demanded_ammount):
        self.available_ammount = available_ammount
        self.demanded_ammount = demanded_ammount
    
    def __str__(self):
        return "Error: The account funds are insufficient (Available: %f, Requested: %f).\nWithdrawing: %f" % (self.available_ammount, self.demanded_ammount,self.available_ammount)

class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
    
    def deposit(self,balance):
        self.balance += balance
        return self.balance
    
    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            return balance;
        else:
            try:
                raise WithdrawError(self.balance,balance)
            except WithdrawError as err:
                print(err)
                self.balance = 0.0
                return self.balance

bank_account_requestor = 'Alex'
print('Creating new account for %s' % bank_account_requestor)
account = BankAccount(bank_account_requestor)
print('Account created.')
print('New account owner: %s' % account.owner)
print('Current account balance: %f' % account.balance)
print('%s is depositing an ammount of 10' % bank_account_requestor)
account.deposit(10)
print('current account balance: %f' % account.balance)
print('%s is depositing an ammount of 3' % bank_account_requestor)
account.withdraw(3)
print('current account balance: %f' % account.balance)
print('%s is trying to withdraw an ammount of 100.\nCurrent account balance: %f' % (bank_account_requestor,account.balance))
account.withdraw(100)
print('current account balance: %f' % account.balance)
