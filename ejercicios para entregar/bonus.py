
tasa = 0.05
saldo = 500000
pagoMensual = 2684.11 #mensual
totalPagado = 0.0
mes = 0
pagoExtra = 1000 
pago_extra_mes_fin= 108
pago_extra_mes_comienzo = 61


while 0 < saldo :
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+ tasa/12) - pagoMensual -pagoExtra
        totalPagado = pagoMensual + totalPagado + pagoExtra
        mes = mes + 1
    elif saldo <= 2684 : 
        saldo1 = saldo * (1+ tasa/12) 
        saldo = saldo * (1+ tasa/12) - saldo1
        totalPagado1 = saldo1
        mes = mes + 1
        print(f'Total Pagado Mes: ${round(totalPagado1, 2)} en el mes: {mes}')



    else:
        saldo = saldo * (1+ tasa/12) - pagoMensual
        totalPagado = pagoMensual +totalPagado
        mes = mes + 1
        
    
    print(f'Total Pagado : ${round(totalPagado, 2)} en el mes: {mes}')
    print("Saldo:",round(saldo,2))
print('Total Pagado', round(totalPagado, 2))
print(f"meses {mes}")        