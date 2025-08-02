import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div style={{ padding: "2rem" }}>
      <h2>Home Page</h2>
      <p>This is your homepage!</p>
      <Link to="/profile">Profile</Link>
    </div>
  );
};

export default Home;
