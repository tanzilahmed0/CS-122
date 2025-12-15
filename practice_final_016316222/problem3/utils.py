''' 2: Write a decorator timed that logs function name and execution time to
expense_logs.txt.
• 3: Write a generator monthly_report(expenses, month, year) that yields tuples
(category, total_amount) for each category in the specified month. '''
import time 


def timed(func): 
    def wrapper(*args, **kwargs): 
        start = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start

        with open('expense_logs.txt', 'a') as f: 
            f.write(f"{func.__name__} elapsed time was {total_time} seconds")

        return result 
    return wrapper 


def monthly_report(expenses, month, year): 
    total_amount = {}
    for i in expenses: 
        if i.month == month and i.year == year: 
            total_amount[i.category] = total_amount.get(i.category, 0) + i.amount 

    for category, amount in total_amount.items():
        yield (category, amount)
        
