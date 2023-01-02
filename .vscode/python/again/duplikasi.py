def dup(buah):
    duplikasi=[]
    for x in buah:
        duplikasi.append(x)
        duplikasi.append(x)
    return duplikasi
print(dup(['pepaya','mangga','pisang','durian','jambu']))