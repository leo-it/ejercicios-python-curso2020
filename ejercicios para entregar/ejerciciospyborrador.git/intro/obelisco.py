grosorBillete = 0.11 * 0.001
alturaObelisco = 67.5
billetes = 1
dia = 1

while alturaObelisco >= grosorBillete * billetes:
    print(dia, billetes*grosorBillete, billetes)
    dia = dia + 1
    billetes = billetes*2

print("dias: ", dia)
print("billetes: ",billetes)
print("grosor:", billetes*grosorBillete)