from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto


class MaestroController(Resource):
    def get(self):
        query : Query = conexion.session.query(Maestro)
        query.all()
        resultado = query.all()
        #print (resultado[0].numero)
        #print (resultado[0].descripcion)
        dto= MaestroDto()
        #dump > es eun metodo en el cual le paso la/las instancias que quiero conververit a tipo de datos genericos Si se le pasa mas de una instancia osea una lista de instancias se le tiene que adicionar el parametro many=True para indicar que lo tendra que interar
        maestros =dto.dump(resultado, many=True)

        #for nivel in resultado:
        #    niveles.append({
        #        'id': nivel.id,
        #        'numero': nivel.numero,
        #        'descripcion': nivel.descripcion
        #    })

        return{
            'content': maestros
        }

    def post(self):
        data = request.json
        dto = MaestroDto()
        # load > aca le pasamos un diccionario y lo convertira y validara si toda la informacion es correcta, si no lo es, emitira un error y si la informacion esta bien, entonces deovolverar un diccionario con la data correcta
        try:
            data_validada= dto.load(data)
            print (data_validada)
        

            nuevo_maestro=Maestro(nombre=data_validada.get('nombre'), apellidos = data_validada.get ('apellidos'),correo=data_validada.get('correo'),direccion=data_validada.get('direccion'),)
            conexion.session.add(nuevo_maestro)
            conexion.session.commit()
            return{
                'message': 'Maestro Creado exitosamente'
            },201
        except Exception as error:
            return {
                'message': 'Error al crear el maestro',
                'content' : error.args
            }
        


class UnMaestroController(Resource):
    def get (self,id):
        query: Query=conexion.session.query(Maestro)
        Maestro_encontrado=query.filter_by(id=id).first()
        dto = MaestroDto()
        resultado=dto.dump(Maestro_encontrado)

        if resultado:
            return{
                'message': resultado
             }
        else:
            return{
                'message': 'Nivel no encontrado'
             }