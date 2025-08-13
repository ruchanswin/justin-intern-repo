# Using Selectors in Redux Toolkit

* When should you use Redux instead of useState?
* You should use Redux when you need to manage global state that is shared across many components, especially in large and complex applications. For example:
* Multiple components need access to the same state
* You want predictable state updates and centralized state management
* You need advanced features like middleware, time-travel debugging, or undo/redo.
* The state logic is complex or needs to be reused.

## Introduction to Redux Toolkit (State Management)

* What are the benefits of using selectors instead of directly accessing state?
* They abstract how state is retrieved, so components don’t need to know the state structure.
* They can be reused across components.
* With tools like Reselect, selectors can cache results and avoid unnecessary recalculations, improving performance.
* If the state shape changes, only selectors need to be updated, not every component.
* They are easy to test in isolation.
