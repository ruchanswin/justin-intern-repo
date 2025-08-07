import { useMemo, useState } from "react";

const ExpensiveCalculation = () => {
  const [number, setNumber] = useState(10000);

  const expensiveResult = useMemo(() => {
    if (number === "" || isNaN(number)) return 0;
    console.log("Running calculation...");
    let result = 1;
    for (let i = 1; i <= number; i++) {
      result += i;
    }
    return result;
  }, [number]);

  return (
    <div>
      <h1>useMemo</h1>
      <div>
        <input
          type="number"
          value={number === "" ? "" : number}
          onChange={(e) => {
            const val = e.target.value;
            setNumber(val === "" ? "" : Number(val));
          }}
        />
      </div>
      <p>The result is {expensiveResult}.</p>
    </div>
  );
};

export default ExpensiveCalculation;
