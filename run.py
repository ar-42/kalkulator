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

# Menampilkan menu operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
pilihan = input("Masukkan nomor operasi yang diinginkan (1/2/3/4): ")

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
