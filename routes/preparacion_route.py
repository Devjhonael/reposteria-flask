from controllers import PreparacionesResource,PreparacionResource


def registrar_preparacion_ruta(api):
    api.add_resource(PreparacionesResource,'/preparaciones')
    api.add_resource(PreparacionResource,'/preparacion/<int:id>')