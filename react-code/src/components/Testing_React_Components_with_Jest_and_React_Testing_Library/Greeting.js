import { useState } from "react";

const Greeting = () => {
  const [greeted, setGreeted] = useState(false);

  return (
    <div>
      <h1>{greeted ? "Hello Justin!" : "Welcome to Focus Bear!"}</h1>
      <button onClick={() => setGreeted(true)}>Greeting</button>
    </div>
  );
};

export default Greeting;
