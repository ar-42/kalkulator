# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian oleh nol"

# Fungsi untuk menampilkan menu operasi
def tampilkan_menu():
    print("\nPilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

# Program Utama
while True:
    tampilkan_menu()

    # Meminta input dari pengguna
    pilihan = input("Masukkan nomor operasi yang diinginkan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih. Program selesai.")
        break

    # Meminta input bilangan dari pengguna
    bilangan1 = float(input("Masukkan bilangan pertama: "))
    bilangan2 = float(input("Masukkan bilangan kedua: "))

    # Memproses input pengguna
    if pilihan == '1':
        print(bilangan1, "+", bilangan2, "=", tambah(bilangan1, bilangan2))
    elif pilihan == '2':
        print(bilangan1, "-", bilangan2, "=", kurang(bilangan1, bilangan2))
    elif pilihan == '3':
        print(bilangan1, "*", bilangan2, "=", kali(bilangan1, bilangan2))
    elif pilihan == '4':
        print(bilangan1, "/", bilangan2, "=", bagi(bilangan1, bilangan2))
    else:
        print("Input tidak valid")

    # Tanya apakah pengguna ingin melakukan perhitungan lagi
    ulangi = input("Mau melakukan perhitungan lagi? (ya/tidak): ")
    if ulangi.lower() != 'ya':
        print("Terima kasih. Program selesai.")
        break
