from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion

from controllers.nivel_controller import NivelController, UnNivelController

from controllers.maestro_controller import MaestroController, UnMaestroController


load_dotenv()

#print(environ)

app= Flask(__name__)
#print (app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


Flask_api = Api(app=app)
#conexion = SQLAlchemy(app=app)
# Si quiero crear mi conexion en otro archivo e inicialiar la coniguracion de mi conexion tengo que utilizar el meotodo init_app y es aca donde le pasare el parametro de mi instancia de la clase Flask
conexion.init_app(app)
Migrate(app=app, db=conexion)

#Defino las rutas de mi API
Flask_api.add_resource(NivelController, '/nivel')
Flask_api.add_resource(UnNivelController, '/nivel/<id>')

Flask_api.add_resource(MaestroController, '/maestro')
Flask_api.add_resource(UnMaestroController, '/maestro/<id>')

if __name__=='__main__':
    app.run(debug=True)
