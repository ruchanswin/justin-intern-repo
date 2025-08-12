# What code smells did you find in your code?

- To identify code smells, I have intentionally created a variety of code smells in "code_smells.py", with the original common code smells and the refactoring of the code.
- Magic numbers & strings: In the example, the function performs a price calculation after applying a 20% discount, but the discount is hardcoded. It is inconvenient when you want to change the discount rate because you have to manually find the hardcoded values. To refactor the code, I create a variable named discount_rate to store the discount value.
- Long functions: In the example, the process_order_bad function manages too many actions: validating orders, calculating price, checking inventory and processing payment. It would be difficult to read through the function and when debugging, the function is prone to malfunction due to cluttered lines of code. To refactor the code: I split the actions into many smaller functions and call them in the process_order function. This way makes the code cleaner and easy to debug.
- Duplicate code: In the example, there are 2 functions: print_user_info and print_admin_info. These functions work exactly the same, so using 2 functions is unnecessary and make the code longer. To refactor the code, these functions are merge into 1 function named print_person_info. It is much better to reuse functions for similar logic instead of blindly copy-paste code.
- God objects: In the example, the class maintains too many responsibilities: adding and removing users, creating orders, updating settings, backing up and restoring data. Similar to long functions problem, this code smell makes it difficult to read through and debug. To refactor the code, I separate different responsibilities into many smaller classes.
- Deeply nested conditionals: In the example, the check_access function uses many if-else statements, which makes the code harder to understand and follow, and it is prone to errors if wrong indentation happens. To refactor the code, I separate if-else statements based on each scenario to avoid nesting.
- Commented-out code: In the example, the sum_numbers function performs number addition, but it still keeps the old subtraction logic. This makes the code unnecessarily longer and if not commented-out properly, it can make the code malfunction and harder to read. It is recommended to remove unused code.
- Inconsistent naming: In the example, the function for addition is named calc and the sum is named z. The names are too generic and doesn't show their real purposes, so for refactoring, the function name is changed to add_numbers and the sum is called total.

# How did refactoring improve the readability and maintainability of the code?

- Refactoring helps create clear, concise functions with descriptive names to make it easier to understand the code, even if the readers are new.
- Refactoring helps maintain the code easily since it breaks down long functions into smaller and more manageable ones.
- Refactoring makes team collaboration and code review smooth since the team doesn't have to waste time understanding the code and asking clarification questions.

# How can avoiding code smells make future debugging easier?

- When the functions are small and readable, it is easy to find the bug when errors happen.
- When you reuse the functions, you spend less effort and time to fix the functions instead of creating copy-pasted code and then needing to find every single piece of code for debugging.
- When the function names are clear and descriptive, it is easier to debug because you can pinpoint the error and fix it. If you use generic names, you have to try multiple tests to find which function causes errors.
