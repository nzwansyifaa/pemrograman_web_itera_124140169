"""Modul item perpustakaan: abstract class LibraryItem beserta subclass Book dan Magazine."""

from abc import ABC, abstractmethod
from datetime import date


class LibraryItem(ABC):
    """Abstract class dasar untuk semua item di perpustakaan.

    Atribut:
        _item_id (protected): kode unik item.
        _judul (protected): judul item.
        __tahun_terbit (private): tahun terbit, dilindungi property dan validasi.
        __dipinjam (private): status peminjaman, hanya diubah lewat pinjam() dan kembalikan().
    """

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        self._item_id = item_id
        self._judul = judul
        self.__dipinjam = False
        self.__tahun_terbit = 0
        self.tahun_terbit = tahun_terbit  # memanggil setter agar divalidasi

    # ---------- Property ----------
    @property
    def item_id(self) -> str:
        """Mengembalikan kode unik item (read-only)."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Mengembalikan judul item (read-only)."""
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        """Mengembalikan tahun terbit."""
        return self.__tahun_terbit

    @tahun_terbit.setter
    def tahun_terbit(self, nilai: int):
        """Mengubah tahun terbit; harus berupa angka antara 1000 dan tahun sekarang."""
        if not isinstance(nilai, int) or not 1000 <= nilai <= date.today().year:
            raise ValueError("Tahun terbit tidak valid!")
        self.__tahun_terbit = nilai

    @property
    def is_dipinjam(self) -> bool:
        """Mengembalikan True jika item sedang dipinjam (read-only)."""
        return self.__dipinjam

    # ---------- Method konkret ----------
    def pinjam(self) -> bool:
        """Menandai item sebagai dipinjam. Mengembalikan False jika sudah dipinjam."""
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Menandai item sebagai dikembalikan. Mengembalikan False jika belum dipinjam."""
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    def __str__(self) -> str:
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"{self.get_detail()} | Status: {status}"

    # ---------- Method abstract (wajib dioverride subclass) ----------
    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan teks detail item."""

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan.

        Parameter:
            hari_terlambat (int): jumlah hari keterlambatan.

        Mengembalikan:
            float: besar denda dalam rupiah.
        """


class Book(LibraryItem):
    """Buku. Denda Rp 1.000 per hari."""

    DENDA_PER_HARI = 1000

    def __init__(self, item_id: str, judul: str, tahun_terbit: int, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul, tahun_terbit)
        self._penulis = penulis
        self._jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        return (f"[Buku] {self.item_id} - {self.judul} ({self.tahun_terbit}) "
                f"oleh {self._penulis}, {self._jumlah_halaman} halaman")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI


class Magazine(LibraryItem):
    """Majalah. Denda Rp 500 per hari."""

    DENDA_PER_HARI = 500

    def __init__(self, item_id: str, judul: str, tahun_terbit: int, edisi: str, penerbit: str):
        super().__init__(item_id, judul, tahun_terbit)
        self._edisi = edisi
        self._penerbit = penerbit

    def get_detail(self) -> str:
        return (f"[Majalah] {self.item_id} - {self.judul} ({self.tahun_terbit}) "
                f"edisi {self._edisi}, penerbit {self._penerbit}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI
