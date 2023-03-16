from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Query
from models.tarea_model import Tarea
from db import conexion
from dtos.tarea_dto import TareaDto, TareaFiltros


#import datetime


class TareasController(Resource):
    @jwt_required()
    def post(self):
        usuario_id= get_jwt_identity()
        data= request.json
        dto= TareaDto()
        try:
            data_validada= dto.load(data)
            nueva_tarea=Tarea(**data_validada, usuarioId= usuario_id)
            conexion.session.add(nueva_tarea)
            conexion.session.commit()
            return{
                 'message': 'Se agrego la tarea exitosamente'
                
            },201
        except Exception as error:
            return {
                'message': 'Error al hacer el login',
                'content': error.args
            }

        pass
    
    @jwt_required()
    def get(self):
        

        usuario_id= get_jwt_identity()
        query: Query= conexion.session.query(Tarea)
        data = query.filter_by(usuarioId=usuario_id).all()
        dto=TareaDto()
        resultado= dto.dump(data,many=True)
        return{
            'content': resultado
        }
        
        #query: Query = conexion.session.query(Tarea)
        #resultado = query.all()
        #dto = TareaDto()
        #tareas = []
        #for tarea in resultado:
        #    tareas.append({
        #         'Id': tarea.id,
        #         'nombre': tarea.nombre,
        #         'descripcion': tarea.descripcion,
        #         'fecha_vencimiento': tarea.fechaVencimiento.strftime('%Y-%m-%d %H:%M:%S'),
        #         'estado': tarea.estado.name,
        #         'Usuario_id': tarea.usuarioId                           
        #     })
        #     
        #return {
        #    'content': tareas
        #}


class TareaController(Resource):
    @jwt_required()
    
    def get(self):
        usuario_id= get_jwt_identity()
        query_params=request.args.to_dict().copy()
        query_params['usuarioId']= usuario_id
        try:
            dto=TareaFiltros()
            parametros = dto.load(query_params)
            query:Query= conexion.session.query(Tarea)
            data= query.filter_by(**parametros).all()
            dto=TareaDto()
            resultado= dto.dump(data, many=True)
            return{
                'content':resultado
            }

        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content': e.args
            }

        #nombre = request.args.get('nombre')
        #estado = request.args.get('estado')

        ##tareas = []
        #query: Query = conexion.session.query(Tarea)
        #if nombre and estado:
        #    resultado= query.filter_by(nombre=nombre)
        #    resultado=  resultado.filter_by(estado=estado)
        #    
        #elif nombre:
        #    resultado= query.filter_by(nombre=nombre)
        #    
        #elif estado:
        #    resultado= query.filter_by(estado=estado)
        #else:
        #    return {
        #        'message': 'No se enviaron los argumentos '                
        #    }        
       
        #for tarea in resultado:
        #    tareas.append({
        #            'Id': tarea.id,
        #            'nombre': tarea.nombre,
        #            'descripcion': tarea.descripcion,
        #            'fecha_vencimiento': tarea.fechaVencimiento.strftime('%Y-%m-%d %H:%M:%S'),
        #            'estado': tarea.estado.name,
        #            'Usuario_id': tarea.usuarioId                           
        #    })

        #if len(tareas) !=0:
        #    return {
        #        'content': tareas
        #    }
        #else:
        #    
        #    return {
        #        'message': 'No se encontraron coincidencias '                
        #    }
        

        
