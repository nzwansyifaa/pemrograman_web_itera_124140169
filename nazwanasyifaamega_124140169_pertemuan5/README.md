# Tugas Pertemuan 5: Sistem Manajemen Perpustakaan (Python OOP)

**Praktikum Pengembangan Aplikasi Web - Pertemuan 5 (Python OOP)**

- Nama: Nazwa Nasyifa Mega
- NIM: 124140169
- Kelas: PAW RA

## Deskripsi Program

Program ini adalah sistem manajemen perpustakaan sederhana berbasis OOP Python. Perpustakaan menyimpan koleksi **buku** dan **majalah**. Pengguna dapat menambahkan item, menampilkan katalog item yang tersedia, mencari item berdasarkan judul atau id, meminjam dan mengembalikan item, serta menghitung denda keterlambatan.

### Alur Program (`main.py`)

1. Membuat perpustakaan dan satu anggota, lalu menambahkan 3 buku dan 2 majalah (termasuk uji penambahan dengan id kembar yang ditolak).
2. Menampilkan katalog item yang tersedia.
3. Mencari item berdasarkan judul (kata kunci) dan berdasarkan id.
4. Meminjam item, lalu menampilkan katalog lagi. Item yang sedang dipinjam tidak muncul di katalog tersedia.
5. Mengembalikan item dan menghitung denda keterlambatan.
6. Menguji proteksi atribut private, validasi setter, dan larangan membuat objek dari abstract class.

### Penerapan Konsep OOP

| Konsep | Penerapan | Lokasi |
|---|---|---|
| Abstract class dan inheritance | `LibraryItem(ABC)` memiliki abstract method `get_detail()` dan `hitung_denda()`. `Book` dan `Magazine` mewarisinya dan wajib mengimplementasikan keduanya. | `library_item.py` |
| Encapsulation | Atribut `__dipinjam` dan `__tahun_terbit` (private), `_judul` dan `_item_id` (protected), `__koleksi` pada `Library`, serta `__daftar_pinjaman` pada `Member`. Perubahan status hanya lewat method `pinjam()` dan `kembalikan()`. | `library_item.py`, `library.py`, `member.py` |
| Property decorator | `@property` untuk `item_id`, `judul`, `tahun_terbit` (dengan `@tahun_terbit.setter` yang memvalidasi tahun), dan `is_dipinjam`. | `library_item.py` |
| Polymorphism | `hitung_denda()` memberi hasil berbeda untuk buku (Rp 1.000 per hari) dan majalah (Rp 500 per hari). `Library.kembalikan_item()` cukup memanggil `item.hitung_denda()` tanpa memeriksa jenis item. | `library.py` |
| Class | `Library` mengelola koleksi, `Member` mewakili anggota. | `library.py`, `member.py` |

## Cara Menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal di folder `nazwanasyifaamega_124140169_pertemuan5`, lalu jalankan:

```bash
# Program tugas
cd tugas_perpustakaan
python main.py

# File latihan (dari folder pertemuan5)
cd ..
python latihan/01_everything_is_object.py
python latihan/02_class_object.py
```

Jika perintah `python` tidak dikenali, gunakan `python3`.

## Screenshot Output

### Penambahan item dan tampilan katalog
![Tambah item dan katalog](screenshots/1-tambah-dan-katalog.png)

### Pencarian item
![Pencarian](screenshots/2-pencarian.png)

### Peminjaman, pengembalian, dan denda
![Peminjaman dan denda](screenshots/3-peminjaman-dan-denda.png)

### Uji encapsulation dan abstract class
![Encapsulation dan abstract class](screenshots/4-encapsulation.png)

## Struktur Folder

```
nazwanasyifaamega_124140169_pertemuan5/
├── latihan/
│   ├── 01_everything_is_object.py
│   ├── 01_procedural_vs_oop.py
│   ├── 02_class_object.py
│   ├── 03_inheritance.py
│   ├── 04_encapsulation.py
│   ├── 05_polymorphism.py
│   └── 06_abstract_class.py
├── tugas_perpustakaan/
│   ├── library_item.py
│   ├── member.py
│   ├── library.py
│   └── main.py
├── screenshots/
├── README.md
└── .gitignore
```
