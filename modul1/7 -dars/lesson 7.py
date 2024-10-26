def onlikdan_tortlikka(son) :
    tortlikdagi_son = ''
    while son > 0:
        ozgaruvchi = son % 4
        tortlikdagi_son = str(ozgaruvchi) +tortlikdagi_son
        son = son // 4
    return tortlikdagi_son

print(onlikdan_tortlikka(4))


    














