import { useDispatch, useSelector } from "react-redux";
import { increment, decrement, selectCounter } from "./store";

const Counter = () => {
  const count = useSelector(selectCounter);
  const dispatch = useDispatch();

  return (
    <div style={{ marginBottom: "2rem" }}>
      <h1>Counter: {count}</h1>
      <button
        onClick={() => dispatch(increment())}
        style={{ marginRight: "1rem" }}
      >
        Increase
      </button>
      <button onClick={() => dispatch(decrement())}>Decrease</button>
    </div>
  );
};

export default Counter;
