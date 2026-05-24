def interes_compuesto(capital, tasa, tiempo):
   monto = capital * (1 + tasa) ** tiempo
   interes = monto - capital
   return monto, interes
