import { createContext, useContext, useState } from "react";
import PropTypes from "prop-types";
import useLocalStorage from "../hooks/useLocalStorage.js";

const BookContext = createContext(null);

// Provider: menyimpan data buku, filter, dan pencarian untuk seluruh aplikasi
export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage("manajemen_buku", []);
  const [statusFilter, setStatusFilter] = useState("semua");
  const [searchQuery, setSearchQuery] = useState("");

  const addBook = (data) => {
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    setBooks((prev) => [...prev, { id, ...data }]);
  };

  const updateBook = (id, data) => {
    setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...data } : b)));
  };

  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
  };

  // Filter berdasarkan status, lalu cari di judul atau penulis
  const keyword = searchQuery.trim().toLowerCase();
  const filteredBooks = books.filter((b) => {
    const cocokStatus = statusFilter === "semua" || b.status === statusFilter;
    const cocokCari =
      b.judul.toLowerCase().includes(keyword) ||
      b.penulis.toLowerCase().includes(keyword);
    return cocokStatus && cocokCari;
  });

  const value = {
    books,
    filteredBooks,
    addBook,
    updateBook,
    deleteBook,
    statusFilter,
    setStatusFilter,
    searchQuery,
    setSearchQuery,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

// Hook untuk memakai context (error jika dipakai di luar provider)
export function useBooks() {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error("useBooks harus dipakai di dalam BookProvider");
  }
  return context;
}
