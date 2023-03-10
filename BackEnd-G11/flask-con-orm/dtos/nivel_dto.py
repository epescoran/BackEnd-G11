from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.nivel_model import Nivel

class NivelDto(SQLAlchemyAutoSchema):
    class Meta:
        # Model > para indicar que modelo tiene que utilizar para poder hader el mapeo y validaciones de los atributos
        model = Nivel