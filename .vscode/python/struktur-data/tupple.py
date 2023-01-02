gorengan= ('bakwan','tempe','risol')           #indeks 0
sop=('sop buntut','sop iga','sop kaki')        #indeks 1
nasi=('nasi goreng','nasi uduk','nasi putih')  #indeks 2

# tuple di dalam tuple
makanan = (gorengan,sop,nasi)

print('--------gorengan----------')
for i in makanan[0]:
    print(i)
    
print('------sop-------')

for i in makanan[1]:
    print(i)
    
print('-------nasi-------')

for i in makanan[2]:
    print(i)
    
for i in makanan:
    for m in i:
        print(m)