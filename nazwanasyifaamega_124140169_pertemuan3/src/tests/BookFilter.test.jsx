import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import BookFilter from "../components/BookFilter/BookFilter.jsx";

describe("BookFilter", () => {
  it("memanggil onSearchChange saat mengetik di kolom pencarian", () => {
    const onSearchChange = vi.fn();
    render(
      <BookFilter
        statusFilter="semua"
        searchQuery=""
        onStatusChange={vi.fn()}
        onSearchChange={onSearchChange}
      />
    );

    fireEvent.change(screen.getByPlaceholderText(/cari judul/i), { target: { value: "laskar" } });
    expect(onSearchChange).toHaveBeenCalledWith("laskar");
  });
});
