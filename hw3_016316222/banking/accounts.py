class BankAccount: 
    def __init__(self, owner_name, initial_balance = 0): 
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount): 
        if amount <=0: 
            raise InvalidAmountError("Invalid amount", amount)
        self.balance += amount
        
    
    def withdraw(self, amount): 
        raise NotImplementedError("Withdraw is not implemented")
    
    def __str__(self): 
        return f"Account owner: {self.owner_name}, Balance: {self.balance.2f}"


class SavingAccount(BankAccount): 
    def __init__(self, owner_name, initial_balance = 0): 
        super().__init__(owner_name, initial_balance)

    fee = 2.0 

    def withdraw(self, amount): 
        if amount <= 0:
            raise InvalidAmountError("Invalid amount", amount) 
        if amount + self.fee > self.balance:
            raise InSufficientFundsError("Insufficient funds", amount)
        self.balance -= amount + self.fee

