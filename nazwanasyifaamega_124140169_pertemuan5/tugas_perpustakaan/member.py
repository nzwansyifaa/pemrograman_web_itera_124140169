"""Modul anggota perpustakaan."""


class Member:
    """Anggota perpustakaan yang dapat meminjam item.

    Atribut:
        __id_anggota (private): nomor anggota.
        __daftar_pinjaman (private): id item yang sedang dipinjam.
    """

    BATAS_PINJAM = 3

    def __init__(self, id_anggota: str, nama: str):
        self.__id_anggota = id_anggota
        self._nama = nama
        self.__daftar_pinjaman = []

    @property
    def id_anggota(self) -> str:
        """Mengembalikan nomor anggota (read-only)."""
        return self.__id_anggota

    @property
    def nama(self) -> str:
        """Mengembalikan nama anggota."""
        return self._nama

    @property
    def daftar_pinjaman(self) -> list:
        """Mengembalikan salinan daftar id item yang sedang dipinjam."""
        return list(self.__daftar_pinjaman)

    def bisa_meminjam(self) -> bool:
        """Mengembalikan True jika anggota belum mencapai batas pinjam."""
        return len(self.__daftar_pinjaman) < self.BATAS_PINJAM

    def catat_pinjam(self, item_id: str):
        """Mencatat item yang dipinjam anggota."""
        self.__daftar_pinjaman.append(item_id)

    def catat_kembali(self, item_id: str):
        """Menghapus item dari daftar pinjaman anggota."""
        if item_id in self.__daftar_pinjaman:
            self.__daftar_pinjaman.remove(item_id)

    def __str__(self) -> str:
        return f"Anggota {self.id_anggota} - {self._nama} (pinjaman aktif: {len(self.__daftar_pinjaman)})"
