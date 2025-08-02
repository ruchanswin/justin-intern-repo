# DISCOUNT_RATE = 0.2
# def calculate_discount_price(price):
#     return price * (1 - DISCOUNT_RATE)

DISCOUNT_RATE = 0.2
def calculate_discount_price(price):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number.")
    if isinstance(price, bool):
        raise TypeError("Price cannot be a boolean.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price * (1 - DISCOUNT_RATE)

calculate_discount_price(100) 
# calculate_discount_price("yolo")  
calculate_discount_price(False)  
calculate_discount_price(-15)  
