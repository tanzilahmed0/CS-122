apply_tax = lambda price: price * 1.08 

def apply_discount(func):    
    def wrapper(price): 
        if price > 100:
            return func(price * 0.9)
        else: 
            return func(price)
    return wrapper

def price_generator(prices, processing_function): 
    for price in prices: 
        yield processing_function(price)
