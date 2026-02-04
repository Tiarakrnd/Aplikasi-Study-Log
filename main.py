from datetime import datetime
import json
import os

# Nama file untuk menyimpan data
FILE_CATATAN = "catatan_belajar.json"

# List untuk menyimpan semua catatan belajar
catatan = []

def muat_catatan():
    """Memuat catatan dari file JSON"""
    global catatan
    if os.path.exists(FILE_CATATAN):
        try:
            with open(FILE_CATATAN, "r") as f:
                catatan = json.load(f)
        except:
            catatan = []

def simpan_catatan():
    """Menyimpan catatan ke file JSON"""
    with open(FILE_CATATAN, "w") as f:
        json.dump(catatan, f, indent=4)

def tambah_catatan():
    """Fungsi untuk menambah catatan belajar baru"""
    print("\n--- Tambah Catatan Belajar ---")
    
    mapel = input("Masukkan nama mapel: ").strip()
    topik = input("Masukkan topik yang dipelajari: ").strip()
    
    # Validasi durasi harus angka positif
    while True:
        try:
            durasi = int(input("Masukkan durasi belajar (menit): "))
            if durasi > 0:
                break
            else:
                print("Durasi harus lebih dari 0 menit!")
        except ValueError:
            print("Masukkan angka yang valid!")
    
    # Menyimpan data ke dalam list catatan
    # Struktur: dictionary yang mudah dipahami pemula
    now = datetime.now()
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
        "tanggal": now.strftime("%d/%m/%Y"),
        "jam": now.strftime("%H:%M")
    }
    
    catatan.append(catatan_baru)
    
    # Simpan catatan ke file
    simpan_catatan()
    
    # Tabel berwarna merah maroon dengan emoticon ✨
    MAROON = "\033[38;5;131m"
    RESET = "\033[0m"
    
    print()
    print(f"{MAROON}╔═══════════════════════════════════════════════════════╗{RESET}")
    print(f"{MAROON}║                                                       ║{RESET}")
    print(f"{MAROON}║       ✨ CATATAN BERHASIL DITAMBAHKAN! ✨            ║{RESET}")
    print(f"{MAROON}║                                                       ║{RESET}")
    print(f"{MAROON}╠═══════════════════════════════════════════════════════╣{RESET}")
    print(f"{MAROON}║  📚 Mapel    : {mapel:<38}║{RESET}")
    print(f"{MAROON}║  📖 Topik    : {topik:<38}║{RESET}")
    print(f"{MAROON}║  ⏱️  Durasi   : {durasi} menit{' ':<28}║{RESET}")
    print(f"{MAROON}║  📅 Tanggal  : {catatan_baru['tanggal']:<38}║{RESET}")
    print(f"{MAROON}║                                                       ║{RESET}")
    print(f"{MAROON}╚═══════════════════════════════════════════════════════╝{RESET}")
    print()


def lihat_catatan():
    """Fungsi untuk menampilkan semua catatan belajar"""
    PINK = "\033[38;5;205m"
    RESET = "\033[0m"
    
    # Jika belum ada data, tampilkan pesan yang sesuai
    if len(catatan) == 0:
        print()
        print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║      ❌ BELUM ADA CATATAN BELAJAR! ❌                ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║   📚 Mulai belajar sekarang dan catat progresmu!      ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
        print()
        return
    
    # Menampilkan header tabel
    print()
    print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}║          👀 DAFTAR CATATAN BELAJARMU 👀              ║{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╠═══════════════════════════════════════════════════════╣{RESET}")
    
    # Menampilkan semua catatan dengan rapi
    for i, item in enumerate(catatan, 1):
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║  #{i} 📚 Mapel: {item['mapel']:<39}║{RESET}")
        print(f"{PINK}║     📖 Topik : {item['topik']:<39}║{RESET}")
        print(f"{PINK}║     ⏱️  Durasi: {item['durasi']} menit{' ':<33}║{RESET}")
        print(f"{PINK}║     📅 Tanggal: {item['tanggal']:<38}║{RESET}")
    
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
    print()


def total_waktu():
    """Fungsi untuk menghitung total durasi belajar"""
    PINK = "\033[38;5;205m"
    RESET = "\033[0m"
    
    if len(catatan) == 0:
        print()
        print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║      ❌ BELUM ADA CATATAN BELAJAR! ❌                ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║      ⏱️  Mulai belajar untuk melihat waktu total!    ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
        print()
        return
    
    # Menghitung total durasi dari semua catatan
    total_menit = sum(item["durasi"] for item in catatan)
    
    # Konversi ke jam dan menit
    jam = total_menit // 60
    menit = total_menit % 60
    
    print()
    print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}║         ⏰ TOTAL WAKTU BELAJARMU ⏰                  ║{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╠═══════════════════════════════════════════════════════╣{RESET}")
    print(f"{PINK}║  📊 Total Menit    : {total_menit} menit{' ':<27}║{RESET}")
    print(f"{PINK}║  🕐 Total Jam      : {jam} jam {menit} menit{' ':<21}║{RESET}")
    print(f"{PINK}║  📝 Jumlah Catatan : {len(catatan)}{' ':<34}║{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
    print()


def ringkasan_mingguan():
    """Fitur pengembangan: Ringkasan belajar mingguan"""
    PINK = "\033[38;5;205m"
    RESET = "\033[0m"
    
    if len(catatan) == 0:
        print()
        print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║      ❌ BELUM ADA DATA MINGGU INI! ❌                ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}║   📈 Mulai belajar untuk melihat ringkasan!          ║{RESET}")
        print(f"{PINK}║                                                       ║{RESET}")
        print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
        print()
        return
    
    # Hitung total waktu per mapel
    ringkasan = {}
    for item in catatan:
        mapel = item["mapel"]
        if mapel in ringkasan:
            ringkasan[mapel] += item["durasi"]
        else:
            ringkasan[mapel] = item["durasi"]
    
    # Hitung total keseluruhan
    total_all = sum(ringkasan.values())
    mapel_terbanyak = max(ringkasan, key=ringkasan.get)
    
    # Tampilkan header tabel
    print()
    print(f"{PINK}╔═══════════════════════════════════════════════════════╗{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}║        📈 RINGKASAN MINGGUAN BELAJARMU 📈            ║{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╠═══════════════════════════════════════════════════════╣{RESET}")
    
    # Tampilkan waktu belajar per mapel
    for mapel, durasi in sorted(ringkasan.items()):
        jam = durasi // 60
        menit = durasi % 60
        print(f"{PINK}║  📚 {mapel:<35} {durasi}m ({jam}j{menit}m)  ║{RESET}")
    
    print(f"{PINK}╠═══════════════════════════════════════════════════════╣{RESET}")
    print(f"{PINK}║  🏆 Terbaik: {mapel_terbanyak:<38}║{RESET}")
    print(f"{PINK}║  ⏱️  Total  : {total_all} menit ({total_all//60}j {total_all%60}m){' ':<22}║{RESET}")
    print(f"{PINK}║                                                       ║{RESET}")
    print(f"{PINK}╚═══════════════════════════════════════════════════════╝{RESET}")
    print()


def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Ringkasan mingguan")
    print("5. Keluar")

# Muat catatan saat program dimulai
muat_catatan()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        ringkasan_mingguan()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar! 📚")
        break
    else:
        print("Pilihan tidak valid")