import { describe, it, expect, beforeEach } from "vitest";
import { renderHook, act } from "@testing-library/react";
import useBookStats from "../hooks/useBookStats.js";
import useLocalStorage from "../hooks/useLocalStorage.js";

describe("useBookStats", () => {
  it("menghitung jumlah buku per status", () => {
    const books = [
      { id: "1", judul: "A", penulis: "X", status: "milik" },
      { id: "2", judul: "B", penulis: "Y", status: "baca" },
      { id: "3", judul: "C", penulis: "Z", status: "beli" },
    ];
    const { result } = renderHook(() => useBookStats(books));
    expect(result.current).toEqual({ total: 3, milik: 1, baca: 1, beli: 1 });
  });
});

describe("useLocalStorage", () => {
  beforeEach(() => localStorage.clear());

  it("menyimpan nilai baru ke localStorage", () => {
    const { result } = renderHook(() => useLocalStorage("kunci-uji", []));
    act(() => result.current[1](["buku"]));
    expect(JSON.parse(localStorage.getItem("kunci-uji"))).toEqual(["buku"]);
  });
});
