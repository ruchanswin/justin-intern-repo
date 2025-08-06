import { useState, useCallback } from "react";
import ChildComponent from "./ChildComponent";

const ParentComponent = () => {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("Button clicked");
  }, []); // Will not change on re-renders

  console.log("ParentComponent rendered");

  return (
    <div>
      <h1>useCallback</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
      <ChildComponent onClick={handleClick} />
    </div>
  );
};

export default ParentComponent;
