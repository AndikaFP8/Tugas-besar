# Catatan Keuangan Sederhana
import csv

# File untuk menyimpan data transaksi
FILE_NAME = "catatan_keuangan.csv"

# Fungsi untuk menambahkan transaksi
def tambah_transaksi(jenis, jumlah, deskripsi):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jenis, jumlah, deskripsi])
    print(f"Transaksi {jenis} sebesar {jumlah} berhasil ditambahkan!")

# Fungsi untuk menampilkan semua transaksi
def lihat_transaksi():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("Daftar Transaksi:")
            print(f"{'Jenis':<15} {'Jumlah':<10} {'Deskripsi':<20}")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]:<15} {row[1]:<10} {row[2]:<20}")
    except FileNotFoundError:
        print("Belum ada transaksi yang dicatat.")

# Fungsi untuk menghitung total saldo
def hitung_saldo():
    saldo = 0
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "Pemasukan":
                    saldo += int(row[1])
                elif row[0] == "Pengeluaran":
                    saldo -= int(row[1])
        print(f"Total saldo saat ini: {saldo}")
    except FileNotFoundError:
        print("Belum ada transaksi yang dicatat.")
        saldo = 0
    return saldo

# Menu utama
def menu():
    while True:
        print("\nCatatan Keuangan")
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Hitung Saldo")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            jenis = input("Jenis (Pemasukan/Pengeluaran): ")
            jumlah = int(input("Jumlah: "))
            deskripsi = input("Deskripsi: ")
            tambah_transaksi(jenis, jumlah, deskripsi)
        elif pilihan == "2":
            lihat_transaksi()
        elif pilihan == "3":
            hitung_saldo()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
menu()