# SILOG - Sistem Informasi Logistik

> **Tugas Final Struktur Data** | Semester Genap T.A. 2025/2026

Sistem berbasis CLI (Command Line Interface) untuk pengelolaan logistik pengiriman paket.

---

## 📋 Identitas Mahasiswa
| Field | Detail |
|-------|--------|
| **Nama** | SENDY FERRY SETYAWAN |
| **NPM** | 218 |
| **Digit NPM Terakhir** | 8 (GENAP) |

---

## 📦 Fitur Sistem

### Menu 1 — Kelola Jaringan Hub dan Rute Logistik
- **1.1** Input Hub Kota Baru — Graph tidak berarah berbobot (Adjacency List via Dictionary)
- **1.2** Input Rute Antar-Kota — bobot berupa jarak (KM), relasi timbal balik

### Menu 2 — Kelola Administrasi Resi Pengiriman
- **2.1** Input Resi Pengiriman Baru — disimpan ke Binary Search Tree (BST), key = No. Resi
- **2.2** Lihat Seluruh Data Resi — In-Order Traversal BST (urut No. Resi kecil → besar)
- **2.3) Urutkan Berdasarkan Biaya Terbesar — **Merge Sort** (NPM genap)

### Menu 3 — Kelola Kurir dan Manifest Pengantaran *(Extra Challenge)*
- **3.1** Input Data Kurir — disimpan dalam Array/List
- **3.2** Plotting Penugasan Manifest — Dictionary kurir → list resi (1 resi : 1 kurir)
- **3.3** Tampil Manifest & Bonus Insentif — Lencana otomatis berdasarkan jumlah paket

---

## ⚙️ Aturan Implementasi (NPM = 218, digit terakhir GENAP)
| Aturan | Nilai |
|--------|-------|
| Algoritma Sort (Menu 2.3) | **Merge Sort** |
| Format No. Resi (Menu 2.1) | Diawali angka `2` (contoh: `2001`) |
| Custom Hub Awal | Mengandung 3 huruf pertama nama depan `SEN` → **"Sengkang"** |

---

## 💰 Rumus Biaya Kirim
```
Total Biaya = (Jarak KM × Rp 2.000) + (Berat Kg × Rp 5.000)
```

---

## 🏅 Tabel Bonus Insentif Kurir
| Jumlah Paket | Lencana | Bonus |
|---|---|---|
| 0 | Kurir Santai | Rp 0 |
| 1 – 3 | Kurir Reguler | Rp 25.000 |
| 4 – 6 | Kurir Produktif | Rp 60.000 |
| > 6 | Kurir Elite | Rp 120.000 |

---

## 🚀 Cara Menjalankan
```bash
python silog.py
```

> Tidak memerlukan library eksternal, cukup Python 3.x standar.

---

## 📁 Struktur File
```
struktur-data/
└── silog.py       # Program utama SILOG
```
