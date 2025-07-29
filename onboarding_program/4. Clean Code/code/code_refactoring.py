# Overly complicated code example
def get_even_numbers(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result

# Refactored
def get_even_numbers_simple(nums):
    """Returns a list of even numbers from the input list."""
    return [n for n in nums if n % 2 == 0]
