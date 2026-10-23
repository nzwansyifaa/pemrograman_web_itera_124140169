# Aplikasi Manajemen Buku Pribadi

**Praktikum Pengembangan Aplikasi Web - Pertemuan 3 (React Basics)**

- Nama: Nazwa Nasyifaa Mega
- NIM: 124140169
- Kelas: PAW RA

## Deskripsi Aplikasi

Aplikasi web untuk mencatat buku pribadi: buku yang sudah dimiliki, sedang dibaca, atau ingin dibeli. Dibuat dengan React (Vite), React Router, dan Context API. Data tersimpan di `localStorage` sehingga tidak hilang saat halaman di-refresh.

### Fitur

- Menambah buku (judul, penulis, status: milik / sedang dibaca / ingin dibeli)
- Mengedit dan menghapus buku
- Filter buku berdasarkan status
- Pencarian berdasarkan judul atau nama penulis
- Halaman statistik jumlah buku per status
- Validasi form: kolom wajib diisi, kolom yang kosong diberi garis merah dan pesan error
- Data tersimpan di `localStorage`

## Instalasi dan Cara Menjalankan

Pastikan Node.js sudah terpasang, lalu buka folder project ini di VS Code dan jalankan di terminal:

```bash
npm install
npm run dev
```

Buka alamat yang muncul di terminal (biasanya `http://localhost:5173`).

### Menjalankan Unit Test

```bash
npm test
```

## Screenshot Aplikasi

![Halaman beranda](screenshots/Screenshot%202026-10-23%20193218.png)

![Edit buku dan validasi form](screenshots/Screenshot%202026-10-23%20193457.png)

![Halaman statistik](screenshots/Screenshot%202026-10-23%20193222.png)

## Laporan Testing

Hasil `npm test` di terminal (7 test, semuanya lulus):

![Hasil unit test](screenshots/Screenshot%202026-10-23%20194338.png)

| File Test | Yang diuji |
|---|---|
| `BookForm.test.jsx` | Pesan error saat form kosong; `onSubmit` dipanggil dengan data benar |
| `BookList.test.jsx` | Pesan saat daftar kosong; tombol Hapus memanggil `onDelete` |
| `BookFilter.test.jsx` | Kolom pencarian memanggil `onSearchChange` |
| `hooks.test.jsx` | `useBookStats` menghitung per status; `useLocalStorage` menyimpan data |

## Penjelasan Fitur React yang Digunakan

| Fitur React | Lokasi | Penjelasan |
|---|---|---|
| Functional component + Hooks | Semua komponen di `src/` | Seluruh komponen berupa function component |
| `useState` | `BookForm`, `Home`, `BookContext` | State form, buku yang diedit, filter, dan pencarian |
| `useEffect` | `Home.jsx`, `useLocalStorage.js` | Mengubah judul tab; menyimpan data ke localStorage |
| Komponen reusable (3) | `BookForm`, `BookList`, `BookFilter` | Dipakai oleh halaman Beranda lewat props |
| Props dan PropTypes | Semua komponen | Tipe props dicek memakai `prop-types` |
| Controlled components | `BookForm.jsx` | Input form dikontrol oleh state |
| Conditional rendering | `BookList`, `BookForm` | Pesan kosong, pesan error, dan mode tambah/edit |
| List dan key | `BookList.jsx` | Daftar buku dirender dengan `map` dan `key` |
| Context API | `context/BookContext.jsx` | Data buku dan fungsi CRUD dipakai bersama oleh semua halaman |
| React Router | `App.jsx`, `main.jsx` | Halaman Beranda (`/`) dan Statistik (`/statistik`) |
| Custom hook (2) | `useLocalStorage.js`, `useBookStats.js` | State persisten dan perhitungan statistik |

## Struktur Folder

```
nazwanasyifaamega_124140169_pertemuan3/
├── src/
│   ├── components/
│   │   ├── BookForm/BookForm.jsx
│   │   ├── BookList/BookList.jsx
│   │   └── BookFilter/BookFilter.jsx
│   ├── pages/
│   │   ├── Home/Home.jsx
│   │   └── Stats/Stats.jsx
│   ├── hooks/
│   │   ├── useLocalStorage.js
│   │   └── useBookStats.js
│   ├── context/BookContext.jsx
│   ├── tests/
│   ├── App.jsx
│   ├── main.jsx
│   ├── constants.js
│   └── index.css
├── screenshots/
├── vite.config.js
├── package.json
└── README.md
```
