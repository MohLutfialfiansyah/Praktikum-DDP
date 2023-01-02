class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""
    
    def __init__(self,nim,nama,rombel):
        self.nama = nama
        self.nim = nim
        self.rombel = rombel
    def welcome(self):
        print("================================\nHallo",self.nama,"\nYour Nim",self.nim,"\nYour Rombel",self.rombel)
        
    def lulus(self,nilai):
        if(nilai>90):
            print("Selamat Anda Lulus Mendapat \nGelar Sarjana 1 Teknik Informatika\n",self.nama,"S.T\n================================")
        else:
            print("Maap Anda Tidak Lulus")

class Alfian(Mahasiswa):
    def __init__(self, nim, nama, rombel,kampus,organisasi,bisnis,mahir):
        super().__init__(nim, nama, rombel)
        self.kampus= kampus
        self.organisasi = organisasi
        self.bisnis = bisnis
        self.mahir = mahir
    def Cetak(self):
        print("================Mahasiswa Berpretasi==========\nYang bernama ",
              self.nama,"\nNim ",self.nim,"\nDari Rombel",self.rombel,"\nBerkampus di",
              self.kampus,"\nPernah di Organisasi",self.organisasi,"\nSudah Berbisnis di Perusahaan",
              self.bisnis,"\nMahir dalam Bidang",self.mahir
              
              )        

y = Alfian("0110222078","Muhammad Lutfi Alfian","TI 13","STT-Nurul Fikri","Presiden Mahasiswa","Lazada","Cyber Security")
y.Cetak()

# x = Mahasiswa("0110222078","Muhammad Lutfi Alfian","TI 13")
# x.welcome()
# x.lulus(100)

# mhs1 = Mahasiswa()
# mhs1.nama = "Muhammad Lutfi Alfian"
# mhs1.nim = "0110222078"
# mhs1.rombel = "TI 13"

# print("==========================")
# print(mhs1.nama)
# print(mhs1.nim)
# print(mhs1.rombel)
# mhs1.lulus(100)
# print("=========================")

# class Alfian(Mahasiswa):
#      def __init__(self,nim,nama,rombel,peringkat) :
#          super().__init__(self,nim,nama,rombel)
#          self.nama =nama
#          self.nim = nim
#          self.rombel = rombel
#          self.peringkat = peringkat
        
#      def printmahasiswa():
#          print(Alfian("0110222078","Muhammad Lutfi Alfian","Ti 13","1"))

