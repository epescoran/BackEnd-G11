from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto
from os import path
from werkzeug.utils import secure_filename
from uuid import uuid4

import os

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()
        imagen=request.files.get('imagen')
        mimetype_validos = 'image/'
        CONTENIDO_MAXIMO = 10 * 1024*1024
        try:
            # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
            if imagen is None: #not request.files.get('imagen'):
                raise Exception('No se encuentra la variable imagen')
            # TODO: validar que solo sean imagenes
            if  mimetype_validos not in imagen.mimetype:
                raise Exception('El archivo no es un archivo valido')
            imagen = request.files.get('imagen')
            # TODO: no recibir imagenes que pesen mas de 10Mb
            if imagen.content_length>10:
                raise Exception('El archivo supera los 10Mb')

            # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
            nombre_seguro =secure_filename(uuid4().hex+'-'+imagen.filename)
          
            
            

            data['imagen'] = nombre_seguro
        
            dto = ProductoDto()
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            conexion.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', data['imagen']))

            conexion.session.commit()

            return {
                'message': 'Producto creado exitosamente'
                }
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        
    def get(self):
        resultado = conexion.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }