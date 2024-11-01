#
print('# Soal NO1 #')

kendaraan = ['vario', 'motor', 200, 'silver', 2]
print(kendaraan)

kendaraan.append('25jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'yamaha')
print(kendaraan)

print()

#
print('# Soal NO2 #')

angka_pilihan = int(input("""Masukan Pilihan: 
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukan nilai sisi: "))
        luas_persegi = sisi ** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2 ")
    
    case 2:
        print("Menghitung Luas Lingkaran")
        jariJari= float(input('Masukan nilai jari-jari lingkaran: '))
        luas_lingkaran = 3.14 * (jariJari **2)
        print(f"Luas lingkaran ={luas_lingkaran}")
        
    case 3:
        print("Menghitung Luas Segitiga")
        alas = float(input('Masukan nilai alas segitiga: '))
        tinggi = float(input('Masukan nilai tinggi segitiga: '))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga = {luas}")
        
    case _:
        print("Input tidak valid")
        