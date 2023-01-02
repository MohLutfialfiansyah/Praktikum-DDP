import aritmatika as hitung
print("1.tambah")
print("2.kurang")
print("3.kali")
data = input("Masukkan Pilihan :")
while(True):
    if data =="1":
        hitung.tambah()
    elif data=="2":
        hitung.kurang()
    elif data=="3":
        hitung.kali()
    else:
        print("Error")