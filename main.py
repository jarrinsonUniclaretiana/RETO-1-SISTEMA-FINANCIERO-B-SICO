import intereses_simple
import tabla_amortizacion
import interes

capital = 1000
tasa = 0.05  # 5% como decimal (0.05)
tiempo = 2   # años

interes_simple = intereses_simple.calcular_interes_simple(capital, tasa, tiempo)
total = intereses_simple.calcular_monto_total(capital, tasa, tiempo)

print("\nInterés generado:", interes_simple)
print("Monto total a pagar:", total)

print("=" * 40)

monto, interes_compuesto = interes.interes_compuesto(capital, tasa, tiempo)

print("\nMonto final:", monto)
print("Interés generado (compuesto):", interes_compuesto)

print("=" * 40)

print("\nTabla de Amortización:")
tabla_amortizacion.tabla_amortizacion(capital, tasa, tiempo)