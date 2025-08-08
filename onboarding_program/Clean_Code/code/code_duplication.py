"""
Original code with duplication: These functions are duplicated even though they have the same logic.
For example, print_user_info - print_admin_info, calculate_user_salary - calculate_admin_salary, 
validate_user_data - validate_admin_data have the same logic.
"""
def print_user_info(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")

def print_admin_info(admin):
    print(f"Name: {admin['name']}")
    print(f"Email: {admin['email']}")

def calculate_user_salary(user):
    base_salary = user.get('base_salary', 0)
    bonus = user.get('bonus', 0)
    total = base_salary + bonus
    return total

def calculate_admin_salary(admin):
    base_salary = admin.get('base_salary', 0)
    bonus = admin.get('bonus', 0)
    total = base_salary + bonus
    return total

def validate_user_data(user):
    if not user.get('name'):
        return False
    if not user.get('email'):
        return False
    if user.get('age', 0) < 18:
        return False
    return True

def validate_admin_data(admin):
    if not admin.get('name'):
        return False
    if not admin.get('email'):
        return False
    if admin.get('age', 0) < 18:
        return False
    return True

# Refactored version by eliminating duplication
def print_person_info(person):
    # Function that works for both users and admins
    print(f"Name: {person['name']}")
    print(f"Email: {person['email']}")

def calculate_salary(person):
    # A single salary calculation function
    base_salary = person.get('base_salary', 0)
    bonus = person.get('bonus', 0)
    total = base_salary + bonus
    return total

def validate_person_data(person):
    # A single validation function
    if not person.get('name'):
        return False
    if not person.get('email'):
        return False
    if person.get('age', 0) < 18:
        return False
    return True

def demonstrate_before_after():
    # Demonstrates how the refactored code eliminates duplication
    # Test data
    user = {'name': 'John Doe', 'email': 'john@example.com', 'base_salary': 50000, 'bonus': 5000, 'age': 25}
    admin = {'name': 'Jane Smith', 'email': 'jane@example.com', 'base_salary': 60000, 'bonus': 8000, 'age': 30}
    
    # Before refactoring - you have to call 6 functions - it is more complex and harder to maintain
    print("User Info:")
    print_user_info(user)
    print("\nAdmin Info:")
    print_admin_info(admin)
    
    print(f"\nUser Salary: ${calculate_user_salary(user)}")
    print(f"Admin Salary: ${calculate_admin_salary(admin)}")
    
    print(f"\nUser Valid: {validate_user_data(user)}")
    print(f"Admin Valid: {validate_admin_data(admin)}")
    
    # After refactoring - you only have to call 3 functions - it is more readable and maintainable
    print("User Info:")
    print_person_info(user)
    print("\nAdmin Info:")
    print_person_info(admin)
    
    print(f"\nUser Salary: ${calculate_salary(user)}")
    print(f"Admin Salary: ${calculate_salary(admin)}")
    
    print(f"\nUser Valid: {validate_person_data(user)}")
    print(f"Admin Valid: {validate_person_data(admin)}")

if __name__ == "__main__":
    demonstrate_before_after()
