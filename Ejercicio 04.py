#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
#y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje
#de IVA, deberá aplicar un 21%.
from typing import Union, Any


def total_factura(precio, porcentaje_iva=21):

    a_pagar: float = float(precio + (precio * porcentaje_iva/100) )            ##
    return a_pagar

total_factura(1000,10.5)