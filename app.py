from flask import Flask
from config.config_db import Config
from extends import db,migrate,ma,api,cors
from flask_swagger_ui import get_swaggerui_blueprint

from models import *
from routes import *


# CONFIGURACION SWAGGER FLASK

# esta varaible se usa para indicar en que ruta(endpoint) se encontrara la documentacion
SWAGGER_URL='/api/docs'

# indicar la ubicacion del archivo swagger.json
API_URL="/static/swagger.json"

swagger_blueprint= get_swaggerui_blueprint(base_url=SWAGGER_URL,api_url=API_URL,config={
    'app_name':'Resposteria Flask - Documentacion Swagger'
})
# FIN DE LA CONFIGURACION

app=Flask(__name__)
app.config.from_object(Config)
# LOS BLUEPRINTS SIRVEN PARA REGISTRAR EN EL CASO QUE NOSOTROS TENGAMOS UN PROYECTO INTERNO Y QUERRAMOS AGREGARLO AL PROYECTO PRINCIPAL DE FLASK
app.register_blueprint(swagger_blueprint)

# origin sirve para indicar que dominion pueden acceder a mi API, x defecto * permite todos los origins 1 o muchos
#methods=sirve para indicar que metodos pueden consultarse a la API, x defecto su valor es [GET,HEAD,POST,OPTIONS,PUT,PATH,DELETE]
# headers = sirve para indicar que cabeceras pueden enviarse x defecto es todos las cabeceras
cors.init_app(app, origins= "*",methods= ["GET", "POST", "PUT", "DELETE"], 
        allow_headers=["Content-Type"]
    
)  
db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)

# aqui falta colocar las rutas antes de incializar
registrar_todas_rutas(api)
api.init_app(app)

@app.route('/',methods=['GET','POST'])
def home():
    return "hola desde la pagina de Home"

if __name__ == '__main__':
    app.run(port=5000,debug=True)