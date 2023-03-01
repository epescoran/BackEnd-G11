class Vehiculo:
    def __init__(self, col, pla, mar) -> None:
        self.color=col
        self.placa=pla
        self.marca=mar

    def verificacionEstado(self, fabricacion):
        return f'El vehiculo de color {self.color} fue fabricado en el año  {fabricacion}'
    
    def concatenarCaracteristicas(self):
        return f'El vehiculo con placa {self.placa} y de color {self.color} es de marca {self.marca}'

vehiculo=Vehiculo("rojo","V21-452","Honda")
#print(vehiculo.verificacionEstado(1999))
#print(vehiculo.concatenarCaracteristicas())




class Alumno:
    def __init__(self,nombre, edad) -> None:
        self.nombre= nombre
        self.edad=edad

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} , Edad: {self.edad}'
    def mostrarNombre(self):
        return self.nombre
    def mostrarEdad(self):
        return self.edad

x=Alumno('Eduardo',30)

print(x)
print(x.mostrarNombre())
