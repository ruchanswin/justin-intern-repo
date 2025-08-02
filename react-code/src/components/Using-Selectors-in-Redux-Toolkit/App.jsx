import Counter from "./counter";
import Message from "./message";

const App = () => {
  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Redux Selector Demo</h1>
      <Counter />
      <Message />
    </div>
  );
};

export default App;
