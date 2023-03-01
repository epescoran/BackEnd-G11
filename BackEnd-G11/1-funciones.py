def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print (saludo)


saludar('Edison')

def saludar_varios(*args):
    #cuando se coloca * significa que no hay limities de ese parametro
    # este parametro deber ir al ultimo

    print (args)


saludar_varios('Roxana','Juana', 'Martin', 'Roberto')
