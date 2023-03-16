from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.usuario_model import Usuario
from marshmallow  import Schema , fields


class UsuarioDto(SQLAlchemyAutoSchema):
    #Podemos utilizar la funcion auto_field() para quener un Field de Marshmallow  basado en el modelo que estamos indicando, esto modificara la config del atributo
    #load_only > solamente este campo sera necesario para cuando queramos validad la informacion entrante, pero si queremos devolver informacion este campo se omitira
    password = auto_field(load_only=True)
    class Meta:
        model=Usuario

class LoginDto(Schema):
    # validar el siguiente patro (expresion regular) xxxxxx@xxxxx.xx
    correo = fields.Email(required=True, error_messages= {'required': 'El correo debe ser requerido'})
    password = fields.Str(required=True, error_messages={'required':'El password debe ser requerido'})
        