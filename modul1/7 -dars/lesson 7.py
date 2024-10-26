def Nima_gap(son) :
    salom = ''
    while son > 0:
        harp = son % 2
        salom = str(harp) +salom
        son = son // 2
    return salom

print(Nima_gap(4))


    














