# soal no 1
print('------ Soal No 1 ------')

def cetak(kata):
    print(kata)
    
# Fungsi untuk mengonversi suhu dari Celcius ke Fahrenheit
def celcius_ke_fahrenheit(celcius): #parameter
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

cetak(celcius_ke_fahrenheit(0))    
cetak(celcius_ke_fahrenheit(100))  


# soal no 2
print('------ Soal No 2 ------')

# Fungsi untuk mengembalikkan true jika bilangan genap, dan false jika bilangan ganjil
def is_genap(angka): #parameter
    hasil = angka % 2 == 0
    return hasil

cetak(is_genap(4))
cetak(is_genap(7))


# soal no 3
print('------ Soal No 3 ------')

# Fungsi untuk melihat keterangan lulus atau tidak lulus
def nilai(nilai_ujian): #parameter
    if nilai_ujian >= 80:
        return "Lulus"
    else:
        return "Gagal"
    
cetak(nilai(80))
cetak(nilai(60))


# soal no 4
print('------ Soal No 4 ------')

#Fungsi untuk menampilkan bilangan ganjil yang kurang argumens
def bilangan(n): #parameter
    ganjil = [str(i) for i in range(1, n, 2)] 
    print(",".join(ganjil))

bilangan(20)

