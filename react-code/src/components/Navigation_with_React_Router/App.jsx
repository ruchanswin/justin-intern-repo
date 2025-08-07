import "./App.css";
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import Home from "./components/Navigation_with_React_Router/Home";
import Profile from "./components/Navigation_with_React_Router/Profile";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;

