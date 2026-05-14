# interes_simple.py

def calcular_interes_simple(capital, tasa, tiempo):
    """
    Calcula el interés simple de un préstamo.
    
    :param capital: Monto del préstamo
    :param tasa: Tasa de interés anual (en decimal)
    :param tiempo: Tiempo en años
    :return: Interés generado
    """
    interes = capital * tasa * tiempo
    return interes


def calcular_monto_total(capital, tasa, tiempo):
    """
    Calcula el monto total a pagar (capital + interés).
    """
    interes = calcular_interes_simple(capital, tasa, tiempo)
    return capital + interes