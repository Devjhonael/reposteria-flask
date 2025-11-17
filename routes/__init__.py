from .ingrediente_route import registrar_ingrediente_ruta
from .receta_route import registrar_receta_ruta
from .receta_ingrediente_route import registrar_receta_ingrediente_ruta
from .preparacion_route import registrar_preparacion_ruta

def registrar_todas_rutas(api):
    registrar_ingrediente_ruta(api)
    registrar_receta_ruta(api)
    registrar_receta_ingrediente_ruta(api)
    registrar_preparacion_ruta(api)