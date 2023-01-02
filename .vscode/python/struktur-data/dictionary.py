# menggunakan dict dengan key:value
data_diri={"nama":"Alfian"}

#print(data_diri["nama"])


nilai={'firda':89, 'isnaya':70, 'salima':100, 'rahmah':75}

#untuk mengakses valuenya aja menggunakan function value()
for i in nilai.values():
    print(i)
    
 #untuk mengakses key nya aja menggunakan function keys()
for i in nilai.keys():
    print(i)
    
 #untuk mengakses kedua2nya menggunakan function items()   
for nama,nilai in nilai.items():
    print(nama, ":" ,nilai)