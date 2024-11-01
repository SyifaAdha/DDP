# program menentukan bilangan ganjil dan genap
print('## 1. Program Bilangan Ganjil dan Genap ##')

# Input Bilangan 
bilangan = int(input('Masukan bilangan anda: '))

# Proses dan Output
if bilangan % 2 == 0:
    print(bilangan, 'Merupakan bilangan genap')
else:
    print(bilangan, 'Merupakan bilangan ganjil')

print()
    
# program menentukan nilai ujian
print('## 2. Program Menentukan Nilai Ujian ##')

# Input Nilai
nilai_ujian = int(input('Masukan Nilai Anda: '))

# Proses dan Output
if nilai_ujian >= 75:
    print('Kamu Dinyatakan Lulus')
else:
    print('Kamu Dinyatakan Tidak Lulus')

print()
    
# program cek usia dan status
print('## 3. Program Cek Usia Dan Status ##')

# Input Usia
usia = int(input('Masukan Usia Anda: '))

# Proses dan Output
if usia >= 18:
    print('Kamu Dewasa')
elif usia <= 13 and usia <= 17:
    print('Kamu Remaja')
else:
    print('Kamu Anak-Anak')
    
print()
    
# program cek keanggotaan
print('## 4. Program Cek Keanggotaan ##')

# Input Status
status_anggota = input("""Daftar Keanggotaan Di Bawah Ini
1. Gold
2. Silver
3. Bronze
Masukan Pilihan Kamu: """).lower()

# Proses dan Output
if status_anggota == 'gold' or status_anggota == 'silver':
    print('Selamat! Anda Mendapatkan Diskon.')
elif status_anggota == 'bronze':
    print('Maaf Anda Tidak Mendapatkan Diskon')
else:
    print('Masukan Kata Dengan Benar')

print()

# program pembelian diskon
print('## 5. Program Pembelian Diskon ##')

# Input Jumlah Pembelian
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))

# proses dan output
total_harga = jumlah_pembelian * (0.9 if jumlah_pembelian > 100 else 1)
print(f"Total harga setelah diskon: {total_harga}")