from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto


class NivelController(Resource):
    def get(self):
        query : Query = conexion.session.query(Nivel)
        query.all()
        resultado = query.all()
        #print (resultado[0].numero)
        #print (resultado[0].descripcion)
        dto= NivelDto()
        #dump > es eun metodo en el cual le paso la/las instancias que quiero conververit a tipo de datos genericos Si se le pasa mas de una instancia osea una lista de instancias se le tiene que adicionar el parametro many=True para indicar que lo tendra que interar
        niveles =dto.dump(resultado, many=True)

        #for nivel in resultado:
        #    niveles.append({
        #        'id': nivel.id,
        #        'numero': nivel.numero,
        #        'descripcion': nivel.descripcion
        #    })

        return{
            'content': niveles
        }

    def post(self):
        data = request.json
        dto = NivelDto()
        # load > aca le pasamos un diccionario y lo convertira y validara si toda la informacion es correcta, si no lo es, emitira un error y si la informacion esta bien, entonces deovolverar un diccionario con la data correcta
        try:
            data_validada= dto.load(data)
            print (data_validada)
        

            nuevo_nivel=Nivel(numero=data_validada.get('numero'), descripcion = data_validada.get ('descripcion'))
            conexion.session.add(nuevo_nivel)
            conexion.session.commit()
            return{
                'message': 'Nivel Creado exitosamente'
            },201
        except Exception as error:
            return {
                'message': 'Error al crear el nivel',
                'content' : error.args
            }
        


class UnNivelController(Resource):
    def get (self,id):
        query: Query=conexion.session.query(Nivel)
        nivel_encontrado=query.filter_by(id=id).first()
        dto = NivelDto()
        resultado=dto.dump(nivel_encontrado)

        if resultado:
            return{
                'message': resultado
             }
        else:
            return{
                'message': 'Nivel no encontrado'
             }