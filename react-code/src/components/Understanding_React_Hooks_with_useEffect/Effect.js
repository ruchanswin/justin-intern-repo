import { useEffect, useState } from "react";

const Effect = () => {
  const [data, setData] = useState(null);
  const [show, setShow] = useState(true);

  // Logs a message when it mounts and unmounts.
  useEffect(() => {
    console.log("Component mounted");

    return () => {
      console.log("Component unmounted");
    };
  }, []);

  // Fetches data from an API when a button is clicked.
  const fetchData = async () => {
    try {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/todos/1",
      );
      const json = await response.json();
      setData(json);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  if (!show)
    return (
      <div>
        <p>Component hidden</p>
        <button onClick={() => setShow(true)}>Mount Component</button>
      </div>
    );

  return (
    <div style={{ padding: "1rem", border: "1px solid #ccc" }}>
      <h2>useEffect</h2>
      <button onClick={fetchData}>Fetch Data</button>
      <button onClick={() => setShow(false)} style={{ marginLeft: "1rem" }}>
        Unmount Component
      </button>

      {data && (
        <div style={{ marginTop: "1rem" }}>
          <strong>Title:</strong> {data.title}
          <p>{data.body}</p>
        </div>
      )}
    </div>
  );
};

export default Effect;
