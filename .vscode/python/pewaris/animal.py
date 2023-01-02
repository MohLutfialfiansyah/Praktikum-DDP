# parent class
class Animal:
    def __init__(self,nama,makanan,hidup,berkembangBiak) :
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang = berkembangBiak
    def printname(self):
        print(self.nama,self.makanan,self.hidup,self.berkembang)
# Child 1
class Badak(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak,jenis,warna):
        super().__init__(nama, makanan, hidup, berkembangBiak)     
        self.jenis = jenis
        self.warna = warna
        
    def suaraBadak():
        return "rawrrr"
    
    def b(self):
        print("Nama Hewan ini adalah",self.nama,"\nMakanannya adalah",self.makanan,"\nHidup di",self.hidup,"\nBerkembang Biang dengan Cara",self.berkembang,"\nHewan ini Berjenis",self.jenis,"\nWarna Hewan Ini adalah",self.warna)
#Child 2
class Ikan(Animal):  
    def __init__(self, nama, makanan, hidup, berkembangBiak,jenis,warna):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis= jenis
        self.warna=warna    
    def i(self):
        print("Nama Hewan ini adalah",self.nama,"\nMakanannya adalah",self.makanan,"\nHidup di",self.hidup,"\nBerkembang Biang dengan Cara",self.berkembang,"\nHewan ini Berjenis",self.jenis,"\nWarna Hewan Ini adalah",self.warna)
#Child 3
class Ular(Animal):  
    def __init__(self, nama, makanan, hidup, berkembangBiak,jenis,warna):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis= jenis
        self.warna=warna    
    def u(self):
        print("Nama Hewan ini adalah",self.nama,"\nMakanannya adalah",self.makanan,"\nHidup di",self.hidup,"\nBerkembang Biang dengan Cara",self.berkembang,"\nHewan ini Berjenis",self.jenis,"\nWarna Hewan Ini adalah",self.warna)



x = Badak("Badak","Tumbuhan","Darat","Melahirkan","Bercula satu","Hitam coklat" "\n")
x.b()

y = Ikan("Ikan","Omnivora(segala jenis makanan)","Laut","Bertelur","Nemo","Orange" "\n")
y.i()

z = Ular("Ular","Daging","Darat","Bertelur","Cobra","Hitam")
z.u()