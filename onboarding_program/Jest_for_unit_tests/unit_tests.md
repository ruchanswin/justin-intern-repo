# Testing Redux with Jest
* What was the most challenging part of testing Redux?
- Isolating logic from side effects because middleware can complicate tests.
- Mocking store state transitions to ensure the reducer works properly across multiple actions.
- Testing async actions requires mocking dispatch and external dependencies like API.
- Redux logic can be lengthy, so structuring tests clearly is importnat.
* How do Redux tests differ from React component tests?
- Focus Area: Redux tests focus on state management logic (reducers, actions, middleware), while React component tests focus on UI behavior and rendering.
- Testing Tools: Redux tests often use Jest alone or with utilities like redux-mock-store, while React component tests typically use Jest + React Testing Library.
- User Perspective: Redux tests are logic-driven, not user-facing, while React tests simulate real user interactions (clicks, typing, etc.).
- State Handling: Redux tests directly manipulate and assert on store state, while React tests rely on props, context, or hooks to manage state.
- Mocking Needs: Redux tests often mock dispatch functions and API calls, while React tests mock DOM events, browser APIs, and sometimes network requests.
- Test Scales: Redux tests are unit-level, validating pure functions, while React tests can be integration-level, covering component trees and side effects.
# Mocking API Calls in Jest
* Why is it important to mock API calls in tests?
- Ensure tests don’t depend on external services, avoid slow network calls, prevent flaky tests due to API downtime, and allow testing edge cases and error handling.
* What are some common pitfalls when testing asynchronous code?
- Forget to await or return promises, which can lead to false positives.
- Not handling errors properly, which can cause unhandled promise rejections.
- Over-mocking hides bugs, while under-mocking causes instability.
# Testing React Components with Jest & React Testing Library
* What are the benefits of using React Testing Library instead of testing implementation details?
- Encourage testing from the user’s perspective, leading to more robust and maintainable tests, avoid easily broken tests tied to internal component structure, promote accessibility-first testing via roles and labels, and easier to maintain as components evolve.
* What challenges did you encounter when simulating user interaction?
- Async updates (await findBy queries or use waitFor), complex state changes especially with nested components or context, ensuring events start in the correct order, some interactions like keyboard navigation require careful setup.
# Introduction to Unit Testing with Jest
* Why is automated testing important in software development?
- It catches bugs early before they reach production, improves code quality through test-driven development, enables safe refactoring with confidence, and speeds up development by reducing manual testing.
* What did you find challenging when writing your first Jest test?
- Understanding Jest syntax (describe, test, expect, etc.), setting up the environment, writing meaningful assertions (understanding what and why to test), debugging test failures even if stack traces are unclear.