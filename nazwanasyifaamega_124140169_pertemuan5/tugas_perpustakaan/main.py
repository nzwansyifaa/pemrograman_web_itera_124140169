"""Program utama: menguji sistem manajemen perpustakaan."""

from library_item import LibraryItem, Book, Magazine
from library import Library
from member import Member


def cetak_judul(teks: str):
    """Mencetak judul bagian program."""
    print(f"\n{'#' * 60}\n# {teks}\n{'#' * 60}")


def main():
    """Menjalankan seluruh skenario uji sistem perpustakaan."""
    perpus = Library("Perpustakaan ITERA")
    anggota = Member("A001", "Nazwa")

    cetak_judul("1. MENAMBAHKAN ITEM")
    perpus.tambah_item(Book("B001", "Bumi", 2014, "Tere Liye", 440))
    perpus.tambah_item(Book("B002", "Laut Bercerita", 2017, "Leila S. Chudori", 379))
    perpus.tambah_item(Book("B003", "Touché", 2011, "Windhy Puspitadewi", 208))
    perpus.tambah_item(Magazine("M001", "Info Komputer", 2024, "Oktober", "Media Digital"))
    perpus.tambah_item(Magazine("M002", "Tekno Masa Kini", 2023, "Juli", "Pustaka Nusantara"))
    perpus.tambah_item(Book("B001", "Buku Dengan ID Kembar", 2022, "Anonim", 100))  # id duplikat

    cetak_judul("2. MENAMPILKAN KATALOG")
    perpus.tampilkan_katalog()

    cetak_judul("3. PENCARIAN ITEM")
    print("Cari judul 'laut':")
    for item in perpus.cari_by_judul("laut"):
        print(f"  - {item.get_detail()}")
    item = perpus.cari_by_id("M001")
    print("Cari id 'M001':", item.get_detail() if item else "tidak ditemukan")
    print("Cari id 'X999':", "tidak ditemukan" if perpus.cari_by_id("X999") is None else "ada")

    cetak_judul("4. PEMINJAMAN DAN STATUS KETERSEDIAAN")
    perpus.pinjam_item("B001", anggota)
    perpus.pinjam_item("M001", anggota)
    perpus.pinjam_item("B001", Member("A002", "Iqbal"))  # sudah dipinjam
    perpus.tampilkan_katalog(hanya_tersedia=True)
    print(f"\n{anggota}")

    cetak_judul("5. PENGEMBALIAN DAN DENDA (POLYMORPHISM)")
    perpus.kembalikan_item("B001", anggota, hari_terlambat=3)  # buku: Rp 1.000/hari
    perpus.kembalikan_item("M001", anggota, hari_terlambat=3)  # majalah: Rp 500/hari
    perpus.tampilkan_katalog(hanya_tersedia=False)

    cetak_judul("6. UJI ENCAPSULATION DAN ABSTRACT CLASS")
    buku = perpus.cari_by_id("B002")
    try:
        print(buku.__dipinjam)
    except AttributeError:
        print("Akses langsung buku.__dipinjam GAGAL (atribut private).")
    try:
        buku.tahun_terbit = 3000
    except ValueError as err:
        print(f"Validasi setter tahun_terbit: {err}")
    try:
        LibraryItem("X001", "Item Abstrak", 2020)
    except TypeError as err:
        print(f"LibraryItem tidak bisa dibuat langsung: {err}")


if __name__ == "__main__":
    main()
