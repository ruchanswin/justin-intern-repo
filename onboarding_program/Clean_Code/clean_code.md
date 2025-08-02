# Writing Unit Tests for Clean Code
* How do unit tests help keep code clean?
- Unit tests verify the functions work as expected and identify any errors before pushing the code to the codebase.
- If the code is too complex to be tested, it needs refactoring.
- When you make changes to the code, unit tests ensure the function behaviours remain the same.
- Unit tests clarify the functions' purposes, so other developers could understand and avoid asking clarification questions.
* What issues did you find while testing?
- I haven't tested edge cases for my function (the price is 0, negative, a very large number or non-integer values like boolean or string). These edge cases can break the function if not properly handled.
- Testing can point out the function's weaknesses, which allows me to refactor the code and strengthen code security.
- It is important to write clear, concise tests that are related to the function's purposes.
# Handling Errors & Edge Cases
* What was the issue with the original code?
- For the example, I'm using the price calculation to demonstrate how this function lacks necessary errors handling and edge case covering. To refactor the code, I've added if-else statements to test if the input is valid (positive integer or float values). If the input is unsatisfactory, the function will return errors.
* How does handling errors improve reliability?
- Defensive coding (like guard clauses) ensures the code doesn’t break when users enter invalid input.
- Good error messages allow developers to understand what's going wrong for debugging.
# Commenting & Documentation
* When should you add comments?
- When you want to explain the context or intent behind the code and not restate the obvious.
- When the logic is complex to understand or when the code handles errors or edge cases.
* When should you avoid comments and instead improve the code?
- When the comments restate the obvious logic in the code, or you want to rewrite the code to make it self-explanatory.
- When the code contain bad naming convention which can be confused for readers.
- When the comments are outdated and unrelated to the code purposes, you should remove or update them.
# Refactoring Code for Simplicity
* What made the original code complex?
- The original code for extracting even numbers used an explicit for-loop with manual indexing and conditional logic, making it longer and harder to read. Since it required tracking the index and appending to a result list, it added unnecessary complexity for a simple task.
* How did refactoring improve it?
- Refactoring replaced the manual loop with a list comprehension, making the code much shorter and more readable.
- The intent of the code is now clear in a single line, reducing the risk of errors and making maintenance easier.
# Avoiding Code Duplication
* What were the issues with duplicated code?
- Any changes would need to be made in multiple places, increasing the risk of inconsistencies and bugs.
- The code makes the codebase longer and harder to maintain or understand.
- It can be hard to debug errors since you have to find ever single function and fix it.
* How did refactoring improve maintainability?
- Refactoring removed the duplicated code by combining similar functions into one reusable function, so any changes only need to be made in a single place, reducing the risk of inconsistencies.
- The code is shorter, easier to read, and less error-prone, making future maintenance and updates much simpler.
# Writing Small, Focused Functions
* Why is breaking down functions beneficial?
- Smaller, focused functions are easier to read, understand, and test.
- Each function has a single responsibility, making bugs easier to isolate and fix.
- Reusable functions reduce code duplication and make future changes simpler.
- It encourages better naming and documentation, improving overall code quality.
* How did refactoring improve the structure of the code?
- Refactoring split a long, complex function into several smaller functions, each handling a specific task (validation, calculation, payment, etc.).
- The main function now reads like a sequence of clear steps, making the logic easier to follow.
- This modular structure makes the codebase more maintainable and extensible.
# Naming Variables & Functions
* What makes a good variable or function name?
- A good name is descriptive, specific, and clearly indicates the purpose or value it represents.
- It uses consistent naming conventions and avoids abbreviations that could be confusing.
- Function names should describe what the function does (e.g., calculate_area), and variable names should describe what data they hold (e.g., width, height).
* What issues can arise from poorly named variables?
- Poorly named variables make code harder to read, understand, and maintain.
- They can cause confusion, lead to bugs, and slow down development because other developers (or your future self) may misunderstand the code purposes and need to ask clarification questions
- Vague or misleading names increase the risk of errors and make debugging more difficult.
* How did refactoring improve code readability?
- Refactoring replaced unclear names (like c, x, y, z) with descriptive names (like calculate_area, width, height, area).
- The code is now self-explanatory, making it easier for anyone to understand its purpose without extra comments.
- Clear naming reduces cognitive load and helps prevent mistakes.
# Code Formatting & Style Guide
* Why is code formatting important?
- Consistent formatting makes code easier to read, understand, debug and maintain for everyone on the team, prevent bugs caused by inconsistent structure. It also supports code reviews and collaboration.
* What issues did the linter detect?
- The linter detected inconsistent indentation, missing or extra spaces, and variable naming issues. It also flagged unused imports, unreachable code, and lines that were too long.
- Fixing these issues improved code quality and reduced the risk of subtle bugs.
* Did formatting the code make it easier to read?
- Yes, formatting the code made it much easier to scan and understand. Proper indentation, spacing, and alignment help highlight the structure and logic of the code.
# Understanding Clean Code Principles
* Research and summarize the clean code principles
- Simplicity: Keep logic straightforward and use the least complex solution that works (prefer clear structure over cleverness, break problems into small, manageable parts, avoid unnecessary abstractions or premature optimizations).
- Readability: Make sure others can quickly understand what your code does (use descriptive names for variables and functions, write short, focused functions, prioritize clarity over brevity).
- Maintainability: Write code that you, or someone else, can safely modify in a long time (avoid duplication and tightly coupled logic, use modular design with single responsibility functions, leave helpful comments when the logic isn’t obvious).
- Consistency: Follow the project’s formatting, naming conventions, and organizational patterns (Stick to the style guide like ESLint, Prettier or PEP8, apply consistent indentation, naming formats like camelCase or snake_case, and file structures) helps teams read and work with code efficiently.
- Efficiency: Write code that performs well, but don’t optimize prematurely (consider algorithmic performance when necessary, reuse code and make use of built-in libraries, profile or benchmark only after solving performance issues).