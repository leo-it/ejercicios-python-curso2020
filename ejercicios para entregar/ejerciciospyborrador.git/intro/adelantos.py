tiempo = 30*12 #años
tasa = 0.05
saldo = 500000
pagoMensual = 2684.11 #mensual
totalPagado = 0
mes = 0

while mes<12 :
    saldo = saldo * (1+ tasa/12) - pagoMensual -1000
    totalPagado = pagoMensual +totalPagado +1000
    mes = mes + 1

    print("Total Pagado: ", totalPagado, "mes: ", mes )


while 0 < saldo :
    saldo = saldo * (1+ tasa/12) - pagoMensual
    totalPagado = pagoMensual +totalPagado
    mes = mes + 1

    print("Total Pagado: ", totalPagado, "mes: ", mes )