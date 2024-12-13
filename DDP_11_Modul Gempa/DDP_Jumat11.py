class Orang:
    # variabel (properti)
    nama = "Syifa"
    umur = 19
    gender = "Perempuan"
    
    # fungsi (method)
    def ngomong(self):
        print("Saya bisa berbicara")
        
    def jalan(self, kata):
        print("Saya bisa jalan", kata)
        
# objek1
supir = Orang()
supir.nama = "Aya"
print(supir.nama)
supir.jalan("Kapan?")
supir.sim = "A"
print(supir.sim)
