import { useEffect } from "react";
import { api, controller } from "./api";

function TestAPI() {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await api.post("/posts", {
          title: "API Test",
          body: "Welcome to Focus Bear!",
          userId: 1,
        });
        console.log("Response:", res.data);
        // Redirect after successful response
        window.location.href = "/success";
      } catch (err) {
        console.error("Failed request:", err.message);
      }
    };

    fetchData();

    return () => controller.abort(); // Cancel if component unmounts
  }, []);

  return <div>POST request sent. Check the console!</div>;
}

export default TestAPI;
