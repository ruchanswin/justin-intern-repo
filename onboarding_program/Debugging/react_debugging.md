# What are the most common debugging techniques?
- Using console.log to inspect variables, props, and state at different stages in the component lifecycle.
- Using React DevTools to inspect the component tree, props, and state in real time.
- Setting breakpoints and going through code with the browser's debugger or VS Code debugger.
- Using error boundaries to catch and handle runtime errors in the UI.
- Isolating components and writing unit tests to reproduce and fix bugs.
- Checking the browser console for warnings and errors.

# Which tools are most effective for React debugging?
- React DevTools is used to visualize the component tree, inspect props/state, and track re-renders.
- Browser Developer Tools use the Elements panel, Console, and Sources for debugging JavaScript and DOM issues.
- VS Code Debugger is used to set breakpoints, go through code, and inspect variables directly in your editor.
- React Profiler analyzes component render performance and identify unnecessary re-renders or bottlenecks.
- Error boundaries catch and display errors in the UI without crashing the whole app.

# How do you debug issues in large React codebases?
- You should break down the large codebases into small components to reproduce the bug.
- You should use React DevTools to trace the flow of props and state through the component tree.
- You should add logging or breakpoints to follow data and event flow.
- You should use search and code navigation features in your IDE to track down where state or props are set/changed.
- You should rite targeted unit or integration tests to isolate the components and identify the bug.
- You should collaborate with teammates and find relevant, credible resources to avoid duplicated effort.