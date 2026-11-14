# Latihan 3: Inheritance, super(), method overriding, multiple inheritance, MRO

class Kendaraan:
    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def deskripsi(self) -> str:
        return f"{self.merek} {self.model} ({self.tahun})"

    def tambah_jarak(self, km: float):
        if km > 0:
            self.odometer += km
            print(f"[{self.merek}] Menempuh perjalanan +{km} km. Total Odo: {self.odometer} km")
        else:
            print("Nilai kilometer tambahan tidak valid!")

    def klakson(self) -> str:
        return "Tin tin!"


class Mobil(Kendaraan):
    def __init__(self, merek: str, model: str, tahun: int, jumlah_pintu: int, kapasitas_tangki: float):
        super().__init__(merek, model, tahun)
        self.jumlah_pintu = jumlah_pintu
        self.kapasitas_tangki = kapasitas_tangki
        self.sisa_bensin = kapasitas_tangki

    def deskripsi(self) -> str:
        return f"{super().deskripsi()} [Mobil {self.jumlah_pintu} Pintu, Tangki: {self.kapasitas_tangki}L]"

    def klakson(self) -> str:
        return "Telolet! Telolet! (Klakson Mobil)"


class Motor(Kendaraan):
    def __init__(self, merek: str, model: str, tahun: int, kapasitas_cc: int):
        super().__init__(merek, model, tahun)
        self.kapasitas_cc = kapasitas_cc

    def deskripsi(self) -> str:
        return f"{super().deskripsi()} [Motor Sport {self.kapasitas_cc}cc]"

    def klakson(self) -> str:
        return "Bip bip! (Klakson Motor)"

    def wheelie(self):
        print(f"[{self.merek} {self.model}] Melakukan atraksi wheelie satu roda!")


class KomponenBaterai:
    def __init__(self, kapasitas_kwh: float):
        self.kapasitas_kwh = kapasitas_kwh
        self.daya_tersisa = 100.0

    def isi_daya(self, persen: float):
        self.daya_tersisa = min(100.0, self.daya_tersisa + persen)
        print(f"Baterai diisi ulang. Kapasitas daya: {self.daya_tersisa}%")


class MobilListrik(Mobil, KomponenBaterai):
    """Multiple inheritance: mewarisi Mobil dan KomponenBaterai."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_kwh: float):
        Mobil.__init__(self, merek, model, tahun, jumlah_pintu=4, kapasitas_tangki=0.0)
        KomponenBaterai.__init__(self, kapasitas_kwh)

    def deskripsi(self) -> str:
        return (f"{self.merek} {self.model} ({self.tahun}) "
                f"[EV Baterai {self.kapasitas_kwh} kWh, Daya: {self.daya_tersisa}%]")


if __name__ == "__main__":
    avanza = Mobil("Toyota", "Avanza Veloz", 2023, jumlah_pintu=5, kapasitas_tangki=45.0)
    cbr = Motor("Honda", "CBR250RR", 2022, kapasitas_cc=250)
    ioniq = MobilListrik("Hyundai", "Ioniq 5", 2024, kapasitas_kwh=72.6)

    print("--- Deskripsi Kendaraan ---")
    for kendaraan in (avanza, cbr, ioniq):
        print(kendaraan.deskripsi())

    print("\n--- Suara Klakson (Overriding) ---")
    print(f"{avanza.model} : {avanza.klakson()}")
    print(f"{cbr.model}    : {cbr.klakson()}")

    print("\n--- Perjalanan dan Energi ---")
    avanza.tambah_jarak(120.5)
    cbr.wheelie()
    ioniq.isi_daya(30)

    print("\n--- isinstance dan issubclass ---")
    print("avanza instance dari Mobil?     :", isinstance(avanza, Mobil))
    print("avanza instance dari Kendaraan? :", isinstance(avanza, Kendaraan))
    print("cbr instance dari Mobil?        :", isinstance(cbr, Mobil))
    print("Mobil subclass dari Kendaraan?  :", issubclass(Mobil, Kendaraan))
    print("\nMRO MobilListrik:", [c.__name__ for c in MobilListrik.__mro__])
