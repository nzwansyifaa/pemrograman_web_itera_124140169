import { useState } from "react";
import PropTypes from "prop-types";
import { STATUS_OPTIONS, bookShape } from "../../constants.js";

// Form tambah/edit buku (controlled components + validasi)
function BookForm({ onSubmit, initialBook, onCancel }) {
  const [judul, setJudul] = useState(initialBook?.judul ?? "");
  const [penulis, setPenulis] = useState(initialBook?.penulis ?? "");
  const [status, setStatus] = useState(initialBook?.status ?? "milik");
  const [errors, setErrors] = useState({});

  const handleSubmit = (event) => {
    event.preventDefault();

    // Validasi kolom wajib isi
    const newErrors = {};
    if (judul.trim() === "") newErrors.judul = "Judul wajib diisi.";
    if (penulis.trim() === "") newErrors.penulis = "Penulis wajib diisi.";
    setErrors(newErrors);
    if (Object.keys(newErrors).length > 0) return;

    onSubmit({ judul: judul.trim(), penulis: penulis.trim(), status });

    if (!initialBook) {
      setJudul("");
      setPenulis("");
      setStatus("milik");
    }
  };

  return (
    <form className="panel" onSubmit={handleSubmit} noValidate>
      <h2>{initialBook ? "Edit buku" : "Tambah buku"}</h2>

      <label htmlFor="judul">Judul buku</label>
      <input
        id="judul"
        type="text"
        value={judul}
        className={errors.judul ? "invalid" : ""}
        onChange={(e) => setJudul(e.target.value)}
      />
      {errors.judul && <p className="error">{errors.judul}</p>}

      <label htmlFor="penulis">Penulis</label>
      <input
        id="penulis"
        type="text"
        value={penulis}
        className={errors.penulis ? "invalid" : ""}
        onChange={(e) => setPenulis(e.target.value)}
      />
      {errors.penulis && <p className="error">{errors.penulis}</p>}

      <label htmlFor="status">Status</label>
      <select id="status" value={status} onChange={(e) => setStatus(e.target.value)}>
        {STATUS_OPTIONS.map(({ value, label }) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>

      <button type="submit" className="btn btn-utama">
        {initialBook ? "Simpan perubahan" : "Tambah buku"}
      </button>
      {onCancel && (
        <button type="button" className="btn btn-sekunder" onClick={onCancel}>
          Batal
        </button>
      )}
    </form>
  );
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialBook: bookShape,
  onCancel: PropTypes.func,
};

export default BookForm;
