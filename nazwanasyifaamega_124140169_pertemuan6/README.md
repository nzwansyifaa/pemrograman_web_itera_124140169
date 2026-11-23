# Aplikasi REST API Manajemen Mahasiswa dan Matakuliah

## Identitas

- Nama: Nazwa Nasyifaa Mega
- NIM: 124140169
- Kelas: RA

## Deskripsi

Aplikasi REST API menggunakan Pyramid, SQLAlchemy, Alembic, dan PostgreSQL untuk mengelola data mahasiswa dan matakuliah. API menyediakan operasi baca, tambah, ubah, dan hapus. Kode matakuliah dan NIM harus unik; SKS dan semester harus berupa bilangan bulat positif.

## Struktur Proyek

```text
pertemuan6/
├── development.ini
├── production.ini
├── setup.py
├── README.md
├── .gitignore
├── screenshots/
└── pyramid_mahasiswa/
    ├── __init__.py
    ├── routes.py
    ├── alembic/
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions/
    ├── models/
    ├── scripts/initialize_db.py
    ├── tests/
    └── views/
```

## Instalasi dan Konfigurasi

Persyaratan: Python 3.10 atau lebih baru dan PostgreSQL.

Buat user dan database PostgreSQL melalui `psql`:

```sql
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
CREATE DATABASE pyramid_mahasiswa OWNER pyramid_user;
```

URL koneksi lokal pada `development.ini`:

```ini
sqlalchemy.url = postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```

Buat virtual environment dan pasang dependensi dari PowerShell di folder proyek:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[testing]"
```

## Migrasi, Seeding, dan Server

Terapkan migrasi dan masukkan data contoh:

```powershell
alembic -c development.ini upgrade head
python -m pyramid_mahasiswa.scripts.initialize_db development.ini
```

Migrasi membuat tabel `mahasiswa` dan `matakuliah`. Seeding dapat dijalankan berulang tanpa menggandakan data contoh.

Jalankan server pengembangan:

```powershell
pserve development.ini --reload
```

Server berjalan di `http://localhost:6543`.

## Endpoint API

| Method | Endpoint | Fungsi |
| --- | --- | --- |
| GET | `/api/mahasiswa` | Daftar mahasiswa |
| GET | `/api/mahasiswa/{id}` | Detail mahasiswa |
| POST | `/api/mahasiswa` | Tambah mahasiswa |
| PUT | `/api/mahasiswa/{id}` | Ubah data mahasiswa |
| DELETE | `/api/mahasiswa/{id}` | Hapus mahasiswa |
| GET | `/api/matakuliah` | Daftar matakuliah |
| GET | `/api/matakuliah/{id}` | Detail matakuliah |
| POST | `/api/matakuliah` | Tambah matakuliah |
| PUT | `/api/matakuliah/{id}` | Ubah data matakuliah |
| DELETE | `/api/matakuliah/{id}` | Hapus matakuliah |

Semua endpoint menerima dan mengembalikan JSON. Kesalahan validasi menghasilkan HTTP 400, sedangkan data yang tidak ditemukan menghasilkan HTTP 404. Route dengan path sama dibedakan menggunakan predikat `request_method`.

## Pengujian Otomatis

Jalankan tes dengan:

```powershell
python -m pytest pyramid_mahasiswa/tests -q
```


## Bukti Pengujian API

![Respons daftar matakuliah](screenshots/matakuliah-list.png)
![Respons penambahan matakuliah](screenshots/matakuliah-create.png)
![Respons validasi SKS](screenshots/matakuliah-validasi-sks.png)
