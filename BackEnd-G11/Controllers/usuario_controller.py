from flask_restful import Resource, request
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm import Query
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
from dtos.usuario_dto import UsuarioDto, LoginDto
from models.usuario_model import Usuario
from db import conexion

class UsuariosController(Resource):
    def post(self):
        data= request.json
        dto= UsuarioDto()
        try:
            data_validada= dto.load(data)
            salt = gensalt( rounds=10)
            password = bytes(data_validada.get('password'),'utf-8')
            password_hashed=hashpw(password, salt)
            password_hashed_str= password_hashed.decode('utf-8')
            nuevo_Usuario=Usuario(correo= data_validada.get('correo'), password= password_hashed_str, nombre= data_validada.get('nombre'), apellido= data_validada.get('apellido'))
            conexion.session.add(nuevo_Usuario)
            conexion.session.commit()
            return{
                'message':'Usuario creado exitosamente'
            }
        except Exception as error:
            return{
                'message': 'Error al ingresar el usuario',
                'content': error.args
            }



class LoginController(Resource):
    def post(self):
        data = request.json
        dto = LoginDto()
        print(data)
        try:
            data_validada = dto.load(data)
            # Buscar el usuario por ese correo
            # SELECT * FROM usuarios WHERE correo = '....';
            query:Query = conexion.session.query(Usuario)
            usuario_encontrado: Usuario | None =  query.filter_by(correo = data_validada.get('correo')).first()
            print(usuario_encontrado)
            if not usuario_encontrado:
                return {
                    'message': 'El usuario no existe'
                }
            # Ahora valido si la contraseña es la correcta
            # Lo convierto a bytes porque asi trabaja la funcion checkpw
            hashed_password = bytes(usuario_encontrado.password,'utf-8')
            password = bytes(data_validada.get('password'), 'utf-8')

            resultado = checkpw(password,hashed_password)

            if resultado:
                token=create_access_token(identity= usuario_encontrado.id)

                return {
                    'message': token
                }
            else:
                return {
                    'message': 'Credenciales incorrectas'
                }

        except Exception as error:
            return {
                'message': 'Error al hacer el login',
                'content': error.args
            }




class PerfilController(Resource):
    #al poner el decorador ahora tiene que ser obligatorio pasar la token
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        id=get_jwt_identity()
        query:Query= conexion.session.query(Usuario)

        usuario_encontrado:Usuario=query.filter_by(id=id).first()
        print(usuario_encontrado)
        dto= UsuarioDto()
        data= dto.dump(usuario_encontrado)
        return {
            'content': data
        }
