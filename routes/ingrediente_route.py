from controllers import IngredientesResource,IngredienteResource,BuscarIngredienteResource

def registrar_ingrediente_ruta(api):
    api.add_resource(IngredientesResource,'/ingredientes')
    api.add_resource(IngredienteResource,'/ingrediente/<int:id>')
    api.add_resource(BuscarIngredienteResource,'/buscar_ingrediente')