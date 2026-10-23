import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import BookForm from "../components/BookForm/BookForm.jsx";

describe("BookForm", () => {
  it("menampilkan pesan error jika form kosong dikirim", () => {
    const onSubmit = vi.fn();
    render(<BookForm onSubmit={onSubmit} />);

    fireEvent.click(screen.getByRole("button", { name: /tambah buku/i }));

    expect(screen.getByText("Judul wajib diisi.")).toBeInTheDocument();
    expect(screen.getByText("Penulis wajib diisi.")).toBeInTheDocument();
    expect(onSubmit).not.toHaveBeenCalled();
  });

  it("memanggil onSubmit dengan data yang benar", () => {
    const onSubmit = vi.fn();
    render(<BookForm onSubmit={onSubmit} />);

    fireEvent.change(screen.getByLabelText(/judul buku/i), { target: { value: "Atomic Habits" } });
    fireEvent.change(screen.getByLabelText(/penulis/i), { target: { value: "James Clear" } });
    fireEvent.change(screen.getByLabelText(/status/i), { target: { value: "baca" } });
    fireEvent.click(screen.getByRole("button", { name: /tambah buku/i }));

    expect(onSubmit).toHaveBeenCalledWith({
      judul: "Atomic Habits",
      penulis: "James Clear",
      status: "baca",
    });
  });
});
