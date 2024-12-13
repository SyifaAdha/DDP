from Person import *

class Mahasiswa(Person):
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
        
    def info_mahasiswa(self):
        super().info_person()
        print("Prodi \t\t\t : ", self.prodi,
              "\nSemester \t\t : ", self.semester,
              "\n-------------------------------")
        
# m1 = Mahasiswa("Siti Aminah", "Wanita", 20, "SI", 3)
# m1.info_mahasiswa()
# m2 = Mahasiswa("Budi Santoso", "Pria", 23, "TI", 5)
# m2.info_mahasiswa()

