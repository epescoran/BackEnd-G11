numero =10
otro_numero= 20

if numero>11:
    print('Es Mayor que 11')

string = "Soy un string"
boolean_true= True
boolean_false = False
flotantes = 3.14
diccionarios={
    'nombre':'Eduardo'
}
listas= [1,2,3,'string',3.14,[2,3]]
tuplas =("texto_1","texto_2","texto_3")
#print(type(listas))

x = 5
x = 'cinco'
X= 'numero'
y='5'
y= int(y)
y=str(y)
y= float(y)
#print (type(y))
#FORMAR INCORRECTAS DE NOMBRAR VARIABLES

#numero-cinco=5
#5numero=5
#numero cinco=5


#FORMAS CORRECTAS DE NOMBRAR VARIABLES
numero_cinco=5
Numero_Cinco=5
_numeroCinco=5

#ASIGNAR MULTIMPLES VARIABLES
a,b,c =2,5,'string'
#print (b)

def myFuncion():
    variable_1 ='Texto de ejemplo'
    print(variable_1)


#myFuncion()

# OPERADORES
# 5==5
# 4!=5
# 0<1
# 5 >=5
# 6<=6
# or
# and
# not


edad = 17

if edad<18 :
    print('Eres menor de edad')
elif edad == 18:
    print ('Acabas de convertirte en mayor de edad')
else:
    print('Eres mayor de edad')


estado_civil = 'C'

#if estado_civil=='C':
#    print('Esta casado')
#elif estado_civil=='V':
#    print('Esta viudo')
#elif estado_civil=='D':
#    print('Esta divorciado')
#else:
#    print('Esta soltero')



#lista_nombres=['Eduardo','Antoni','Luis','May','Paolo']
#for nombre in lista_nombres:
#    print(nombre)


lista_numeros=[23,24,25,26,27]
#for num in lista_numeros:
#    print(num)

#print(lista_numeros[2])


for num in lista_numeros:
    if num ==25:
        break
    #print(num)
    #23
    #24



for num in lista_numeros:
    if num ==25:
        continue
    #print(num)
    #23
    #24
    #26
    #27


cadena_texto="Hola, soy alumno del G11 BackEnd"

#for letra in cadena_texto:
    #print (letra)
    
print (cadena_texto[3])


