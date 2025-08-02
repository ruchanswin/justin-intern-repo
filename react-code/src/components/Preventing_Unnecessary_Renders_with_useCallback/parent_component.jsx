import { useState, useCallback } from "react";
import ChildComponent from "./child_component";

const ParentComponent = () => {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("🔘 Button clicked");
  }, []); // 🔁 Will not change on re-renders

  console.log("🔁 ParentComponent rendered");

  return (
    <div>
      <h2>useCallback Demo</h2>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <ChildComponent onClick={handleClick} />
    </div>
  );
};

export default ParentComponent;
