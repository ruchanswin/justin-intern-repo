import { Link } from "react-router-dom";

const Profile = () => {
  return (
    <div style={{ padding: "2rem" }}>
      <h2>Profile</h2>
      <p>This is your profile!</p>
      <Link to="/home">Home</Link>
    </div>
  );
};

export default Profile;
