def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print (saludo)


##saludar('Edison')

def saludar_varios(*args):
    #cuando se coloca * significa que no hay limities de ese parametro
    # este parametro deber ir al ultimo
    #Todos los valoes q se pasen al parametro se almacenan en una tupla
    # Las tuplas a diferencia de los arreglos no se pueden modificar, una vez creados sus valores no se pueden cambiar
    
    #print (args)

    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        # print (saludo)


saludar_varios('Roxana','Juana', 'Martin', 'Roberto')
saludar_varios('Luis','Pedro')
saludar_varios()
saludar_varios('Eduardo',20,True,10.5)



def informacion_usuario(**kwargs):
    # kwargs > keyboard argument o se le pasan parametros por llaves
  #   print (kwargs)
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

##informacion_usuario(nombre='Eduardo', edad=30, estado_civil='soltero', estatura='1.88')
##informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Colombiana', fecha_nacimiento='31/06/1999')

##Recibir dos valores y hacer la division
def dividir (dividendo, divisor):
    try:
        valor=dividendo/divisor
        return valor

    except ZeroDivisionError:
        return 'No puede haber division entre 0'
    except TypeError:
        return 'Las divisiones solos pueden ser entre numeros'
    except:
        return 'Error desconocido'
    

valor= dividir(10,5)
print(valor)
valor=dividir(10,0)
print(valor)
valor=dividir('a','h')
print(valor)