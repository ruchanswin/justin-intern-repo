# What was the issue?
The Child component in my React code was directly mutating a prop (`state.count = state.count + 5`). This caused unexpected behavior and broke React's one-way data flow, leading to bugs and unpredictable UI updates.

# What debugging method did you use?
I reviewed the code and noticed the prop mutation. I used console.log statements to inspect the state before and after the mutation, and referred to React documentation and error messages in the browser console, which warned against mutating props.

# How did you resolve the problem?
I refactored the Child component to avoid mutating props, and I calculated the derived value (`state.count + 5`) in a local variable to use that for rendering, ensuring the original state remained unchanged. This fixed the bug and followed React best practices.