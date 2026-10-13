// Kunci penyimpanan di localStorage
const STORAGE_KEY = "dashboard_tugas_mahasiswa";

// Mengubah karakter khusus agar aman dimasukkan ke HTML
const escapeHtml = (teks) =>
  String(teks)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

// Class untuk satu item tugas
class TaskItem {
  constructor({ id = Date.now(), judul, matkul, deadline, selesai = false }) {
    this.id = id;
    this.judul = judul;
    this.matkul = matkul;
    this.deadline = deadline;
    this.selesai = selesai;
  }

  // Tugas terlambat kalau belum selesai dan deadline sudah lewat
  get terlambat() {
    const hariIni = new Date().toISOString().slice(0, 10);
    return !this.selesai && this.deadline < hariIni;
  }
}

// Class utama untuk mengelola dashboard
class DashboardApp {
  constructor() {
    this.tasks = this.muatData();
    this.editId = null;
    this.filter = "semua";

    this.form = document.getElementById("form-tugas");
    this.inputJudul = document.getElementById("judul");
    this.inputMatkul = document.getElementById("matkul");
    this.inputDeadline = document.getElementById("deadline");
    this.pesanError = document.getElementById("pesan-error");
    this.btnSimpan = document.getElementById("btn-simpan");
    this.btnBatal = document.getElementById("btn-batal");
    this.daftar = document.getElementById("daftar-tugas");
    this.kosong = document.getElementById("kosong");
  }

  // ---------- localStorage ----------
  muatData() {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data).map((item) => new TaskItem(item)) : [];
  }

  simpanData() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(this.tasks));
  }

  // ---------- Operasi data (array tidak diubah langsung) ----------
  tambah({ judul, matkul, deadline }) {
    this.tasks = [...this.tasks, new TaskItem({ judul, matkul, deadline })];
  }

  ubah(id, perubahan) {
    this.tasks = this.tasks.map((t) =>
      t.id === id ? new TaskItem({ ...t, ...perubahan }) : t
    );
  }

  hapus(id) {
    this.tasks = this.tasks.filter((t) => t.id !== id);
  }

  // ---------- Tampilan ----------
  render() {
    const tampil = this.tasks
      .filter(({ selesai }) =>
        this.filter === "semua" ? true : this.filter === "selesai" ? selesai : !selesai
      )
      .sort((a, b) => a.deadline.localeCompare(b.deadline));

    this.daftar.innerHTML = tampil
      .map(
        (t) => `
        <li class="tugas ${t.selesai ? "selesai" : ""} ${t.terlambat ? "terlambat" : ""}">
          <div class="judul-tugas">${escapeHtml(t.judul)}</div>
          <div class="info-tugas">
            ${escapeHtml(t.matkul)} | Deadline: ${t.deadline}
            ${t.terlambat ? '<span class="label-terlambat">(Terlambat)</span>' : ""}
          </div>
          <button class="btn btn-kecil btn-selesai" data-aksi="selesai" data-id="${t.id}">
            ${t.selesai ? "Batalkan selesai" : "Tandai selesai"}
          </button>
          <button class="btn btn-kecil btn-edit" data-aksi="edit" data-id="${t.id}">Edit</button>
          <button class="btn btn-kecil btn-hapus" data-aksi="hapus" data-id="${t.id}">Hapus</button>
        </li>`
      )
      .join("");

    this.kosong.hidden = tampil.length > 0;

    const selesai = this.tasks.filter((t) => t.selesai).length;
    document.getElementById("stat-total").textContent = this.tasks.length;
    document.getElementById("stat-selesai").textContent = selesai;
    document.getElementById("stat-belum").textContent = this.tasks.length - selesai;
  }

  resetForm() {
    this.form.reset();
    this.editId = null;
    this.pesanError.textContent = "";
    this.btnSimpan.textContent = "Tambah tugas";
    this.btnBatal.hidden = true;
    document.getElementById("judul-form").textContent = "Tambah tugas";
  }

  // ---------- Event ----------
  handleSubmit(event) {
    event.preventDefault();
    const judul = this.inputJudul.value.trim();
    const matkul = this.inputMatkul.value.trim();
    const deadline = this.inputDeadline.value;

    let galat = "";
    if (judul.length < 3) {
      galat = "Judul tugas minimal 3 karakter.";
    } else if (matkul === "") {
      galat = "Mata kuliah wajib diisi.";
    } else if (deadline === "") {
      galat = "Deadline wajib dipilih.";
    }

    if (galat !== "") {
      this.pesanError.textContent = galat;
      return;
    }

    if (this.editId === null) {
      this.tambah({ judul, matkul, deadline });
    } else {
      this.ubah(this.editId, { judul, matkul, deadline });
    }

    this.simpanData();
    this.resetForm();
    this.render();
  }

  handleKlikDaftar(event) {
    const tombol = event.target.closest("button");
    if (!tombol) return;

    const id = Number(tombol.dataset.id);
    const { aksi } = tombol.dataset;
    const tugas = this.tasks.find((t) => t.id === id);

    if (aksi === "selesai") {
      this.ubah(id, { selesai: !tugas.selesai });
    } else if (aksi === "hapus") {
      if (!confirm(`Hapus tugas "${tugas.judul}"?`)) return;
      this.hapus(id);
    } else if (aksi === "edit") {
      this.editId = id;
      this.inputJudul.value = tugas.judul;
      this.inputMatkul.value = tugas.matkul;
      this.inputDeadline.value = tugas.deadline;
      this.btnSimpan.textContent = "Simpan perubahan";
      this.btnBatal.hidden = false;
      document.getElementById("judul-form").textContent = "Edit tugas";
      this.inputJudul.focus();
      return;
    }

    this.simpanData();
    this.render();
  }

  // ---------- Fetch API (async/await) ----------
  async muatCuaca() {
    const elemen = document.getElementById("cuaca");
    try {
      const url =
        "https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true";
      const respon = await fetch(url);
      if (!respon.ok) throw new Error("Gagal mengambil data cuaca");
      const { current_weather: cuaca } = await respon.json();
      elemen.textContent = `Suhu ${cuaca.temperature}°C, kecepatan angin ${cuaca.windspeed} km/jam.`;
    } catch (error) {
      elemen.textContent = "Cuaca tidak dapat dimuat (cek koneksi internet).";
    }
  }

  async muatKutipan() {
    const elemen = document.getElementById("kutipan");
    try {
      const respon = await fetch("https://dummyjson.com/quotes/random");
      if (!respon.ok) throw new Error("Gagal mengambil kutipan");
      const { quote, author } = await respon.json();
      elemen.textContent = `"${quote}" - ${author}`;
    } catch (error) {
      elemen.textContent = "Kutipan tidak dapat dimuat (cek koneksi internet).";
    }
  }

  // ---------- Mulai aplikasi ----------
  init() {
    document.getElementById("tanggal").textContent = new Date().toLocaleDateString("id-ID", {
      weekday: "long",
      day: "numeric",
      month: "long",
      year: "numeric",
    });

    this.form.addEventListener("submit", (e) => this.handleSubmit(e));
    this.btnBatal.addEventListener("click", () => this.resetForm());
    this.daftar.addEventListener("click", (e) => this.handleKlikDaftar(e));
    document.getElementById("filter").addEventListener("change", (e) => {
      this.filter = e.target.value;
      this.render();
    });

    this.render();
    this.muatCuaca();
    this.muatKutipan();
  }
}

const app = new DashboardApp();
app.init();
