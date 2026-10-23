import { useState, useEffect } from "react";
import { useBooks } from "../../context/BookContext.jsx";
import BookForm from "../../components/BookForm/BookForm.jsx";
import BookList from "../../components/BookList/BookList.jsx";
import BookFilter from "../../components/BookFilter/BookFilter.jsx";

function Home() {
  const {
    filteredBooks,
    addBook,
    updateBook,
    deleteBook,
    statusFilter,
    setStatusFilter,
    searchQuery,
    setSearchQuery,
  } = useBooks();
  const [editingBook, setEditingBook] = useState(null);

  // useEffect: ubah judul tab browser sesuai mode (tambah/edit)
  useEffect(() => {
    document.title = editingBook ? "Edit Buku" : "Manajemen Buku";
  }, [editingBook]);

  const handleSubmit = (data) => {
    if (editingBook) {
      updateBook(editingBook.id, data);
      setEditingBook(null);
    } else {
      addBook(data);
    }
  };

  const handleDelete = (id) => {
    if (window.confirm("Hapus buku ini?")) {
      deleteBook(id);
      if (editingBook?.id === id) setEditingBook(null);
    }
  };

  return (
    <div className="dua-kolom">
      {/* key mengubah form menjadi baru setiap pindah buku yang diedit */}
      <BookForm
        key={editingBook?.id ?? "baru"}
        initialBook={editingBook}
        onSubmit={handleSubmit}
        onCancel={editingBook ? () => setEditingBook(null) : undefined}
      />

      <section className="panel">
        <h2>Daftar buku</h2>
        <BookFilter
          statusFilter={statusFilter}
          searchQuery={searchQuery}
          onStatusChange={setStatusFilter}
          onSearchChange={setSearchQuery}
        />
        <BookList books={filteredBooks} onEdit={setEditingBook} onDelete={handleDelete} />
      </section>
    </div>
  );
}

export default Home;
