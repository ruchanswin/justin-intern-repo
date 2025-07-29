# Long, complex function
def process_order(order):
    # Validate order
    if not order.get('item'):
        print("No item specified!")
        return
    if order.get('quantity', 0) <= 0:
        print("Invalid quantity!")
        return
    
    # Check inventory
    print("Checking inventory...")
    
    # Calculate price
    price = order['quantity'] * 9.99
    print(f"Total price: {price}")

    # Process payment
    print("Processing payment...")

    # Send confirmation
    print("Order complete! Confirmation sent.")

# Refactored into smaller functions
def validate_order(order):
    if not order.get('item'):
        print("No item specified!")
        return False
    if order.get('quantity', 0) <= 0:
        print("Invalid quantity!")
        return False
    return True

def check_inventory(order):
    print("Checking inventory...")

def calculate_price(order):
    return order['quantity'] * 9.99

def process_payment(price):
    print("Processing payment...")

def send_confirmation():
    print("Order complete! Confirmation sent.")

def process_order_refactored(order):
    if not validate_order(order):
        return
    check_inventory(order)
    price = calculate_price(order)
    process_payment(price)
    send_confirmation()
