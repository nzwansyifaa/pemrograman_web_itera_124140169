"""Program utama: menggunakan seluruh fungsi dari modul math_operations."""

# Cara impor 1: mengimpor seluruh modul (dipanggil dengan awalan math_operations.)
import math_operations

# Cara impor 2: mengimpor fungsi dan konstanta tertentu langsung
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin, PI


def cetak_judul(teks: str):
    """Mencetak judul bagian dengan garis pembatas.

    Parameter:
        teks (str): judul yang akan dicetak.
    """
    print(f"\n=== {teks} ===")


def uji_geometri():
    """Menguji fungsi luas dan keliling untuk persegi, persegi panjang, dan lingkaran."""
    cetak_judul("GEOMETRI")
    print(f"Konstanta PI = {PI}")

    print("\nPersegi:")
    for sisi in [4, 7.5, 10]:
        luas = math_operations.luas_persegi(sisi)
        keliling = math_operations.keliling_persegi(sisi)
        print(f"  Sisi {sisi:>5} -> Luas = {luas:>8.2f} | Keliling = {keliling:>7.2f}")

    print("\nPersegi panjang:")
    for panjang, lebar in [(5, 3), (10, 4), (8.5, 2.5)]:
        luas = math_operations.luas_persegi_panjang(panjang, lebar)
        keliling = math_operations.keliling_persegi_panjang(panjang, lebar)
        print(f"  {panjang:>4} x {lebar:<4} -> Luas = {luas:>8.2f} | Keliling = {keliling:>7.2f}")

    print("\nLingkaran:")
    for jari_jari in [3, 7, 10.5]:
        luas = math_operations.luas_lingkaran(jari_jari)
        keliling = math_operations.keliling_lingkaran(jari_jari)
        print(f"  r = {jari_jari:>5} -> Luas = {luas:>8.2f} | Keliling = {keliling:>7.2f}")


def uji_suhu():
    """Menguji fungsi konversi suhu Celsius ke Fahrenheit dan Kelvin."""
    cetak_judul("KONVERSI SUHU")
    print(f"{'Celsius':>9}{'Fahrenheit':>14}{'Kelvin':>10}")
    for celsius in [-40, 0, 25, 37, 100]:
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>9.1f}{fahrenheit:>14.2f}{kelvin:>10.2f}")


def main():
    """Menjalankan seluruh pengujian modul."""
    uji_geometri()
    uji_suhu()


if __name__ == "__main__":
    main()
