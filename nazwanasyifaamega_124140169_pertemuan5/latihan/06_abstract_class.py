# Latihan 6: Abstract class, @abstractmethod, abstract property, dan interface

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def luas(self) -> float:
        """Menghitung luas bangun datar."""

    @abstractmethod
    def keliling(self) -> float:
        """Menghitung keliling bangun datar."""

    def cetak_laporan(self):
        print(f"[{self.nama}] Luas: {self.luas():.2f} | Keliling: {self.keliling():.2f}")


class PersegiPanjang(Shape):
    def __init__(self, panjang: float, lebar: float):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> float:
        return self.panjang * self.lebar

    def keliling(self) -> float:
        return 2 * (self.panjang + self.lebar)


class Lingkaran(Shape):
    def __init__(self, radius: float):
        super().__init__("Lingkaran")
        self.radius = radius

    def luas(self) -> float:
        return math.pi * (self.radius ** 2)

    def keliling(self) -> float:
        return 2 * math.pi * self.radius


class DatabaseConnector(ABC):
    @property
    @abstractmethod
    def driver_name(self) -> str:
        """Abstract property: nama mesin database."""

    @abstractmethod
    def connect(self, host: str, port: int, database: str) -> bool:
        """Membuka koneksi database."""

    @abstractmethod
    def execute_query(self, sql: str) -> list:
        """Menjalankan query SQL."""

    @abstractmethod
    def disconnect(self):
        """Menutup koneksi database."""


class PostgreSQLConnector(DatabaseConnector):
    @property
    def driver_name(self) -> str:
        return "PostgreSQL (psycopg2)"

    def connect(self, host: str, port: int, database: str) -> bool:
        print(f"[{self.driver_name}] Terhubung ke postgresql://{host}:{port}/{database} [OK]")
        return True

    def execute_query(self, sql: str) -> list:
        print(f"[{self.driver_name}] Menjalankan SQL: '{sql}'")
        return [{"id": 1, "nama": "Kim Jongseob"}, {"id": 2, "nama": "Choi Seunghyun"}]

    def disconnect(self):
        print(f"[{self.driver_name}] Koneksi database ditutup.")


class SegitigaCacat(Shape):
    """Sengaja lupa mengimplementasikan keliling()."""

    def __init__(self, alas: float, tinggi: float):
        super().__init__("Segitiga Cacat")
        self.alas = alas
        self.tinggi = tinggi

    def luas(self) -> float:
        return 0.5 * self.alas * self.tinggi


if __name__ == "__main__":
    print("--- 1. Implementasi Shape ---")
    PersegiPanjang(10, 5).cetak_laporan()
    Lingkaran(7).cetak_laporan()

    print("\n--- 2. Enforcement Abstract Class ---")
    try:
        Shape("Bentuk Abstrak")
    except TypeError as err:
        print(f"Penolakan Python: {err}")
    try:
        SegitigaCacat(6, 8)
    except TypeError as err:
        print(f"Penolakan Subclass Cacat: {err}")

    print("\n--- 3. Interface Database ---")
    db = PostgreSQLConnector()
    db.connect("localhost", 5432, "paw_praktikum_db")
    print("Hasil Query:", db.execute_query("SELECT id, nama FROM mahasiswa;"))
    db.disconnect()
