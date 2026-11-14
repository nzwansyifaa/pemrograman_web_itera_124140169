"""Modul Library: mengelola koleksi item perpustakaan."""

from library_item import LibraryItem
from member import Member


class Library:
    """Perpustakaan yang menyimpan dan mengelola koleksi LibraryItem.

    Atribut:
        __koleksi (private): dictionary {item_id: LibraryItem}.
    """

    def __init__(self, nama: str):
        self.nama = nama
        self.__koleksi = {}

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item ke koleksi. Gagal jika bukan LibraryItem atau id sudah dipakai."""
        if not isinstance(item, LibraryItem):
            print("Gagal: objek yang ditambahkan harus turunan LibraryItem.")
            return False
        if item.item_id in self.__koleksi:
            print(f"Gagal: item dengan id {item.item_id} sudah ada.")
            return False
        self.__koleksi[item.item_id] = item
        print(f"Berhasil menambahkan: {item.judul}")
        return True

    def tampilkan_katalog(self, hanya_tersedia: bool = True):
        """Menampilkan daftar item (secara default hanya yang tersedia)."""
        judul = "ITEM TERSEDIA" if hanya_tersedia else "SELURUH KOLEKSI"
        print(f"\n=== {judul} DI {self.nama.upper()} ===")
        ditampilkan = 0
        for item in self.__koleksi.values():
            if hanya_tersedia and item.is_dipinjam:
                continue
            ditampilkan += 1
            print(f"{ditampilkan}. {item}")
        if ditampilkan == 0:
            print("(tidak ada item)")

    def cari_by_id(self, item_id: str):
        """Mencari item berdasarkan id. Mengembalikan item atau None."""
        return self.__koleksi.get(item_id)

    def cari_by_judul(self, kata_kunci: str) -> list:
        """Mencari item yang judulnya memuat kata kunci (tidak peka huruf besar/kecil)."""
        kata = kata_kunci.lower()
        return [item for item in self.__koleksi.values() if kata in item.judul.lower()]

    def pinjam_item(self, item_id: str, anggota: Member) -> bool:
        """Memproses peminjaman item oleh anggota."""
        item = self.cari_by_id(item_id)
        if item is None:
            print(f"Gagal: item {item_id} tidak ditemukan.")
        elif not anggota.bisa_meminjam():
            print(f"Gagal: {anggota.nama} sudah mencapai batas pinjam ({Member.BATAS_PINJAM} item).")
        elif not item.pinjam():
            print(f"Gagal: '{item.judul}' sedang dipinjam.")
        else:
            anggota.catat_pinjam(item_id)
            print(f"{anggota.nama} berhasil meminjam '{item.judul}'.")
            return True
        return False

    def kembalikan_item(self, item_id: str, anggota: Member, hari_terlambat: int = 0) -> float:
        """Memproses pengembalian item dan mengembalikan denda (0 jika tepat waktu)."""
        item = self.cari_by_id(item_id)
        if item is None or item_id not in anggota.daftar_pinjaman:
            print(f"Gagal: {anggota.nama} tidak sedang meminjam item {item_id}.")
            return 0.0
        item.kembalikan()
        anggota.catat_kembali(item_id)
        denda = item.hitung_denda(hari_terlambat)  # polymorphism: perilaku tergantung jenis item
        print(f"'{item.judul}' dikembalikan oleh {anggota.nama}. Denda: Rp {denda:,.0f}")
        return denda

    def daftar_item(self) -> list:
        """Mengembalikan salinan daftar seluruh item."""
        return list(self.__koleksi.values())
