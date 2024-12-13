from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_racun, bentuk_kepala):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.jenis_racun = jenis_racun
        self.bentuk_kepala = bentuk_kepala
        
    def info_ular(self):
        super().info_animal(),
        print("Jenis Racun\t\t : ", self.jenis_racun,
              "\nBentuk Kepala\t\t : ", self.bentuk_kepala)
        
ular_python = Ular("Python", "Mamalia Kecil dan Sedang (Hamster, Tikus, Rusa Muda, Kambing)", "Darat", "Bertelur", "Berbisa", "Datar Dan Besar")
ular_python.info_ular()
print("=====================================================")
ular_viper = Ular("Viper", "Mamalia, Reptil, Serangga", "Darat", "Beranak", "Berbisa", "Segitiga Yang Khas")
ular_viper.info_ular()