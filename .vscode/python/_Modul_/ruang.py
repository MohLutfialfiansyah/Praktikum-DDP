def lingkaran(jari1,jari2):
    hasil=3,14*jari1*jari2
    print('Luas Lingkaran', jari1, 'dan', jari2, 'adalah', hasil)

def kubus(sisi1,sisi2) :
    hasil=6*sisi1*sisi2
    print('Luas Kubus',sisi1,'dan', sisi2,'adalah',hasil ) 

def balok(tinggi,panjang,lebar):
    v=panjang*lebar+panjang*tinggi+lebar*tinggi
    hasil=2*v
    print('luas balok adalah', hasil) 

def bola(jari_jari,diameter):
    r=diameter/2
    hasil=4*3,14*r**jari_jari
    print('luas bola adalah',hasil)