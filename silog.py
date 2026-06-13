# ============================================================
# SILOG - Sistem Informasi Logistik
# Nama  : SENDY FERRY SETYAWAN
# NPM   : 218 (digit terakhir GENAP)
# Aturan: Merge Sort, No. Resi awali '2', Hub mengandung 'SEN'
# ============================================================

import re

# ===================== STRUKTUR DATA ========================

# --- Graph (Weighted Undirected Graph via Adjacency List) ---
graph = {}  # { "Kota": {"KotaLain": jarak, ...}, ... }

# --- BST Node ---
class NodeBST:
    def __init__(self, no_resi, nama_pengirim, kota_asal, kota_tujuan, berat, biaya):
        self.no_resi       = no_resi
        self.nama_pengirim = nama_pengirim
        self.kota_asal     = kota_asal
        self.kota_tujuan   = kota_tujuan
        self.berat         = berat
        self.biaya         = biaya
        self.kiri          = None
        self.kanan         = None

bst_root = None  # root BST

# --- Array Kurir ---
daftar_kurir   = []   # list of dict
manifest       = {}   # { id_kurir: [no_resi, ...] }
resi_terpasang = set()  # no resi yg sudah dialokasikan ke kurir

# ===================== HELPER ================================

def cetak_garis(char="=", panjang=60):
    print(char * panjang)

def input_huruf_saja(prompt):
    """Input nama kota: hanya huruf, tidak boleh angka, spasi, atau simbol."""
    while True:
        nilai = input(prompt).strip()
        if re.fullmatch(r'[A-Za-z]+', nilai):
            return nilai.title()
        print("  [!] Input tidak valid. Nama kota hanya boleh berisi huruf.")

def input_int_positif(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("  [!] Harus angka positif.")
        except ValueError:
            print("  [!] Masukkan angka bulat.")

def input_float_positif(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("  [!] Harus angka positif.")
        except ValueError:
            print("  [!] Masukkan angka.")

# ===================== GRAPH =================================

def tambah_hub(nama_kota):
    if nama_kota in graph:
        print(f'  [!] Kota "{nama_kota}" sudah terdaftar.')
    else:
        graph[nama_kota] = {}
        print(f'  [+] Hub "{nama_kota}" berhasil ditambahkan.')

def tambah_rute(kota_a, kota_b, jarak):
    if kota_a not in graph or kota_b not in graph:
        print("  [!] Salah satu atau kedua kota belum terdaftar sebagai hub.")
        return
    if kota_a == kota_b:
        print("  [!] Kota asal dan tujuan tidak boleh sama.")
        return
    graph[kota_a][kota_b] = jarak
    graph[kota_b][kota_a] = jarak
    print(f"  [+] Rute {kota_a} <-> {kota_b} ({jarak} KM) berhasil ditambahkan.")

def cek_rute(kota_a, kota_b):
    """Kembalikan jarak jika ada rute langsung, else None."""
    if kota_a in graph and kota_b in graph[kota_a]:
        return graph[kota_a][kota_b]
    return None

# ===================== BST ===================================

def bst_insert(root, node):
    if root is None:
        return node
    if node.no_resi < root.no_resi:
        root.kiri = bst_insert(root.kiri, node)
    elif node.no_resi > root.no_resi:
        root.kanan = bst_insert(root.kanan, node)
    else:
        print("  [!] No. Resi sudah terdaftar dalam sistem.")
    return root

def bst_inorder(root, hasil):
    if root:
        bst_inorder(root.kiri, hasil)
        hasil.append(root)
        bst_inorder(root.kanan, hasil)

def bst_cari(root, no_resi):
    if root is None:
        return None
    if no_resi == root.no_resi:
        return root
    elif no_resi < root.no_resi:
        return bst_cari(root.kiri, no_resi)
    else:
        return bst_cari(root.kanan, no_resi)

# ===================== SORTING ================================

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    kiri  = merge_sort(arr[:mid])
    kanan = merge_sort(arr[mid:])
    return merge(kiri, kanan)

def merge(kiri, kanan):
    hasil = []
    i = j = 0
    while i < len(kiri) and j < len(kanan):
        # sort descending by biaya
        if kiri[i].biaya >= kanan[j].biaya:
            hasil.append(kiri[i]); i += 1
        else:
            hasil.append(kanan[j]); j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil

def format_rupiah(n):
    return f"Rp {n:,.0f}".replace(",", ".")

# ===================== MENU 1 ================================

def menu_kelola_hub():
    while True:
        cetak_garis()
        print("  MENU 1 - Kelola Jaringan Hub dan Rute Logistik")
        cetak_garis()
        print("  1.1) Input Hub Kota Baru")
        print("  1.2) Input Rute Antar-Kota")
        print("  0)   Kembali ke Menu Utama")
        cetak_garis("-")
        pilihan = input("  Pilih menu: ").strip()
        if pilihan in ("1", "1.1"):
            menu_input_hub()
        elif pilihan in ("2", "1.2"):
            menu_input_rute()
        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")

def menu_input_hub():
    cetak_garis("-")
    print("  [INPUT HUB KOTA BARU]")
    nama = input_huruf_saja("  Nama Kota Hub: ")
    tambah_hub(nama)

def menu_input_rute():
    cetak_garis("-")
    print("  [INPUT RUTE ANTAR-KOTA]")
    if len(graph) < 2:
        print("  [!] Minimal 2 kota hub harus terdaftar terlebih dahulu.")
        return
    print("  Daftar Hub Terdaftar:", ", ".join(graph.keys()))
    kota_a = input_huruf_saja("  Kota Asal : ")
    kota_b = input_huruf_saja("  Kota Tujuan: ")
    jarak  = input_int_positif("  Jarak (KM): ")
    tambah_rute(kota_a, kota_b, jarak)

# ===================== MENU 2 ================================

def menu_kelola_resi():
    while True:
        cetak_garis()
        print("  MENU 2 - Kelola Administrasi Resi Pengiriman")
        cetak_garis()
        print("  2.1) Input Resi Pengiriman Baru")
        print("  2.2) Lihat Seluruh Data Resi Terdaftar")
        print("  2.3) Urutkan Transaksi Resi Berdasarkan Biaya Terbesar")
        print("  0)   Kembali ke Menu Utama")
        cetak_garis("-")
        pilihan = input("  Pilih menu: ").strip()
        if pilihan in ("1", "2.1"):
            menu_input_resi()
        elif pilihan in ("2", "2.2"):
            menu_lihat_resi()
        elif pilihan in ("3", "2.3"):
            menu_urut_resi()
        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")

def menu_input_resi():
    global bst_root
    while True:
        cetak_garis("-")
        print("  [INPUT RESI PENGIRIMAN BARU]")
        print("  Catatan: No. Resi harus 4 digit diawali angka '2' (contoh: 2001)")

        # No. Resi
        while True:
            no_resi_str = input("  No. Resi (4 digit, awali '2'): ").strip()
            if re.fullmatch(r'2\d{3}', no_resi_str):
                no_resi = int(no_resi_str)
                if bst_cari(bst_root, no_resi):
                    print("  [!] No. Resi sudah terdaftar. Gunakan nomor lain.")
                else:
                    break
            else:
                print("  [!] No. Resi harus 4 digit dan diawali angka '2'.")

        nama_pengirim = input("  Nama Pengirim: ").strip()

        # Kota Asal
        if not graph:
            print("  [!] Belum ada kota hub terdaftar. Tambahkan dulu di Menu 1.")
            return
        print("  Hub Terdaftar:", ", ".join(graph.keys()))
        while True:
            kota_asal = input_huruf_saja("  Kota Asal   : ")
            if kota_asal not in graph:
                print(f'  [!] Kota "{kota_asal}" tidak terdaftar sebagai hub.')
            else:
                break

        while True:
            kota_tujuan = input_huruf_saja("  Kota Tujuan : ")
            if kota_tujuan not in graph:
                print(f'  [!] Kota "{kota_tujuan}" tidak terdaftar sebagai hub.')
            elif kota_tujuan == kota_asal:
                print("  [!] Kota tujuan tidak boleh sama dengan kota asal.")
            else:
                break

        jarak = cek_rute(kota_asal, kota_tujuan)
        if jarak is None:
            print("  [!] Rute pengiriman belum tersedia dalam jaringan!")
            lagi = input("  Apakah ingin melakukan input resi lagi (Y/N)? ").strip().upper()
            if lagi != "Y":
                break
            continue

        berat = input_float_positif("  Berat Paket (Kg): ")
        biaya = (jarak * 2000) + (berat * 5000)

        node = NodeBST(no_resi, nama_pengirim, kota_asal, kota_tujuan, berat, biaya)
        bst_root = bst_insert(bst_root, node)

        cetak_garis("-")
        print("  [+] Input Resi Berhasil!")
        print(f"      No. Resi     : {no_resi}")
        print(f"      Pengirim     : {nama_pengirim}")
        print(f"      Rute         : {kota_asal} -> {kota_tujuan} ({jarak} KM)")
        print(f"      Berat        : {berat} Kg")
        print(f"      Total Biaya  : {format_rupiah(biaya)}")
        cetak_garis("-")

        lagi = input("  Apakah ingin melakukan input resi lagi (Y/N)? ").strip().upper()
        if lagi != "Y":
            break

def menu_lihat_resi():
    cetak_garis("-")
    print("  [SELURUH DATA RESI TERDAFTAR - In-Order Traversal BST]")
    cetak_garis("-")
    hasil = []
    bst_inorder(bst_root, hasil)
    if not hasil:
        print("  Belum ada data resi.")
    else:
        print(f"  {'No.Resi':<10}{'Pengirim':<20}{'Asal':<15}{'Tujuan':<15}{'Berat':>8}  {'Biaya':>15}")
        cetak_garis("-")
        for r in hasil:
            print(f"  {r.no_resi:<10}{r.nama_pengirim:<20}{r.kota_asal:<15}{r.kota_tujuan:<15}{r.berat:>7.1f}Kg  {format_rupiah(r.biaya):>15}")
    cetak_garis("-")

def menu_urut_resi():
    cetak_garis("-")
    print("  [URUTKAN RESI BERDASARKAN BIAYA TERBESAR - Merge Sort]")
    cetak_garis("-")
    daftar = []
    bst_inorder(bst_root, daftar)
    if not daftar:
        print("  Belum ada data resi.")
        return
    terurut = merge_sort(daftar)
    print(f"  {'Rank':<6}{'No.Resi':<10}{'Pengirim':<20}{'Asal':<15}{'Tujuan':<15}{'Biaya':>15}")
    cetak_garis("-")
    for i, r in enumerate(terurut, 1):
        print(f"  {i:<6}{r.no_resi:<10}{r.nama_pengirim:<20}{r.kota_asal:<15}{r.kota_tujuan:<15}{format_rupiah(r.biaya):>15}")
    cetak_garis("-")

# ===================== MENU 3 (EC) ===========================

def menu_kelola_kurir():
    while True:
        cetak_garis()
        print("  MENU 3 - Kelola Kurir dan Manifest Pengantaran")
        cetak_garis()
        print("  3.1) Input Data Kurir")
        print("  3.2) Plotting Penugasan Manifest")
        print("  3.3) Tampil Manifest & Aturan Bonus Insentif")
        print("  0)   Kembali ke Menu Utama")
        cetak_garis("-")
        pilihan = input("  Pilih menu: ").strip()
        if pilihan in ("1", "3.1"):
            menu_input_kurir()
        elif pilihan in ("2", "3.2"):
            menu_plotting_manifest()
        elif pilihan in ("3", "3.3"):
            menu_tampil_manifest()
        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")

def menu_input_kurir():
    while True:
        cetak_garis("-")
        print("  [INPUT DATA KURIR]")

        while True:
            id_kurir = input("  ID Kurir: ").strip()
            if not id_kurir:
                print("  [!] ID Kurir tidak boleh kosong.")
                continue
            if any(k['id'] == id_kurir for k in daftar_kurir):
                print("  [!] ID Kurir sudah terdaftar.")
            else:
                break

        nama_kurir = input("  Nama Kurir: ").strip()
        while True:
            print("  Jenis Kendaraan: 1) Motor  2) Mobil  3) Truck")
            jenis_input = input("  Pilih (1/2/3): ").strip()
            jenis_map = {"1": "Motor", "2": "Mobil", "3": "Truck"}
            if jenis_input in jenis_map:
                jenis = jenis_map[jenis_input]
                break
            print("  [!] Pilihan tidak valid.")

        daftar_kurir.append({"id": id_kurir, "nama": nama_kurir, "kendaraan": jenis})
        if id_kurir not in manifest:
            manifest[id_kurir] = []
        print("  [+] Data Kurir Berhasil Diinputkan.")

        lagi = input("  Apakah ingin menambahkan data Kurir lagi (Y/N)? ").strip().upper()
        if lagi != "Y":
            break

def menu_plotting_manifest():
    cetak_garis("-")
    print("  [PLOTTING PENUGASAN MANIFEST]")
    if not daftar_kurir:
        print("  [!] Belum ada data kurir. Tambahkan kurir terlebih dahulu.")
        return

    print(f"  {'ID':<12}{'Nama':<20}{'Kendaraan'}")
    cetak_garis("-")
    for k in daftar_kurir:
        print(f"  {k['id']:<12}{k['nama']:<20}{k['kendaraan']}")
    cetak_garis("-")

    id_pilih = input("  Masukkan ID Kurir yang ditugaskan: ").strip()
    kurir_obj = next((k for k in daftar_kurir if k['id'] == id_pilih), None)
    if not kurir_obj:
        print("  [!] ID Kurir tidak ditemukan.")
        return

    print(f"  Kurir terpilih: {kurir_obj['nama']} ({kurir_obj['kendaraan']})")

    semua_resi = []
    bst_inorder(bst_root, semua_resi)
    if not semua_resi:
        print("  [!] Belum ada data resi terdaftar.")
        return

    while True:
        print()
        print(f"  {'No.Resi':<10}{'Pengirim':<20}{'Asal':<15}{'Tujuan':<15}{'Status':>18}")
        cetak_garis("-")
        for r in semua_resi:
            status = "Telah ditugaskan" if r.no_resi in resi_terpasang else "Tersedia"
            print(f"  {r.no_resi:<10}{r.nama_pengirim:<20}{r.kota_asal:<15}{r.kota_tujuan:<15}{status:>18}")
        cetak_garis("-")

        no_resi_str = input("  Masukkan No. Resi (atau 0 untuk selesai): ").strip()
        if no_resi_str == "0":
            break
        try:
            no_resi_int = int(no_resi_str)
        except ValueError:
            print("  [!] Input tidak valid.")
            continue

        node_resi = bst_cari(bst_root, no_resi_int)
        if not node_resi:
            print("  [!] No. Resi tidak ditemukan dalam sistem.")
            continue
        if no_resi_int in resi_terpasang:
            print("  [!] Resi ini sudah ditugaskan ke kurir lain.")
            continue

        manifest[id_pilih].append(no_resi_int)
        resi_terpasang.add(no_resi_int)
        print(f"  [+] Resi {no_resi_int} berhasil ditugaskan ke kurir {kurir_obj['nama']}.")

def menu_tampil_manifest():
    cetak_garis("-")
    print("  [MANIFEST & ATURAN BONUS INSENTIF]")
    cetak_garis("-")
    if not daftar_kurir:
        print("  Belum ada data kurir.")
        return
    for kurir in daftar_kurir:
        kid       = kurir['id']
        resi_list = manifest.get(kid, [])
        jumlah    = len(resi_list)

        if jumlah == 0:
            lencana, bonus = "Kurir Santai",    0
        elif jumlah <= 3:
            lencana, bonus = "Kurir Reguler",   25000
        elif jumlah <= 6:
            lencana, bonus = "Kurir Produktif", 60000
        else:
            lencana, bonus = "Kurir Elite",     120000

        cetak_garis("-")
        print(f"  ID Kurir    : {kurir['id']}")
        print(f"  Nama Kurir  : {kurir['nama']}")
        print(f"  Kendaraan   : {kurir['kendaraan']}")
        print(f"  Lencana     : {lencana}")
        print(f"  Bonus       : {format_rupiah(bonus)}")
        print(f"  Jumlah Paket: {jumlah}")

        if resi_list:
            print()
            print(f"  {'No.Resi':<10}{'Pengirim':<20}{'Asal':<15}{'Tujuan':<15}{'Biaya':>15}")
            cetak_garis("-")
            for no in resi_list:
                r = bst_cari(bst_root, no)
                if r:
                    print(f"  {r.no_resi:<10}{r.nama_pengirim:<20}{r.kota_asal:<15}{r.kota_tujuan:<15}{format_rupiah(r.biaya):>15}")
        else:
            print("  (Belum ada paket)")
    cetak_garis()

# ===================== INISIALISASI DATA AWAL ================

def inisialisasi_data_awal():
    """
    Aturan: Salah satu kota hub wajib mengandung 3 huruf pertama
    dari nama depan mahasiswa = SEN -> "Sengkang"
    """
    kota_default = ["Sengkang", "Makassar", "Yogyakarta", "Jakarta", "Bandung", "Surabaya"]
    rute_default = [
        ("Sengkang",   "Makassar",   200),
        ("Yogyakarta",  "Jakarta",   560),
        ("Yogyakarta",  "Bandung",   290),
        ("Yogyakarta",  "Surabaya",  320),
        ("Jakarta",     "Bandung",   150),
        ("Jakarta",     "Surabaya",  800),
        ("Bandung",     "Surabaya",  740),
    ]
    for kota in kota_default:
        if kota not in graph:
            graph[kota] = {}
    for a, b, j in rute_default:
        if b not in graph[a]:
            graph[a][b] = j
            graph[b][a] = j

# ===================== MAIN LOOP =============================

def main():
    inisialisasi_data_awal()

    while True:
        cetak_garis()
        print("  ===  MENU UTAMA SILOG  ===")
        cetak_garis()
        print("  1) Kelola Jaringan Hub dan Rute Logistik")
        print("  2) Kelola Administrasi Resi Pengiriman")
        print("  3) Kelola Kurir dan Manifest Pengantaran [EC]")
        print("  0) Exit Program")
        cetak_garis("-")
        pilihan = input("  Pilih menu: ").strip()

        if pilihan == "1":
            menu_kelola_hub()
        elif pilihan == "2":
            menu_kelola_resi()
        elif pilihan == "3":
            menu_kelola_kurir()
        elif pilihan == "0":
            print("  Terima kasih. Program SILOG dihentikan.")
            cetak_garis()
            break
        else:
            print("  [!] Pilihan tidak valid. Silakan pilih 0-3.")

if __name__ == "__main__":
    main()
