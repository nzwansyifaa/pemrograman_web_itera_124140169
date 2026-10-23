import { useMemo } from "react";

// Custom hook 2: menghitung statistik buku berdasarkan status
function useBookStats(books) {
  return useMemo(() => {
    const stats = { total: books.length, milik: 0, baca: 0, beli: 0 };
    books.forEach((book) => {
      if (stats[book.status] !== undefined) stats[book.status] += 1;
    });
    return stats;
  }, [books]);
}

export default useBookStats;
