
from pprint import pprint


ciudades=[
    {
        'nombre':'Tumbes',
        'habitantes':500000
    },
    {
        'nombre':'Arequipa',
        'habitantes':800000
    },
    {
        'nombre':'Loreto',
        'habitantes':10000
    }
]

def habitante(ciudad):
    return ciudad['habitantes']

#lista_numeros =[1,5,2,4,6,9,8]
#lista_numeros.sort()
#lista_numeros.sort(reverse=True)
ciudades.sort(key=habitante, reverse=True)
#pprint(ciudades)

ciudades.append({'nombre':'Cusco', 'habitantes':20000})

#ciudades.pop(0)


index=0
for ciudad in ciudades:
    if ciudad['nombre']=='Cusco':
        ciudades.remove(ciudades[index])
    index=index+1


#pprint(ciudades)

lista=['Arequipa','Cusco','Tumbes']
lista.remove('Arequipa')
#pprint(lista)

for x, y  in enumerate(lista):
    print(x,y)



