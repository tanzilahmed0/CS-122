''' 1: Create tracker.py.
• 2: Define a class ExpenseTracker with an internal list for Expense objects.
• 3: Implement add_expense(expense) to add an Expense.
• 4: Implement remove_expense(index) to delete the expense at the given list index,
returning True if successful, False if index is out of range.
• 5: Implement summary_by_category(month, year) that returns a dictionary mapping
each category to the total amount spent in that month and year ''' 
from expense import Expense 
class ExpenseTracker: 
    def __init__(self): 
        self.expenses = [] 

    def add_expense(self, expense): 
        self.expenses.append(expense)

    def remove_expense(self, index): 
        if 0 <= index < len(self.expenses): 
            self.expenses.pop(index)
            return True
        else: 
            return False 
    
    def summary_by_category(self, month, year): 
        output = {}

        for i in self.expenses: 
            if i.date.month == month and i.date.year == year: 
                output[i.category] = output.get(i.category, 0) + i.amount
        
        return output 
