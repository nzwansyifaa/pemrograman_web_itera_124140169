"""Tugas 1: Program penghitung BMI (Body Mass Index) sederhana."""


def hitung_bmi(berat: float, tinggi: float) -> float:
    """Menghitung nilai BMI.

    Parameter:
        berat (float): berat badan dalam kilogram (kg).
        tinggi (float): tinggi badan dalam meter (m).

    Mengembalikan:
        float: nilai BMI, yaitu berat / (tinggi * tinggi).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori(bmi: float) -> str:
    """Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameter:
        bmi (float): nilai BMI yang sudah dihitung.

    Mengembalikan:
        str: kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def baca_angka_positif(pesan: str, batas_atas: float = None) -> float:
    """Meminta input angka dari pengguna sampai nilainya valid.

    Parameter:
        pesan (str): teks yang ditampilkan saat meminta input.
        batas_atas (float): batas maksimum nilai (opsional).

    Mengembalikan:
        float: angka positif yang valid.
    """
    while True:
        teks = input(pesan)
        try:
            nilai = float(teks.replace(",", "."))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue

        if nilai <= 0:
            print("Nilai harus lebih besar dari 0. Silakan coba lagi.")
        elif batas_atas is not None and nilai > batas_atas:
            print(f"Nilai terlalu besar (maksimal {batas_atas}). Silakan coba lagi.")
        else:
            return nilai


def main():
    """Menjalankan program: input data, hitung BMI, lalu cetak hasilnya."""
    print("=== PENGHITUNG BMI ===")
    berat = baca_angka_positif("Masukkan berat badan (kg)  : ")
    tinggi = baca_angka_positif("Masukkan tinggi badan (m)  : ", batas_atas=3.0)

    bmi = hitung_bmi(berat, tinggi)
    kategori = tentukan_kategori(bmi)

    print("\n--- HASIL ---")
    print(f"Nilai BMI : {bmi:.2f}")
    print(f"Kategori  : {kategori}")


if __name__ == "__main__":
    main()
