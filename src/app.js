import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";
import LagnaChart from "./LagnaChart";
import Transits from "./Transits";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/lagna" element={<LagnaChart />} />
        <Route path="/transits" element={<Transits />} />
      </Routes>
    </Router>
  );
}

export default App;
 