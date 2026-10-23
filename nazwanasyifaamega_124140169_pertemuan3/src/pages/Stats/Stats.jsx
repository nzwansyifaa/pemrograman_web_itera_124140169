import { useBooks } from "../../context/BookContext.jsx";
import useBookStats from "../../hooks/useBookStats.js";

function Stats() {
  const { books } = useBooks();
  const { total, milik, baca, beli } = useBookStats(books);

  return (
    <section className="panel">
      <h2>Statistik buku</h2>
      <ul className="statistik">
        <li>Total buku: <strong>{total}</strong></li>
        <li>Milik: <strong>{milik}</strong></li>
        <li>Sedang dibaca: <strong>{baca}</strong></li>
        <li>Ingin dibeli: <strong>{beli}</strong></li>
      </ul>
    </section>
  );
}

export default Stats;
