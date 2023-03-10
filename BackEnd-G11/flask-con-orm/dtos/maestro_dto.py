from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.maestro_model import Maestro

class MaestroDto(SQLAlchemyAutoSchema):
    class Meta:
        # Model > para indicar que modelo tiene que utilizar para poder hader el mapeo y validaciones de los atributos
        model =  Maestro