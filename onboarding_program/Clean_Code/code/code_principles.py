# Messy version
# Poor naming: function and variables ('f', 'a', 'b', 'x') cannot convey intent.
# Duplicated logic: two similar loops for a and b.
# Manual indexing: uses range(len(...)) instead of iterating values.
# No documentation: behavior/contract is not stated.
# Imperative accumulator style: obscures the simple goal (sum evens).
def f(a,b):
 x=0
 for i in range(len(a)):
  if a[i]%2==0:
   x+=a[i]
 for j in range(len(b)):
  if b[j]%2==0:
   x+=b[j]
 return x

# Clean version
# Descriptive naming: 'sum_even_numbers', 'list1', 'list2' can convey intent.
# DRY: avoids duplicated loop logic.
# Pythonic iteration: comprehensions express "sum evens" succinctly.
# Documented behavior: brief docstring clarifies purpose.
# Single responsibility: easier to read and test.
def sum_even_numbers(list1, list2):
    """Return the sum of all even numbers in two lists."""
    total = sum(n for n in list1 if n % 2 == 0)
    total += sum(n for n in list2 if n % 2 == 0)
    return total

# Personal experience
"""
Back in the last semester, I was working on a project that involved a lot of data processing and analysis. That part belonged to
another team member, but since my part was building a time-series analysis model, I had to look through the code to understand
how data was processed. The code was a mess: there is no documentation or comments, the code contains duplicated logic and errors,
and some of the code is not even working. So before working on my part, I had to refactor the code to make it more readable and 
maintainable, and add unit tests to make sure the code is working as expected.
"""
