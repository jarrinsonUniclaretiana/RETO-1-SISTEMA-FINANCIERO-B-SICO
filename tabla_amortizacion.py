def calcular_cuota(capital, tasa, tiempo):
    cuotas = tiempo * 12
    mensual = tasa / 12
    factor = (1 + mensual) ** cuotas
    cuota = capital * (mensual * factor) / (factor - 1)
    return round(cuota, 2)
 
 
def tabla_amortizacion(capital, tasa, tiempo):
    cuotas = tiempo * 12
    mensual = tasa / 12
    cuota = calcular_cuota(capital, tasa, tiempo)
    saldo = capital
 
    print(f"\nCapital: ${capital:,.2f} | Tasa: {tasa*100:.2f}% anual | Tiempo: {tiempo} año(s) ({cuotas} meses)")
    print(f"\n{'Mes':<8} | {'Interés':<14} | {'Amortización':<16} | {'Saldo Final'}")
    print("-" * 55)
 
    for i in range(1, cuotas + 1):
        interes = round(saldo * mensual, 2)
        amortizacion = round(cuota - interes, 2)
        saldo = round(saldo - amortizacion, 2)
        print(f"{i:<8} | {interes:<14,.2f} | {amortizacion:<16,.2f} | {saldo:,.2f}")