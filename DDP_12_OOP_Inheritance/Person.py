class Person:
    def __init__(self, nama, gender, umur):
        self.nama= nama
        self.gender = gender
        self.umur = umur


    def info_person(self):
        print("Nama \t\t\t : ", self.nama,
              "\nJenis Kelamin\t\t : ", self.gender,
              "\nUmur \t\t\t : ", self.umur)
        
# person = Person("Syifa", "Perempuan", 19)
# person.info_person()
