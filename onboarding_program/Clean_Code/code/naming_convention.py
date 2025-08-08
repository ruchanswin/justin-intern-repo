# Example 1: Unclear function and variable names from code_principles.py
def f(a, b):
    # Original unclear code - what does 'f' do? What are 'a' and 'b'?
    x = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            x += a[i]
    for j in range(len(b)):
        if b[j] % 2 == 0:
            x += b[j]
    return x

# Refactored version with clear names
def sum_even_numbers_from_lists(first_list, second_list):
    # Clear purpose: sums all even numbers from two lists.
    even_sum = 0
    for number in first_list:
        if number % 2 == 0:
            even_sum += number
    for number in second_list:
        if number % 2 == 0:
            even_sum += number
    return even_sum

# Example 2: Unclear variable names from code_smells.py
def calc(x, y):
    # Original unclear code - what does 'calc' calculate?
    z = x + y
    return z

# Refactored version with clear names
def add_numbers(first_number, second_number):
    # Clear purpose: adds two numbers together.
    sum_result = first_number + second_number
    return sum_result

# Example 3: Generic variable names that don't describe purpose
def process_user_data(data):
    # Original unclear code - what kind of data? What processing?
    temp = data.get('age', 0)
    flag = temp > 18
    return flag

# Refactored version with clear names
def is_user_adult(user_profile):
    # Clear purpose: checks if user is 18 or older.
    user_age = user_profile.get('age', 0)
    is_adult = user_age >= 18
    return is_adult

# Example 4: Single letter variables in loops
def find_max_value(numbers):
    # Original unclear code - single letter variables.
    m = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > m:
            m = numbers[i]
    return m

# Refactored version with clear names
def find_maximum_value(number_list):
    # Clear purpose: finds the highest value in a list.
    maximum_value = number_list[0]
    for current_number in range(1, len(number_list)):
        if number_list[current_number] > maximum_value:
            maximum_value = number_list[current_number]
    return maximum_value
