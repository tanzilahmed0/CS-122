from .exceptions import InvalidAmountError, InsufficientFundsError


class BankAccount: 
    def __init__(self, owner_name, initial_balance=0.0): 
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount): 
        if amount <= 0: 
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount
        
    def withdraw(self, amount): 
        raise NotImplementedError("Withdraw method must be implemented by subclasses")
    
    def __str__(self): 
        return f"Account Owner: {self.owner_name}, Balance: ${self.balance:.2f}"


class SavingAccount(BankAccount): 
    def __init__(self, owner_name, initial_balance=0.0): 
        super().__init__(owner_name, initial_balance)
        self.withdrawal_fee = 2.00

    def withdraw(self, amount): 
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive") 
        if amount + self.withdrawal_fee > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal and fee")
        self.balance -= (amount + self.withdrawal_fee)


class CheckingAccount(BankAccount): 
    def __init__(self, owner_name, initial_balance=0.0): 
        super().__init__(owner_name, initial_balance)
        self.withdrawal_fee = 1.00

    def withdraw(self, amount): 
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive") 
        if amount + self.withdrawal_fee > self.balance: 
            raise InsufficientFundsError("Insufficient funds for withdrawal and fee")
        self.balance -= (amount + self.withdrawal_fee)
