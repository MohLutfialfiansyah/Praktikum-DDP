
hasil_akhir=[
      {'nama' : 'Reza', 'nilai': 70},
      {'nama' : 'Ciut', 'nilai': 63},
      {'nama' : 'Dian', 'nilai': 80},
      {'nama' : 'Badu', 'nilai': 40}, 
]


for i in hasil_akhir:
  if i['nilai']>65:
    print(i['nama'])