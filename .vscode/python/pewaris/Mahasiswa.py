from Person import *

class Mahasiswa(Person):
    prodi = ""
    semester = ""
    
    def __init__(self, nama, gender, umur,prodi,semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
        
    def cetak(self):
        super().cetak()
        print("------------------------")
        print("Prodi :",self.prodi)
        print("Semester :",self.semester)
        print("------------------------")