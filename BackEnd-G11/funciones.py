def suma(numero_1, numero_2):
       return int(numero_1) + int(numero_2)
    
def resta(numero_1, numero_2):
       return int(numero_1) - int(numero_2)

def multiplicacion(numero_1, numero_2):
     return int(numero_1) * int(numero_2)


#resultado_suma=suma(4,5)
#print(resultado_suma)


def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    if operacion=='suma':
         return suma(valor_1,valor_2)
    elif operacion=='resta':
         return resta(valor_1,valor_2)
    else:
         return multiplicacion(valor_1,valor_2)


opcion =input('Indique operacion matematica: ')
val1 =input('Primer valor: ')
val2 =input('Segundo Valor: ')

resultado= calcularResultadoPorOperacion(opcion,val1,val2)
print("El resultado es: "+ str(resultado))


#print ('La operacion matematica q solicito es:' + opcion)

