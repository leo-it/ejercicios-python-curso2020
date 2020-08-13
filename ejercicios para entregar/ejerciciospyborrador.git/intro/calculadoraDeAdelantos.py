#hay algo mal me da mas meses

tiempo = 30*12 #años
tasa = 0.05
saldo = 500000
pagoMensual = 2684.11 #mensual
totalPagado = 0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while 0 < saldo :
    saldo = saldo * (1+ tasa/12) - pagoMensual
    totalPagado = pagoMensual +totalPagado
    mes = mes + 1

    print("Total Pagado: ", round(totalPagado,2), "mes: ", mes )

 
while mes> pago_extra_mes_comienzo and mes < (4*12+pago_extra_mes_comienzo):
    saldo = saldo * (1+ tasa/12) - pagoMensual - pago_extra
    totalPagado = pagoMensual +totalPagado + pago_extra
    mes = mes + 1

    print("Total Pagado: ", round(totalPagado,2), "mes: ", mes )
