from flask import Flask, request, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return "Mi primera API con Flask 😊"

@app.route("/alumno")
def alumno():
    return{
        'nombre': 'Eduardo',
        'edad':30,
        'promedio':18
    }

@app.route("/alumnos", methods=['GET','POST', 'PUT', 'DELETE', 'OPTIONS','PATCH'])
def alumnos():
    print(request.method)
    if request.method=='GET':
        return lista_alumnos
    elif request.method=='POST':
        lista_alumnos.append(request.json)
        return lista_alumnos

lista_alumnos=[
        {
        'nombre': 'Eduardo',
        'edad':30,
        'promedio':18
    },
    {
        'nombre': 'Guillermo',
        'edad':25,
        'promedio':15
    },
    {
        'nombre': 'Edison',
        'edad':30,
        'promedio':17
    }
    ]

#@app.route("/alumno/<int:nombre>")
@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno['nombre']==nombre:
            return alumno
    return {
            'message': "El alumno no existe"
        }
    #return f'El alumno se llama: {nombre}'


@app.route("/html")
def html():
    edad=10
   # return "<button> Dame Click </button>"
    return render_template('index.html', edad=edad)
# debug=True > Si realizamos algun cambio podremos verlo en tiempo real (se reiniciara el servidor)

@app.route("/files", methods=['POST'])
def filesl():
    print(request.files['foto'].read().decode())
   
    return 'Archivo recibido exitosamente'


app.run(debug=True)