import { useSelector } from "react-redux";
import { selectCounter } from "./store";

const Message = () => {
  const count = useSelector(selectCounter);

  let message = "Let's go!";
  if (count > 5) message = "Push yourself further!";
  else if (count < 5 && count > 0) message = "Keep it up!";
  else if (count < 0) message = "Don't give up just yet!";
  
  return (
    <div>
      <h1>Our lovely message:</h1>
      <p>{message}</p>
    </div>
  );
};

export default Message;
