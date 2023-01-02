def berangkat(cuaca):
    if(cuaca=="hujan"):
        print("Cuaca Hari ini Hujan Maka Berangkat dengan Gocar")
    elif(cuaca=="adem"):
        print("Cuaca Hari ini Adem Maka Berangkat dengan Motor")
    else:
        print("Hari ini Libur")
        
berangkat("hujan")