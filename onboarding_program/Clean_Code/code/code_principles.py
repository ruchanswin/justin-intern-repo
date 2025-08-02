# Example of messy code (lacks structure, uses poor naming, and has no comments)
def f(a,b):
 x=0
 for i in range(len(a)):
  if a[i]%2==0:
   x+=a[i]
 for j in range(len(b)):
  if b[j]%2==0:
   x+=b[j]
 return x

# Cleaner, more structured version
def sum_even_numbers(list1, list2):
    # Returns the sum of all even numbers in two lists.
    total = sum(n for n in list1 if n % 2 == 0)
    total += sum(n for n in list2 if n % 2 == 0)
    return total
