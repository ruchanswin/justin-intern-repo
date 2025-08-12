# Preventing Unneccesary Renders with useCallback

* What problem does useCallback solve?
* It prevents unnecessary re-creations of functions on every render, and helps avoid unwanted re-renders in deeply nested components.
* It is useful when passing functions as props to child components that rely on reference equality like React.memo.

* How does useCallback work differently from useMemo?
* useCallback returns a memoized function, while useMemo returns a memoized value. You should use useCallback when you want to preserve a function reference, and useMemo when you want to store a computed value.

* When would useCallback not be useful?
* When the function is not passed to child components or used in dependency arrays.
* When the components don’t re-render frequently.
* When the function is cheap and easy to recreate and doesn’t cause performance issues.

# Optimizing Performance with useMemo

* How does useMemo improve performance?
* It avoids expensive recalculations by caching results, so it can prevent unnecessary renders when used with memoized components, which is useful for derived data like filtered lists or computed values.

* When should you avoid using useMemo?
* When the calculations are simple and don’t impact performance.
* When the memoization adds complexity without major benefits.
* When dependencies change frequently, which makes memoization ineffective.

* What happens if you remove useMemo from your implementation?
* The value will be recalculated on every render, which can cause unnecessary re-renders in child components relying on stable props and performance degradation if the computation is expensive.

# Understanding React Hooks: useEffect

* When should you use useEffect instead of handling logic inside event handlers?
* When you need to run side effects that happen on mount, update, or unmount like API calls or subscriptions, respond to state or prop changes outside of user interaction, and integrate external systems like localStorage, timers, and analytics.

* What happens if you don’t provide a dependency array?
* The effect will keep running after every render, which can cause performance issues, infinite loops and unintended side effects, especially when the function is expensive or needs to access data. Adding the dependancies ensures React knows when to run the effect.

* How can improper use of useEffect cause performance issues?
* The improper use of useEffect can lead to missing dependencies, and these misses can cause stale data and skipped updates. Also, using too many dependencies and computation power can trigger unnecessary re-renders that create uncontrolled loops if state updates are inside effects, and block the main thread.
