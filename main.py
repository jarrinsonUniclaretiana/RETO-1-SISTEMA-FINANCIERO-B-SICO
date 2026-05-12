import intereses_simple

capital = 1000
tasa = 0.05  # 5%
tiempo = 2   # años

interes = intereses_simple.calcular_interes_simple(capital, tasa, tiempo)
total = intereses_simple.calcular_monto_total(capital, tasa, tiempo)

print("Interés generado:", interes)
print("Monto total a pagar:", total)