from controllers import *

def registrar_receta_ruta(api):
    api.add_resource(RecetasResource,'/recetas')
    api.add_resource(RecetaPaginacionResource,'/paginacion_receta')
    api.add_resource(RecetaResource,'/receta/<int:id>')