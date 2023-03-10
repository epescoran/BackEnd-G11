from flask import Flask, request
from psycopg2 import connect
from flask_cors import CORS


app = Flask(__name__)
CORS(app, methods=['GET','POST','PUT','DELETE'], origins=['http://127.0.0.1:5500','http://localhost:5500'])


conexion=connect(host='localhost', database='pruebas', user='postgres', password='a123a456a7890A')


@app.route('/', methods=['GET'])
def inicial():
    return{
        'message':'Bienvenidos a mi API'
    }

@app.route('/alumnos', methods=['GET','POST'])
def alumnos():
    if request.method=='GET':
       # conexion=connect(host='localhost', database='pruebas', user='postgres', password='a123a456a7890A')
        cursor= conexion.cursor()
        cursor.execute('select * from alumnos;')
        resultado=cursor.fetchall()
        #print(resultado)
        alumnos_resultado=[]
        for alumno in resultado:
            info_alumno = {
                'id': alumno[0],
                'nombre':alumno[1],
                'apellido':alumno[2],
                'sexo':alumno[3],
                'fecha_creacion':alumno[4],
                'matriculado':alumno[5]       
                }
          
            alumnos_resultado.append(info_alumno)
        return {
            'message': alumnos_resultado
        }
    elif request.method=='POST':
        data=request.json
        print (data)
        cursor= conexion.cursor()
        cursor.execute("INSERT INTO ALUMNOS(nombre, apellido, matriculado) VALUES(%s,%s,%s);",( data.get('nombre'),data.get('apellido'), data.get('matriculado') ))
        return{
            'message':'Alumno ingresado exitosamente'
        }
        conexion.commit()




@app.route('/alumno/<id>', methods=['GET','PUT','DELETE'])
def gestion_alumno(id):
    if request.method=='GET':
        cursor= conexion.cursor()
        cursor.execute("select * from alumnos where id = %s;",(id,))
        alumno=cursor.fetchone()
        print(alumno)
        if alumno:
           return{
               'content':{
                'id': alumno[0],
                'nombre':alumno[1],
                'apellido':alumno[2],
                'sexo':alumno[3],
                'fecha_creacion':alumno[4],
                'matriculado':alumno[5]  
               }
           } 
        else:
            return{
                'msessage':'El alumno no existe'
            }
    elif request.method=='PUT':
        data=request.json
        
        cursor= conexion.cursor()
        cursor.execute("UPDATE ALUMNOS SET nombre=%s, apellido=%s, matriculado=%s WHERE id=%s;",( data.get('nombre'),data.get('apellido'), data.get('matriculado'),data.get('id') ))
        return{
            'message':'Alumno modificado exitosamente'
        }
        conexion.commit()
    
    elif request.method=='DELETE':
        data=request.json
        
        cursor= conexion.cursor()
        cursor.execute("DELETE ALUMNOS WHERE id=%s;",(data.get('id') ))
        return{
            'message':'Alumno eliminado exitosamente'
        }
        conexion.commit()




if __name__=='__main__':
    app.run(debug=True)