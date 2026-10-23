import PropTypes from "prop-types";
import { bookShape, getStatusLabel } from "../../constants.js";

// Daftar buku (conditional rendering + list dengan key)
function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p className="kosong">Belum ada buku yang cocok.</p>;
  }

  return (
    <ul className="daftar">
      {books.map((book) => (
        <li key={book.id} className="buku">
          <div>
            <strong>{book.judul}</strong>
            <div className="info">
              {book.penulis} | {getStatusLabel(book.status)}
            </div>
          </div>
          <div>
            <button className="btn btn-kecil btn-edit" onClick={() => onEdit(book)}>
              Edit
            </button>
            <button className="btn btn-kecil btn-hapus" onClick={() => onDelete(book.id)}>
              Hapus
            </button>
          </div>
        </li>
      ))}
    </ul>
  );
}

BookList.propTypes = {
  books: PropTypes.arrayOf(bookShape).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default BookList;
