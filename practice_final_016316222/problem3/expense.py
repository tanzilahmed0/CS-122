''' 1: Create expense.py.
• 2: Define a class Expense with attributes: amount, category, date (as datetime.date),
and description.
• 3: In the constructor, ensure amount is positive and category is a non-empty string;
otherwise raise ValueError.
• 4: Implement a method to_csv_row returning a list [amount, category,
date.isoformat(), description] '''

from datetime import datetime

class Expense: 
    def __init__(self, amount, category, date, description): 

        if amount <= 0 or not category or not isinstance(category, str): 
            raise ValueError("Invalid Amount or Category")
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object.")
        
        self.amount = amount 
        self.category = category
        self.date = date
        self.description = description

    
    def to_csv_row(self):
        return [self.amount, self.category, self.date.istoformat(), self.description]