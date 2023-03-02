from camelcase import CamelCase

instancia = CamelCase()


texto = "hola como estas"
resultado=instancia.hump(texto)
print(resultado)

def sumar(num1:int,num2: int) -> int:
    """Funcion para sumar dos numero"""
    return num1+num2

sumar (10,5)