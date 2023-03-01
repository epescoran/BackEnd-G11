class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre= nombre
        self.apellido= apellido
    def saludar(self):
        print('saludar')


class Beneficio:
    def __init__(self,detalle) -> None:
        self.detalle= detalle

    def mostrar_beneficios(self):
        return {
            'detalle': self.detalle
        }

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado):
        self.grado= grado
        super().__init__(nombre,apellido)
    def dar_vueltas(self):
        print('Dando vueltas')
        # Polimorfismo > poli (muchas) morfa (formas) dependiendo de donde se mande a llamar al metodo este tendra un comportamiento u otro, en este caso estamos modificando el metodo de la clase padre Saludar
    def saludar(self):
        print ('Hola soy un alumno')

class Docente(Persona, Beneficio):
    def __init__(self, nombre, apellido,seguro_social,detalle):
        self.seguro_social= seguro_social
        Persona.__init__(self,nombre,apellido)
        Beneficio.__init__(self,detalle)
    def evaluar(self):
        print('Evaluando')


eduardo= Alumno('Eduardo','de rivero','Quinto')
paolo=Docente('Paolo', 'Soncco','1313200','Pizza 15% dscto')

eduardo.saludar()
paolo.saludar()

print(paolo.mostrar_beneficios())
print(eduardo.nombre)