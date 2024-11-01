# biodata diri 
print()
print("===== Profil =====")
print()
# input
nama, nim, kelas, noTelp, alamat = "Syifa Adha Riyanni", "0110124167", "SI_07", "085737639791", """"JL. Raya Sawangan 
RT02 RW 09 Kel.Mampang Kec. Pancoran Mas Kota Depok """

# proses, output
print("Nama Mahasiswa", nama)
print("Nim Mahasiswa", nim)
print("Kelas Mahasiswa", kelas)
print("No Telepon Mahasiswa", noTelp)
print("Alamat Mahasiswa", alamat)

print()

#biodata teman
print()
print("===== Profil Teman =====")
print()
#input
nama, nim, kelas,noTelp, alamat ="Sipa Faujiah", "0110124111", "SI07", "085782772965", """Gg. Arus No. 3,
RT.3/ RW.1, Srengseng Sawah, Kec. Jagakarsa, Kota Jakarta Selatan
Daerah Khusus Ibukota Jakarta 10550"""

#proses, output
print("Nama Mahasiswa:", nama)
print("Nim Mahasiswa:", nim)
print("Kelas Mahasiswa:", kelas)
print("Nomor Telepon Mahasiswa:", noTelp)
print("Alamat Mahasiswa:", alamat)

print()

#nilai berat badan ideal
print()
print("===== Nilai Berat Badan Ideal =====")
print()
#input
tb = int(input("Masukan Tinggi Badan: "))

#proses
bbIdeal = (tb - 100) + ((tb - 100) * 0.15)

#output
print("Berat badan Ideal dengan tinggi badan", tb, "adalah", bbIdeal, "kg")

print()

#nilai konversi dari celcius ke fahreinheit
print()
print("===== Nilai Konversi Dari Celcius Ke Fahreinheit =====")
print()
#input
celcius = float(input("Masukan Nilai Celcius: "))

#proses
fahreinheit = (celcius*9/5)+32

#output
print(celcius,"Derajat Celcius sama dengan", fahreinheit, "derajat fahreinheit")

print()

#luas dan volume tabung
print()
print("===== Luas Dan Volume Tabung =====")
print()
#input
jariJari = int(input("Masukan Jari-jariinya: "))
tinggi = int(input("Masukan Tingginya: ")) 
pi = 22/7

#proses
volume = pi*jariJari*jariJari*tinggi
luas = 2*pi*jariJari*(jariJari+tinggi)

#output
print(jariJari, tinggi, "Volume Tabung ="," {:.2f}".format(volume))
print("Luas Permukaan Tabung ="," {:.2f}".format(luas))

