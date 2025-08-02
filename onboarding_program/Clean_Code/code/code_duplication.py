# Example of duplicated code
def print_user_info(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")

def print_admin_info(admin):
    print(f"Name: {admin['name']}")
    print(f"Email: {admin['email']}")

# Refactored version to eliminate duplication
def print_person_info(person):
    print(f"Name: {person['name']}")
    print(f"Email: {person['email']}")
