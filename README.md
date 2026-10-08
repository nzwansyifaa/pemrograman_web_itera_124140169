# Mini POS: Kasir & Keranjang Belanja Kantin

## Identitas
- **Nama Lengkap:** Nazwa Nasyifaa Mega
- **NIM:** 124140169
- **Kelas Praktikum:** PAW RA

## Deskripsi Aplikasi
Mini POS adalah aplikasi web kasir sederhana untuk kantin atau toko kampus. Kasir memasukkan barang, aplikasi menghitung subtotal, total, diskon, dan kembalian secara otomatis. Isi keranjang tersimpan di `localStorage`, jadi tidak hilang saat halaman di-refresh. Studi kasus: kasir kantin kampus.

## Panduan Menjalankan
1. Clone atau unduh repository ini.
2. Buka folder `nazwansyifaamega_124140169_pertemuan1` di VS Code.
3. Klik kanan `index.html`, pilih **Open with Live Server**.

## Daftar Fitur
- [x] Validasi nama barang (wajib, minimal 3 karakter)
- [x] Validasi harga satuan (angka, minimal Rp 500)
- [x] Validasi qty (angka bulat, minimal 1)
- [x] Pesan error merah di bawah input, barang tidak masuk keranjang jika tidak valid
- [x] Form otomatis di-reset setelah barang berhasil ditambahkan
- [x] Subtotal per barang dan total belanja otomatis
- [x] Diskon 10% jika total belanja minimal Rp 50.000
- [x] Kalkulator uang bayar dan kembalian, dengan keterangan jika uang kurang
- [x] Tabel keranjang (No, Nama Barang, Harga Satuan, Qty, Subtotal, Aksi) dan tombol Hapus
- [x] Penyimpanan keranjang di `localStorage`
- [x] Tombol Transaksi Baru untuk mengosongkan keranjang dan `localStorage`
- [x] Tampilan responsif dan format Rupiah

## Tangkapan Layar
1. Form utama
![Form utama](screenshots/Screenshot%202026-10-08%20161105.png)
2. Validasi error
![Validasi error](screenshots/Screenshot%202026-10-08%20161135.png)
![validasi erroe](screenshots/Screenshot%202026-10-08%20161157.png)
3. Hasil perhitungan
![Hasil perhitungan](screenshots/Screenshot%202026-10-08%20161258.png)

## Penjelasan Teknis Singkat
- **Validasi input:** fungsi `validasiForm()` memeriksa nama (`trim()` dan panjang >= 3), harga (`Number()`, tidak kosong, >= 500), dan qty (`Number.isInteger()`, >= 1). Setiap error ditampilkan lewat `tampilkanError()`. Jika ada yang salah, fungsi mengembalikan `null` sehingga barang tidak ditambahkan.
- **Kalkulator:** `hitungRingkasan()` menjumlahkan `harga * qty` seluruh item memakai `reduce()`. Jika total >= Rp 50.000, diskon = 10% dari total. Total akhir = total - diskon. Kembalian = uang bayar - total akhir; jika uang bayar lebih kecil, aplikasi menampilkan kekurangannya.
- **Serialisasi localStorage:** array `keranjang` diubah ke teks dengan `JSON.stringify()` lalu disimpan lewat `localStorage.setItem()`. Saat halaman dibuka, `JSON.parse()` mengembalikannya menjadi array. Tombol Transaksi Baru memanggil `localStorage.removeItem()`.

## Struktur Folder
```
nazwanasyifaamega_124140169_pertemuan1/
├── screenshots/
├── index.html
├── style.css
├── script.js
└── README.md
```
