import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Courses from './pages/Courses';
import Forum from './pages/Forum';
import Exchange from './pages/Exchange';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/courses" element={<Courses />} />
        <Route path="/forum" element={<Forum />} />
        <Route path="/exchange" element={<Exchange />} />
      </Routes>
    </Router>
  );
}

export default App;
