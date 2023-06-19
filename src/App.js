import './App.css';
import Navbar from "./Components/NavBar"
import Home from "./Pages/Home"
import Instructor from "./Pages/Instructor"
import Student from "./Pages/Student"
import IRT from "./Pages/IRT Model"
import { Route, Routes } from "react-router-dom"
import backgroundImage from "./Images/bg.jpg"
import Background from "./Components/BackGround"

function App() {
  return (
    <>
      <Background image={backgroundImage} />
      <div className="fixed top-0 left-0 right-0 bottom-0" style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center' }}></div>
      <div className="relative z-0">
      <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/instructor" element={<Instructor />} />
          <Route path="/student" element={<Student />} />
          <Route path="/irt" element={<IRT />} />
        </Routes>
      </div>


    </>
  );
}

export default App;
