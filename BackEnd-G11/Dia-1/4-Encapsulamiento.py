class Producto:
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        self.nombre=nombre
        self.precio= precio
        self.cantidad=cantidad
        self.fecha_vencimiento= fecha_vencimiento
        # atributo privado> no se puede acceder a esta informacion fuera de la clase
        self.__ganancia=0.3

    def prueba(self):
        self.__ganancia
        print(self.__ganancia)



pitahaya= Producto('pitahaya',4.50,100, '2023-05-01')
print(pitahaya.nombre)

pitahaya.prueba()