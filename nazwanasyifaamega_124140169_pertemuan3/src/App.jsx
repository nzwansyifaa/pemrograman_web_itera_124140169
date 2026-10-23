import { Routes, Route, NavLink } from "react-router-dom";
import Home from "./pages/Home/Home.jsx";
import Stats from "./pages/Stats/Stats.jsx";

function App() {
  return (
    <div>
      <header className="topbar">
        <h1>Manajemen Buku Pribadi</h1>
        <nav>
          <NavLink to="/" end>
            Beranda
          </NavLink>
          <NavLink to="/statistik">Statistik</NavLink>
        </nav>
      </header>

      <main className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/statistik" element={<Stats />} />
          <Route path="*" element={<p>Halaman tidak ditemukan.</p>} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
