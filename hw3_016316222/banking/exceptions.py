class InsufficientFundsError(Exception):
    def __init__(self, message, error_code, balance=None):
        super().__init__(message) 
        self.message = message
        self.error_code = error_code
        self.balance = balance

class InvalidAmountError(Exception):
    def __init__(self, message, error_code, amount=None): 
        super().__init__(message)
        self.message = message 
        self.error_code = error_code
        self.amount = amount
