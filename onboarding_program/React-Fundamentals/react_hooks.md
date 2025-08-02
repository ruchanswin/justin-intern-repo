# Preventing Unneccesary Renders with useCallback
* What problem does useCallback solve?
  - It prevents unnecessary re-creation of functions, which can help avoid unwanted re-renders in child components that depend on function props.

* How does useCallback work differently from useMemo?
  - useCallback memoizes a function, while useMemo memoizes the result of a function (a value).

* When would useCallback not be useful?
  - When the function is not passed as a prop or does not cause re-renders, or if the function is simple and cheap to recreate.

# Optimizing Performance with useMemo
* How does useMemo improve performance?
  - It memoizes expensive calculations, so they only run when dependencies change, reducing unnecessary computations.

* When should you avoid using useMemo?
  - When the calculation is cheap or the component is simple, as useMemo adds complexity and overhead.

* What happens if you remove useMemo from your implementation?
  - The calculation will run on every render, which can hurt performance if the calculation is expensive.

# Understanding React Hooks: useEffect
* When should you use useEffect instead of handling logic inside event handlers?
  - When you need to run side effects in response to state or prop changes, or on mount/unmount, not just user actions.

* What happens if you don’t provide a dependency array?
  - The effect runs after every render, which can lead to performance issues or unintended behavior.

* How can improper use of useEffect cause performance issues?
  - Running effects too often, causing unnecessary API calls, re-renders, or memory leaks if cleanup is not handled properly.