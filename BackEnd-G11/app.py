from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from Controllers.usuario_controller import UsuariosController, LoginController, PerfilController
from Controllers.tarea_controller import TareasController, TareaController


from db import conexion


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:a123a456a7890A@localhost:5432/tareas'
app.config['JWT_SECRET_KEY']='ultrasupersecreto'
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=1,minutes=10)
api = Api(app)

conexion.init_app(app)
Migrate(app= app, db=conexion)
JWTManager(app)

api.add_resource(UsuariosController,'/registro')
api.add_resource(LoginController,'/login')
api.add_resource(PerfilController,'/perfil')
api.add_resource(TareasController,'/tareas')
api.add_resource(TareaController,'/tarea')

if __name__=='__main__':
    app.run(debug=True)
