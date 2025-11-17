from extends import ma
from models import RecetaModel,EnumPorcion
from marshmallow import fields, ValidationError

# Campo custom para convertir Enum <-> string
class EnumField(fields.Field):
    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        return value.value if value else None

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return self.enum(value)
        except ValueError:
            raise ValidationError(f"Valor inválido. Debe ser uno de {[e.value for e in self.enum]}")

# Acción - Función	- Entrada - Salida
# dump() - Serializar - Instancia - dict / JSON
# load() -Deserializar - dict / JSON - Instancia / dict
# load(..., partial=True, instance=...) - Actualizar parcialmente - dict parcial - Instancia modificad

class RecetaSchema(ma.SQLAlchemyAutoSchema):
    recetaPorcion = EnumField(EnumPorcion, required=True)
    class Meta:
        model=RecetaModel
        load_instance=True
        include_fk=True



class RecetaPaginacionSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model=RecetaModel
        load_instance=True
    page=fields.Int(required=True)
    perPage=fields.Int(required=True)

receta_schema=RecetaSchema()
recetas_schema=RecetaSchema(many=True)

receta_paginacion_schema=RecetaPaginacionSchema()
recetas_paginacion_schema=RecetaPaginacionSchema(many=True)