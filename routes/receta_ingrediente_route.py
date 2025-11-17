from controllers import RecetaIngredienteResource

def registrar_receta_ingrediente_ruta(api):
    api.add_resource(RecetaIngredienteResource,'/receta_ingrediente')