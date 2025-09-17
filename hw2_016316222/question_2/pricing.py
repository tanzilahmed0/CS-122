# Lambda function to apply 8% tax
apply_tax = lambda price: price * 1.08 

def apply_discount(func):
    """Decorator that applies 10% discount for prices over $100 before processing"""    
    def wrapper(price): 
        if price > 100:
            return func(price * 0.9)  
        else: 
            return func(price)
    return wrapper

def price_generator(prices, processing_function): 
    """Generator that applies processing function to each price"""
    for price in prices: 
        yield processing_function(price)
