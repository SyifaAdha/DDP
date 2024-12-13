from Person import *

class Dosen(Person):
    pass
    gelar = ""
    jabatan = ""
    gaji = ""
    
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    
    def setGaji(self, uang):
        self.gaji = uang
   
    def info_dosen(self):
        super().info_person()
        print("Gelar \t\t\t : ", self.gender,
              "\nJabatan \t\t : ", self.jabatan,
              "\nGaji \t\t\t : Rp. ", self.gaji,
              "\n-------------------------------")
        
# d1 = Dosen("Sirojul Munir", "Pria", 43, "S.Si, M.Kom", "LPPM")
# d1.info_dosen()
# d2 = Dosen("Henry Sptono", "Pria", 44, "S.Si, M.Kom", "LTSI")
# d2.info_dosen()

# d1.setGaji(12000000)
# d2.setGaji(10000000)