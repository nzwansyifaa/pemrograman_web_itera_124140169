import { useState, useEffect } from "react";

// Custom hook 1: state yang otomatis tersimpan di localStorage
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const tersimpan = localStorage.getItem(key);
      return tersimpan !== null ? JSON.parse(tersimpan) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  // Setiap value berubah, simpan ke localStorage
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error("Gagal menyimpan ke localStorage", error);
    }
  }, [key, value]);

  return [value, setValue];
}

export default useLocalStorage;
