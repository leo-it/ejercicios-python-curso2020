
tasa = 0.05
saldo = 500000
pagoMensual = 2684.11 #mensual
totalPagado = 0.0
mes = 0
pagoExtra = 1000 


while mes < 12:
    saldo = saldo * (1+ tasa/12) - pagoMensual -pagoExtra
    totalPagado = pagoMensual + totalPagado + pagoExtra
    mes = mes + 1
    print(f'Total Pagado: ${round(totalPagado, 2)} en el mes: {mes}')


while 0 < saldo :
    saldo = saldo * (1+ tasa/12) - pagoMensual
    totalPagado = pagoMensual +totalPagado
    mes = mes + 1


    print(f'Total Pagado: ${round(totalPagado, 2)} en el mes: {mes}')
print('Total Pagado', round(totalPagado, 2))
print(f"meses {mes}")        