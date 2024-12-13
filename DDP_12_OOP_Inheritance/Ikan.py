from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.jenis = jenis
        self.ukuran = ukuran
        
    def info_ikan(self):
        super().info_animal(),
        print("Jenis \t\t\t : ", self.jenis,
              "\nUkuran \t\t\t : ", self.ukuran)
        
ikan_angelfish = Ikan("Angelifish", "Pelet", "Air", "Bertelur", "Ikan Hias", "Kecil")
ikan_angelfish.info_ikan()
print("=====================================================")
ikan_hiu = Ikan("Hiu", "Ikan Ikan Kecil", "Air", "Beranak dan Bertelur (Tergantung Spesiesnya)", "Ikan Laut", "Besar")
ikan_hiu.info_ikan()