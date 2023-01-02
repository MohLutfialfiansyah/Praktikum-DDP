def tambah():
    bil1 = int(input("bilangan 1 >>"))
    bil2 = int(input("bilangan 2 >>"))

    hasil = bil1 + bil2
    print("hasil tambah dari", bil1, "+", bil2, "=", hasil)

def kurang():
    bil1 = int(input("bilangan 1 >>"))
    bil2 = int(input("bilangan 2 >>"))

    hasil = bil1 - bil2
    print("hasil kurang dari", bil1, "-", bil2, "=", hasil)

def kali():
    bil1 = int(input("bilangan 1 >>"))
    bil2 = int(input("bilangan 2 >>"))

    hasil = bil1 * bil2
    print("hasil kali dari", bil1, "*", bil2, "=", hasil)



def tambah(*angka):
    hasil=0