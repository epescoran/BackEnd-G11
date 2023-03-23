from flask_restful import Resource, request
from bcrypt import gensalt, hashpw
from dtos.usuario_dto import UsuarioDto
from db import conexion
from models.usuario_model import Usuario
from utils.enviar_correo import enviar_correo



class RegistroController(Resource):
    def post(self):
        data= request.json
        try:
            dto=UsuarioDto()
            data_serializada = dto.load(data)
            # hash de la contraseña
            salt = gensalt()
            password = bytes(data_serializada.get('password'),'utf-8')
            hashed_password = hashpw(password,salt).decode('utf-8')
            data_serializada['password']=hashed_password
            nuevo_usuario = Usuario(**data_serializada)
            conexion.session.add(nuevo_usuario)
            conexion.session.commit()

            enviar_correo(nuevo_usuario.correo, 'Bienvenido a LibreriAPP','''Bienvenido a esta nueva plataforma.
            Donde podras encontrar todo lonecesario para tus utiles de escritorio''')

            return{
                'message':'Usuario creado exitosamente'
            }
        except Exception as error:
            conexion.session.rollback()
            return{
                'message':'Error al registrar',
                'content': error.args
            }