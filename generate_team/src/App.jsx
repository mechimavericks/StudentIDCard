import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import TeamMembers from "./TeamMembers";
import "./App.css";
import Home from "./Home";

function App() {
  return (
    <>
      <div className="h-screen bg-cover bg-bottom bg-custom">
        <div className="absolute inset-0 bg-black/5 backdrop-blur-[4px]"></div>
        <div className="relative z-10 h-full flex justify-center items-center px-[8%] py-[5%]">
          <div className="bg-black/30 bg-opacity-50 backdrop-blur-sm w-full h-full">
            <Router>
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/team" element={<TeamMembers />} />
              </Routes>
            </Router>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
