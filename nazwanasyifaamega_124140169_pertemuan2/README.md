# Dashboard Tugas Mahasiswa

**Praktikum Pengembangan Aplikasi Web - Pertemuan 2 (JavaScript Next Gen ES6+)**

- Nama: Nazwa Nasyifaa Mega
- NIM: 124140169
- Kelas: PAW RA

## Deskripsi Aplikasi

Dashboard Tugas Mahasiswa adalah aplikasi web sederhana untuk mencatat tugas kuliah beserta mata kuliah dan deadline-nya. Aplikasi ini dibuat agar mahasiswa tidak lupa tugas yang harus dikumpulkan. Data tersimpan di `localStorage`, jadi tidak hilang saat halaman di-refresh.

### Fitur

- Menambah tugas (judul, mata kuliah, deadline) dengan validasi form
- Mengedit tugas yang sudah ada
- Menghapus tugas (dengan konfirmasi)
- Menandai tugas selesai atau belum selesai
- Filter tugas: semua, belum selesai, sudah selesai
- Tugas diurutkan berdasarkan deadline, dan tugas yang lewat deadline diberi tanda terlambat
- Statistik jumlah tugas (total, belum selesai, selesai)
- Widget cuaca kampus ITERA (API Open-Meteo)
- Kutipan harian (API DummyJSON)
- Data tersimpan di `localStorage`

## Screenshot

![Tampilan utama](screenshots/Screenshot%202026-10-13%20221321.png)

![Tambah tugas](screenshots/Screenshot%202026-10-13%20221351.png)

![Tugas selesai](screenshots/Screenshot%202026-10-13%20221356.png)

## Fitur ES6+ yang Diimplementasikan

File: `script.js`

| Fitur ES6+ | Baris | Keterangan |
|---|---|---|
| `let` dan `const` | `let`: 122, `const`: 2, 100, 118-120, 151-153 | `const` untuk nilai yang tidak berubah, `let` untuk `galat` (pesan error) yang nilainya diubah |
| Arrow function (lebih dari 3) | 5, 50, 64, 69, 75, 78, 82, 153, 212-215 | `escapeHtml`, `map`, `filter`, `find`, dan event listener |
| Template literals | 82-94, 158, 185, 197 | Render HTML tugas, pesan konfirmasi, teks cuaca dan kutipan |
| Async/await | 177-189, 191-201 | `muatCuaca()` dan `muatKutipan()` memakai `fetch` dengan `try/catch` |
| Class | 13 (`TaskItem`), 30 (`DashboardApp`) | `TaskItem` untuk data tugas, `DashboardApp` untuk state, localStorage, dan fetch |
| Getter di class | 21-24 | `terlambat` menghitung status tugas lewat deadline |
| Destructuring | 14, 58, 75, 152, 184, 196 | Pada parameter fungsi dan hasil `fetch` |
| Spread operator | 59, 64 | Memperbarui array dan objek tanpa mengubah data lama |
| Default parameter | 14 | `id = Date.now()` dan `selesai = false` |

## Cara Menjalankan

1. Buka folder `nazwanasyifaamega_124140169_pertemuan2` di VS Code.
2. Klik kanan `index.html`, pilih **Open with Live Server**.
3. Koneksi internet diperlukan agar widget cuaca dan kutipan dapat tampil. Fitur tugas tetap jalan tanpa internet.

## Struktur Folder

```
nazwanasyifaamega_124140169_pertemuan2/
├── screenshots/
├── index.html
├── style.css
├── script.js
└── README.md 
```
