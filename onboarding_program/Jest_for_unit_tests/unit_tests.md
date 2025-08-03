# Testing Redux with Jest
* What was the most challenging part of testing Redux?
- Isolating logic from side effects since middleware can complicate tests.
- Mocking store state transitions to ensure the reducer works properly across multiple actions.
- Testing async actions requires mocking dispatch and external dependencies like API.
- Redux logic can be lengthy and complex, so structuring tests clearly is importnat.
* How do Redux tests differ from React component tests?
- Focus Area: Redux tests focus on state management logic (reducers, actions, middleware), while React component tests focus on UI behavior and rendering.
- Testing Tools: Redux tests often use Jest alone or with utilities like redux-mock-store, while React component tests typically use Jest + React Testing Library.
- User Perspective: Redux tests are logic-driven, not user-facing, while React tests simulate user interactions (clicks, typing, etc.).
- State Handling: Redux tests directly manipulate and assert on store state, while React tests rely on props, context, or hooks to manage state.
- Mocking Needs: Redux tests often mock dispatch functions and API calls, while React tests mock DOM events, browser APIs, and sometimes network requests.
- Test Scales: Redux tests are unit-level, validating pure functions, while React tests can be integration-level, covering component trees and side effects.
# Mocking API Calls in Jest
* Why is it important to mock API calls in tests?
- The API calls ensure tests don’t depend on external services, avoid slow network calls, prevent failing tests due to API downtime, and allow testing edge cases and error handling.
* What are some common pitfalls when testing asynchronous code?
- You forget to await or return promises, which can lead to slower performance and false positives.
- You don't handle errors properly, which can cause promise rejections.
- Over-mocking hides bugs, while under-mocking causes instability.
# Testing React Components with Jest & React Testing Library
* What are the benefits of using React Testing Library instead of testing implementation details?
- It encourages testing from the user’s perspective, which leads to more robust and maintainable tests, avoiding easily broken tests tied to internal component structure, promoting accessibility-first testing via roles and labels, and making the tests more maintainable as components evolve.
* What challenges did you encounter when simulating user interaction?
- I encounter complex state changes especially with nested components or context, events that don't start in the correct order so I have to fix the sequence, some interactions like keyboard navigation require careful setup, some imports or file names are missing or misspelled.
# Introduction to Unit Testing with Jest
* Why is automated testing important in software development?
- It catches bugs early before they reach production, improves code quality through test-driven development, enables safe refactoring with confidence, and speeds up development by reducing manual testing.
* What did you find challenging when writing your first Jest test?
- I find it challenging to understand and remember Jest syntax (describe, test, expect, etc.), set up the environment at first, write meaningful assertions (understanding what and why to test), and debug test failures even if stack traces are unclear.