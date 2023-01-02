def konsonan(k):
    x='aiueo '
    y=''
    for data in k :
        if data in x :
            continue
        else:y+=data
    return y

print (konsonan("Nurul Fikri"))