// ===== Konstanta & State =====
const KUNCI_STORAGE = "minipos_keranjang";
const MIN_DISKON = 50000;   // total belanja minimal untuk dapat diskon
const PERSEN_DISKON = 0.1;  // diskon 10%
const MIN_NAMA = 3;
const MIN_HARGA = 500;

let keranjang = muatKeranjang();

// ===== Elemen DOM =====
const form = document.getElementById("form-barang");
const inputNama = document.getElementById("nama");
const inputHarga = document.getElementById("harga");
const inputQty = document.getElementById("qty");
const tbody = document.getElementById("daftar-keranjang");
const inputBayar = document.getElementById("uang-bayar");

// ===== Utilitas =====
function formatRupiah(angka) {
  return "Rp " + Math.round(angka).toLocaleString("id-ID");
}

// ===== LocalStorage (serialisasi JSON) =====
function simpanKeranjang() {
  localStorage.setItem(KUNCI_STORAGE, JSON.stringify(keranjang));
}

function muatKeranjang() {
  try {
    const data = JSON.parse(localStorage.getItem(KUNCI_STORAGE));
    return Array.isArray(data) ? data : [];
  } catch (error) {
    return []; // data rusak -> mulai dari keranjang kosong
  }
}

// ===== Validasi form =====
function tampilkanError(input, pesan) {
  document.getElementById("error-" + input.id).textContent = pesan;
  input.classList.toggle("invalid", pesan !== "");
}

function validasiForm() {
  const nama = inputNama.value.trim();
  const hargaTeks = inputHarga.value.trim();
  const qtyTeks = inputQty.value.trim();
  const harga = Number(hargaTeks);
  const qty = Number(qtyTeks);
  let valid = true;

  if (nama.length < MIN_NAMA) {
    tampilkanError(inputNama, `Nama barang wajib diisi, minimal ${MIN_NAMA} karakter.`);
    valid = false;
  } else tampilkanError(inputNama, "");

  if (hargaTeks === "" || Number.isNaN(harga) || harga < MIN_HARGA) {
    tampilkanError(inputHarga, `Harga wajib berupa angka, minimal ${formatRupiah(MIN_HARGA)}.`);
    valid = false;
  } else tampilkanError(inputHarga, "");

  if (qtyTeks === "" || !Number.isInteger(qty) || qty < 1) {
    tampilkanError(inputQty, "Jumlah wajib berupa angka bulat, minimal 1.");
    valid = false;
  } else tampilkanError(inputQty, "");

  return valid ? { nama, harga, qty } : null;
}

// ===== Perhitungan =====
function hitungRingkasan() {
  const total = keranjang.reduce((jumlah, item) => jumlah + item.harga * item.qty, 0);
  const diskon = total >= MIN_DISKON ? Math.round(total * PERSEN_DISKON) : 0;
  return { total, diskon, akhir: total - diskon };
}

// ===== Render =====
function buatSel(teks, kelas) {
  const td = document.createElement("td");
  td.textContent = teks;
  if (kelas) td.className = kelas;
  return td;
}

function renderTabel() {
  tbody.innerHTML = "";
  if (keranjang.length === 0) {
    const tr = document.createElement("tr");
    const td = buatSel("Keranjang masih kosong. Tambahkan barang lewat form di atas.", "kosong");
    td.colSpan = 6;
    tr.appendChild(td);
    tbody.appendChild(tr);
    return;
  }
  keranjang.forEach((item, index) => {
    const tr = document.createElement("tr");
    tr.appendChild(buatSel(index + 1));
    tr.appendChild(buatSel(item.nama));
    tr.appendChild(buatSel(formatRupiah(item.harga), "angka"));
    tr.appendChild(buatSel(item.qty, "angka"));
    tr.appendChild(buatSel(formatRupiah(item.harga * item.qty), "angka"));

    const tdAksi = document.createElement("td");
    const tombol = document.createElement("button");
    tombol.type = "button";
    tombol.className = "btn btn-hapus";
    tombol.textContent = "Hapus";
    tombol.addEventListener("click", () => hapusItem(item.id));
    tdAksi.appendChild(tombol);
    tr.appendChild(tdAksi);
    tbody.appendChild(tr);
  });
}

function renderRingkasan() {
  const { total, diskon, akhir } = hitungRingkasan();
  document.getElementById("total-belanja").textContent = formatRupiah(total);
  document.getElementById("label-diskon").textContent = diskon > 0 ? "Diskon 10%" : "Diskon";
  document.getElementById("nominal-diskon").textContent = "- " + formatRupiah(diskon);
  document.getElementById("total-akhir").textContent = formatRupiah(akhir);

  const info = document.getElementById("info-diskon");
  if (total === 0) info.textContent = `Belanja minimal ${formatRupiah(MIN_DISKON)} dapat diskon 10%.`;
  else if (diskon === 0) info.textContent = `Tambah ${formatRupiah(MIN_DISKON - total)} lagi untuk dapat diskon 10%.`;
  else info.textContent = "Diskon 10% sudah diterapkan.";

  renderKembalian(akhir);
}

function renderKembalian(totalAkhir) {
  const hasil = document.getElementById("hasil-bayar");
  const teks = inputBayar.value.trim();
  hasil.className = "hasil-bayar";

  if (teks === "") { hasil.textContent = ""; return; }
  if (keranjang.length === 0) { hasil.textContent = "Keranjang masih kosong."; hasil.classList.add("kurang"); return; }

  const bayar = Number(teks);
  if (Number.isNaN(bayar) || bayar < 0) { hasil.textContent = "Uang bayar tidak valid."; hasil.classList.add("kurang"); return; }

  if (bayar < totalAkhir) {
    hasil.textContent = `Uang belum mencukupi, kurang ${formatRupiah(totalAkhir - bayar)}.`;
    hasil.classList.add("kurang");
  } else {
    hasil.textContent = `Kembalian: ${formatRupiah(bayar - totalAkhir)}`;
    hasil.classList.add("cukup");
  }
}

function render() {
  renderTabel();
  renderRingkasan();
}

// ===== Aksi =====
function tambahItem(barang) {
  keranjang.push({ id: Date.now() + Math.random(), ...barang });
  simpanKeranjang();
  render();
}

function hapusItem(id) {
  keranjang = keranjang.filter((item) => item.id !== id);
  simpanKeranjang();
  render();
}

function transaksiBaru() {
  keranjang = [];
  localStorage.removeItem(KUNCI_STORAGE);
  inputBayar.value = "";
  render();
}

// ===== Event listener =====
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const barang = validasiForm();
  if (!barang) return; // data tidak valid -> tidak masuk keranjang
  tambahItem(barang);
  form.reset();
  inputNama.focus();
});

inputBayar.addEventListener("input", () => renderKembalian(hitungRingkasan().akhir));
document.getElementById("btn-reset").addEventListener("click", transaksiBaru);

// ===== Mulai =====
render();
