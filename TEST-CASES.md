# SILOG – Test Cases Checklist

> Tugas Final Struktur Data – SENDY FERRY SETYAWAN (NPM 218)

Gunakan file ini sebagai panduan manual testing. Centang satu per satu saat kamu mencoba di CLI.

---

## 1. Global & Input Umum

- [ ] Menu utama: input huruf (misal `a`, `!`) → muncul pesan pilihan tidak valid, program tidak crash.
- [ ] Menu utama: input angka di luar range (`9`, `-1`) → tetap dianggap tidak valid.
- [ ] Tekan Enter kosong di prompt menu utama dan sub-menu → tidak crash dan tetap meminta input.
- [ ] Semua prompt Y/N:
  - [ ] Input `Y` / `y` → dianggap Ya.
  - [ ] Input `N` / `n` → dianggap Tidak.
  - [ ] Input selain Y/N (`A`, `0`, kosong) → perilaku saat ini = dianggap Tidak (kembali), pastikan kamu terima perilaku ini.

---

## 2. Menu 1 – Kelola Jaringan Hub

### 2.1 Input Hub Kota Baru

- [ ] Input kota valid: `Sengkang`, `Jakarta`, `Yogyakarta` → sukses tersimpan.
- [ ] Input kota dengan angka: `J4karta` → ditolak.
- [ ] Input kota dengan simbol: `Bandung!`, `Surabaya-1` → ditolak.
- [ ] Input kota dengan spasi (kalau regex masih huruf saja): `KotaBaru` (tanpa spasi) diterima, `Kota Baru` ditolak → pastikan ini sesuai aturan kamu.
- [ ] Input nama kota yang sudah ada (misal `Sengkang` dua kali) → kedua kali muncul pesan sudah terdaftar.

### 2.2 Input Rute Antar-Kota

- [ ] Graph masih kurang dari 2 kota → pilih menu Input Rute → muncul pesan minimal 2 hub.
- [ ] Kota asal sama dengan kota tujuan (`Yogyakarta` – `Yogyakarta`) → ditolak.
- [ ] Kota asal ada, kota tujuan tidak ada di graph → pesan kota belum terdaftar.
- [ ] Kota tujuan ada, kota asal tidak ada di graph → pesan kota belum terdaftar.
- [ ] Jarak 0 → ditolak.
- [ ] Jarak negatif → ditolak.
- [ ] Jarak non-angka (`abc`) → tidak crash, minta input ulang.
- [ ] Tambah rute A–B, lalu cek rute B–A saat input resi → harus dianggap terhubung (jarak sama).
- [ ] Tambah rute yang sama dua kali (A–B lagi) → cek apakah jarak di-overwrite atau diberikan pesan (sesuai desain kamu).

---

## 3. Menu 2 – Administrasi Resi (BST)

### 3.1 Input Resi Pengiriman Baru

**No. Resi**

- [ ] Format benar: `2001`, `2999` → diterima.
- [ ] Kurang dari 4 digit: `201`, `200` → ditolak.
- [ ] Lebih dari 4 digit: `20001` → ditolak.
- [ ] Tidak diawali `2`: `1001`, `3001` → ditolak.
- [ ] Ada huruf: `20A1` → ditolak.
- [ ] Input No. Resi yang sudah pernah dipakai (duplikat) → harus ditolak.

**Nama Pengirim**

- [ ] Input nama wajar (misal `Budi`, `Andi Saputra`) → tersimpan benar.
- [ ] Tekan Enter kosong → lihat apakah kamu ingin nama kosong diizinkan (saat ini masih bisa kosong).

**Kota Asal & Tujuan**

- [ ] Tanpa inisialisasi graph (kalau kamu matikan data awal) → menu 2.1 menolak dengan pesan belum ada hub.
- [ ] Kota asal tidak ada di graph → pesan kota tidak terdaftar.
- [ ] Kota tujuan tidak ada di graph → pesan kota tidak terdaftar.
- [ ] Kota asal sama dengan kota tujuan → ditolak.
- [ ] Kota asal & tujuan ada, tapi **rute tidak tersedia** → pesan "Rute pengiriman belum tersedia dalam jaringan!" dan pertanyaan input resi lagi.

**Berat & Biaya**

- [ ] Berat = 0 → ditolak.
- [ ] Berat negatif → ditolak.
- [ ] Berat non-angka (`abc`) → tidak crash, minta ulang.
- [ ] Kasus cek manual biaya: jarak 100 KM, berat 2 Kg → total biaya harus `(100 × 2000) + (2 × 5000) = 210.000`.
- [ ] Coba beberapa kombinasi jarak & berat untuk memastikan rumus konsisten.

**Loop Input Resi**

- [ ] Setelah satu resi berhasil diinput, jawab `Y` → bisa lanjut input resi berikutnya.
- [ ] Setelah satu resi berhasil diinput, jawab `N` → kembali ke sub-menu 2.

### 3.2 Lihat Seluruh Data Resi (In-Order BST)

- [ ] Saat belum ada data resi → pesan "Belum ada data resi".
- [ ] Input beberapa resi dengan No. Resi acak (misal 2005, 2001, 2003, 2010) → output harus urut menaik: 2001, 2003, 2005, 2010.
- [ ] Cek bahwa data yang tampil (pengirim, asal, tujuan, berat, biaya) sesuai saat input.

### 3.3 Urutkan Transaksi Resi Berdasarkan Biaya Terbesar (Merge Sort)

- [ ] Saat belum ada resi → pesan "Belum ada data resi".
- [ ] Input beberapa resi dengan biaya berbeda → hasil harus urut **dari biaya terbesar ke terkecil**.
- [ ] Cek manual ranking untuk beberapa data (misal 5–6 resi) untuk memastikan Merge Sort bekerja benar.

---

## 4. Menu 3 – Kurir & Manifest Pengantaran (EC)

### 4.1 Input Data Kurir

- [ ] ID Kurir normal (misal `K001`) → tersimpan.
- [ ] ID Kurir kosong (Enter) → ditolak.
- [ ] ID Kurir duplikat (`K001` dua kali) → kedua kali ditolak.
- [ ] Nama Kurir normal (`Rudi`, `Santi`) → tersimpan.
- [ ] Nama Kurir kosong (Enter) → cek apakah kamu ingin mengizinkan (saat ini tidak divalidasi).
- [ ] Pilihan kendaraan:
  - [ ] Input `1` → Motor.
  - [ ] Input `2` → Mobil.
  - [ ] Input `3` → Truck.
  - [ ] Input selain 1/2/3 → tidak crash, minta ulang.
- [ ] Jawab `Y` di pertanyaan tambah kurir lagi → bisa input lagi.
- [ ] Jawab `N` → kembali ke menu 3.

### 4.2 Plotting Penugasan Manifest

- [ ] Tanpa kurir sama sekali → menu 3.2 menolak dengan pesan "Belum ada data kurir".
- [ ] Ada kurir tapi belum ada resi → pesan "Belum ada data resi terdaftar".
- [ ] Tampilkan daftar kurir → semua ID, nama, kendaraan muncul benar.
- [ ] Input ID kurir yang tidak ada → pesan "ID Kurir tidak ditemukan".
- [ ] Assign resi:
  - [ ] Assign resi yang valid → status berubah menjadi "Telah ditugaskan".
  - [ ] Assign resi yang sama untuk kedua kali (ke kurir lain) → ditolak, pesan sudah ditugaskan.
  - [ ] Input No. Resi yang tidak ada di BST → pesan tidak ditemukan.
  - [ ] Input No. Resi non-angka → tidak crash, minta ulang.
- [ ] Input `0` pada prompt No. Resi → selesai dari loop plotting dan kembali ke menu 3.

### 4.3 Tampil Manifest & Aturan Bonus Insentif

- [ ] Tanpa kurir → pesan "Belum ada data kurir".
- [ ] Kurir tanpa paket:
  - [ ] Lencana: Kurir Santai.
  - [ ] Bonus: Rp 0.
- [ ] Kurir dengan 1–3 paket:
  - [ ] Lencana: Kurir Reguler.
  - [ ] Bonus: Rp 25.000.
- [ ] Kurir dengan 4–6 paket:
  - [ ] Lencana: Kurir Produktif.
  - [ ] Bonus: Rp 60.000.
- [ ] Kurir dengan >6 paket:
  - [ ] Lencana: Kurir Elite.
  - [ ] Bonus: Rp 120.000.
- [ ] Detail setiap paket di manifest (No. Resi, Pengirim, Asal, Tujuan, Biaya) sesuai dengan data di BST.

---

## 5. Stress Test (Opsional)

- [ ] Input 20–50 resi dengan variasi rute & berat → traversal dan sorting tetap aman, tidak ada error.
- [ ] Input 10–20 kurir dan bagi resi ke banyak kurir → menu 3.3 masih terbaca dan tidak crash.

---

> Kalau semua checklist sudah tercentang dan hasilnya sesuai ekspektasi, berarti implementasi SILOG kamu sudah cukup kuat terhadap berbagai worst case input.
