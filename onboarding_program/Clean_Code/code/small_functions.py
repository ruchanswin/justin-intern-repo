# Original complex function before refactoring
def process_order(order):
    """
    This function has too many responsibilities: order validation, inventory checking, price calculation, 
    payment processing, and confirmation sending, so it is hard to test individual parts, 
    difficult to understand the flow, and hard to reuse individual steps.
    """
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

# Refactored version by splitting into smaller functions
"""
Each function has a single responsibility, so it is easy to test individually, 
make the code more readable, reuse components, and allow for easier maintenance and debugging.
"""
def validate_order(order):
    # Validates order data
    if not order.get('item'):
        print("No item specified!")
        return False
    if order.get('quantity', 0) <= 0:
        print("Invalid quantity!")
        return False
    return True

def check_inventory(order):
    # Checks if item is in stock
    print("Checking inventory...")

def calculate_price(order):
    # Calculates total price
    return order['quantity'] * 9.99

def process_payment(price):
    # Processes the payment
    print("Processing payment...")

def send_confirmation():
    # Sends confirmation to customer
    print("Order complete! Confirmation sent.")

def process_order_refactored(order):
    # Main orchestrator function
    if not validate_order(order):
        return
    check_inventory(order)
    price = calculate_price(order)
    process_payment(price)
    send_confirmation()

# Testing the refactored functions
def test_refactored_functions():
    # Test validation
    test_order = {'item': 'laptop', 'quantity': 2}
    print(f"Validation test: {validate_order(test_order)}")
    
    # Test price calculation
    price = calculate_price(test_order)
    print(f"Price calculation: ${price}")
    
    # Test complete flow
    print("\nComplete order processing:")
    process_order_refactored(test_order)

if __name__ == "__main__":
    test_refactored_functions()
