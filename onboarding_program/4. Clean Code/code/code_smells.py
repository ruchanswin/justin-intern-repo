### All the code is AI-generated. There are 2 versions of each code smell: the original common code smell and the refactored version.

# Magic Numbers & Strings – Using hardcoded values instead of constants.
## Code Smell:
def calculate_discount_bad(price):
    # 0.2 is a magic number (should be a named constant)
    return price * 0.8

## Refactored:
discount_rate = 0.2
def calculate_discount(price):
    return price * (1 - discount_rate)

# Long Functions – Functions that do too much and should be broken into smaller parts.
## Code Smell:
def process_order_bad(order):
    print("Validating order...")
    if not order.get('item'):
        print("No item specified!")
        return
    print("Checking inventory...")
    print("Calculating price...")
    price = order['quantity'] * 9.99
    print(f"Total price: {price}")
    print("Processing payment...")
    print("Order complete!")

## Refactored:
def validate_order(order):
    if not order.get('item'):
        print("No item specified!")
        return False
    print("Order validated.")
    return True

def check_inventory(order):
    print("Checking inventory...")
    # Inventory logic here

def calculate_price(order):
    price = order['quantity'] * 9.99
    print(f"Total price: {price}")
    return price

def process_payment(price):
    print("Processing payment...")
    # Payment logic here

def process_order(order):
    if not validate_order(order):
        return
    check_inventory(order)
    price = calculate_price(order)
    process_payment(price)
    print("Order complete!")

# Duplicate Code – Copy-pasting logic instead of reusing functions.
## Code Smell:
def print_user_info(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")

def print_admin_info(admin):
    print(f"Name: {admin['name']}")
    print(f"Email: {admin['email']}")

## Refactored:
def print_person_info(person):
    print(f"Name: {person['name']}")
    print(f"Email: {person['email']}")

# Large Classes (God Objects) – Classes that handle too many responsibilities.
## Code Smell:
class Application:
    def __init__(self):
        self.users = []
        self.orders = []
        self.settings = {}
    def add_user(self, user):
        self.users.append(user)
    def remove_user(self, user):
        self.users.remove(user)
    def create_order(self, order):
        self.orders.append(order)
    def update_settings(self, key, value):
        self.settings[key] = value
    def backup_data(self):
        print("Backing up data...")
    def restore_data(self):
        print("Restoring data...")

## Refactored:
class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def remove_user(self, user):
        self.users.remove(user)

class OrderManager:
    def __init__(self):
        self.orders = []
    def create_order(self, order):
        self.orders.append(order)

class SettingsManager:
    def __init__(self):
        self.settings = {}
    def update_settings(self, key, value):
        self.settings[key] = value

class BackupManager:
    def backup_data(self):
        print("Backing up data...")
    def restore_data(self):
        print("Restoring data...")

# Deeply Nested Conditionals – Complex if/else trees that make code harder to follow.
## Code Smell:
def check_access_bad(user):
    if user:
        if user.get('is_active'):
            if user.get('role') == 'admin':
                if user.get('department') == 'IT':
                    print("Access granted!")
                else:
                    print("Wrong department.")
            else:
                print("Not an admin.")
        else:
            print("User not active.")
    else:
        print("No user provided.")

## Refactored:
def check_access(user):
    if not user:
        print("No user provided.")
        return
    if not user.get('is_active'):
        print("User not active.")
        return
    if user.get('role') != 'admin':
        print("Not an admin.")
        return
    if user.get('department') != 'IT':
        print("Wrong department.")
        return
    print("Access granted!")

# Commented-Out Code – Unused code that clutters the codebase.
## Code Smell:
def sum_numbers_bad(a, b):
    # result = a - b  # Old logic
    return a + b

## Refactored:
def sum_numbers(a, b):
    return a + b

# Inconsistent Naming – Variable names that don't clearly describe their purpose.
## Code Smell:
def calc(x, y):
    z = x + y
    return z

## Refactored:
def add_numbers(a, b):
    total = a + b
    return total
