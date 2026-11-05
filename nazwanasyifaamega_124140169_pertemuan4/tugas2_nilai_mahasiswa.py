"""Tugas 2: Program pengelolaan data nilai mahasiswa."""

# Data contoh: list yang berisi dictionary data mahasiswa
data_mahasiswa = [
    {"nama": "Yoon Keeho", "nim": "124140301", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
    {"nama": "Yoon Yechan", "nim": "124140302", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 80},
    {"nama": "Zhao Yufan", "nim": "124140303", "nilai_uts": 65, "nilai_uas": 60, "nilai_tugas": 70},
    {"nama": "Choi Seunghyun", "nim": "124140304", "nilai_uts": 55, "nilai_uas": 50, "nilai_tugas": 60},
    {"nama": "Lee Seunghyun", "nim": "124140305", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
    {"nama": "Hwang Hyunjin", "nim": "124140306", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 92},
]


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir dengan bobot UTS 30%, UAS 40%, Tugas 30%.

    Parameter:
        uts (float): nilai UTS.
        uas (float): nilai UAS.
        tugas (float): nilai tugas.

    Mengembalikan:
        float: nilai akhir.
    """
    return (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade (A-E) berdasarkan nilai akhir.

    Parameter:
        nilai_akhir (float): nilai akhir mahasiswa.

    Mengembalikan:
        str: grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def proses_nilai(daftar: list) -> list:
    """Menambahkan nilai akhir dan grade ke setiap data mahasiswa.

    Parameter:
        daftar (list): list dictionary data mahasiswa.

    Mengembalikan:
        list: list dictionary baru yang sudah memuat nilai_akhir dan grade.
    """
    hasil = []
    for mhs in daftar:
        nilai_akhir = hitung_nilai_akhir(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        hasil.append({**mhs, "nilai_akhir": nilai_akhir, "grade": tentukan_grade(nilai_akhir)})
    return hasil


def cetak_tabel(daftar: list):
    """Mencetak data mahasiswa dalam format tabel yang rapi.

    Parameter:
        daftar (list): list dictionary yang sudah memuat nilai_akhir dan grade.
    """
    header = f"{'No':<4}{'Nama':<20}{'NIM':<12}{'Nilai Akhir':>12}{'Grade':>8}"
    garis = "-" * len(header)

    print(garis)
    print(header)
    print(garis)
    for nomor, mhs in enumerate(daftar, start=1):
        print(
            f"{nomor:<4}{mhs['nama']:<20}{mhs['nim']:<12}"
            f"{mhs['nilai_akhir']:>12.2f}{mhs['grade']:>8}"
        )
    print(garis)


def cetak_info(judul: str, mhs: dict):
    """Mencetak informasi satu mahasiswa.

    Parameter:
        judul (str): judul yang ditampilkan.
        mhs (dict): data mahasiswa yang akan dicetak.
    """
    print(f"{judul}")
    print(f"  Nama        : {mhs['nama']}")
    print(f"  NIM         : {mhs['nim']}")
    print(f"  Nilai Akhir : {mhs['nilai_akhir']:.2f}")
    print(f"  Grade       : {mhs['grade']}")


def main():
    """Menjalankan program: hitung nilai, cetak tabel, cari nilai tertinggi dan terendah."""
    hasil = proses_nilai(data_mahasiswa)

    print("=== DATA NILAI MAHASISWA ===")
    cetak_tabel(hasil)

    tertinggi = max(hasil, key=lambda m: m["nilai_akhir"])
    terendah = min(hasil, key=lambda m: m["nilai_akhir"])

    print()
    cetak_info("Mahasiswa dengan nilai akhir TERTINGGI:", tertinggi)
    print()
    cetak_info("Mahasiswa dengan nilai akhir TERENDAH:", terendah)


if __name__ == "__main__":
    main()
