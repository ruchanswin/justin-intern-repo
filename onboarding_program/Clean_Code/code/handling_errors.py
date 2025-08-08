# The code doesn't have any error handling. If the input is invalid, it can break the code.
DISCOUNT_RATE = 0.2
def calculate_discount_price(price):
    return price * (1 - DISCOUNT_RATE)

# The code handles errors properly. When the price is not a number, boolean, or negative, the code will raise an error.
# Error handling is important to prevent the code from breaking and to make the code more robust.
DISCOUNT_RATE = 0.2
def calculate_discount_price(price):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number.")
    if isinstance(price, bool):
        raise TypeError("Price cannot be a boolean.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price * (1 - DISCOUNT_RATE)
