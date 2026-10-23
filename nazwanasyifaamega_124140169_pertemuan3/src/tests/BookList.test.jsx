import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import BookList from "../components/BookList/BookList.jsx";

const contohBuku = [
  { id: "1", judul: "Laskar Pelangi", penulis: "Andrea Hirata", status: "baca" },
];

describe("BookList", () => {
  it("menampilkan pesan kosong jika tidak ada buku", () => {
    render(<BookList books={[]} onEdit={vi.fn()} onDelete={vi.fn()} />);
    expect(screen.getByText(/belum ada buku/i)).toBeInTheDocument();
  });

  it("menampilkan buku dan memanggil onDelete saat tombol Hapus diklik", () => {
    const onDelete = vi.fn();
    render(<BookList books={contohBuku} onEdit={vi.fn()} onDelete={onDelete} />);

    expect(screen.getByText("Laskar Pelangi")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /hapus/i }));
    expect(onDelete).toHaveBeenCalledWith("1");
  });
});
