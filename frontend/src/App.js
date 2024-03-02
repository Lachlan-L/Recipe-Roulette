import { BrowserRouter, Route, Routes } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import Roulette from "./pages/Roulette";

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/spin" element={<Roulette />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
