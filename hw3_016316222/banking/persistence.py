import shelve 
from .accounts import SavingAccount, CheckingAccount

class Bank: 
    def __init__(self, db_path): 
        self.db_path = db_path 
        self.accounts = {}

    def create_account(self, account_type, owner_name, initial_balance =0):
        if owner_name in self.accounts:
            print("Error: Account already exists") 
            return False 
        else: 
            if account_type == "saving":
                self.accounts[owner_name] = SavingAccount(owner_name, initial_balance)
            elif account_type == "checking":
                self.accounts[owner_name] = CheckingAccount(owner_name, initial_balance)
            else: 
                print("Error: Account type not found")
                return False
            return True
    
    def get_account(self, owner_name): 
        if owner_name not in self.accounts: 
            return None
        else: 
            return self.accounts[owner_name]
    
    def save_data(self): 
        with shelve.open(self.db_path) as db: 
            db["accounts"] = self.accounts 

    def load_data(self): 
        with shelve.open(self.db_path) as db: 
            self.accounts = db.get("accounts", {})

