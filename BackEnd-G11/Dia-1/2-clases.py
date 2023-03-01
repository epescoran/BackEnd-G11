class Persona:
    estatura =1.80
    peso= 80
    signo_zodiacal='LEO'

    def sumar(self, *args):
        # Self es como el this en el cado de js, c#, c++
        total=0
        for numero in args:
            total=total+numero
        
        return total

    def saludar(self, nombre):
        return 'Hola {}'.format(nombre)



persona1= Persona()
persona2= Persona()

persona1.peso=70
persona2.peso=50

print(persona1.peso)
print(persona2.peso)

resultado1=persona1.sumar(10,20,30)
resultado2=persona2.sumar(1+2+3+4+5)

print(resultado1)
print(resultado2)