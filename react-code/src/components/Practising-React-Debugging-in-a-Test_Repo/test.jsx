import { useState } from 'react';

function Parent() {
  const [state, setState] = useState({ count: 0 });
  return (
    <div>
      <p>count: {state.count}</p>
      <button onClick={() => setState(c => ({ count: c.count + 1 }))}>Increment</button>
      <Child state={state} />
    </div>
  );
}

// Buggy version (do not use):
// function Child({ state }) {
//   // Bug: Directly mutating props (state.count = state.count + 5)
//   state.count = state.count + 5;
//   return <div><p>count + 5 = {state.count}</p></div>;
// }

// Fixed version:
function Child({ state }) {
  // Do not mutate props, just calculate the derived value.
  const countPlusFive = state.count + 5;
  return <div><p>count + 5 = {countPlusFive}</p></div>;
}

// Alternative solution (also correct):
// function Child({ state }) {
//   // Create a copy of the state to avoid direct mutation
//   const copy = { ...state };
//   return <div><p>count + 5 = {copy.count + 5}</p></div>;
// }

export default Parent;