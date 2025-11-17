from controllers import *

def registrar_ingrediente_ruta(api):
    api.add_resource(IngredientesResource,'/ingredientes')
    api.add_resource(IngredienteResource,'/ingrediente/<int:id>')
    api.add_resource(BuscarIngredienteResource,'/buscar_ingrediente')