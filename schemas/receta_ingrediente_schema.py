from extends import ma
from models import RecetaIngredienteModel,IngredienteModel
from marshmallow import fields


class IngredienteItemSchema(ma.Schema):
    ingrediente_id = fields.Integer(required=True)
    cantidad = fields.String(required=True)


class RecetaIngredienteSchema(ma.SQLAlchemyAutoSchema):
    ingredientes_id = fields.List(fields.Nested(
        IngredienteItemSchema), required=True)

    class Meta:
        model = RecetaIngredienteModel
        load_instance = True
        include_fk = True
        exclude = ("cantidad",)


class RecetasIngredientesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RecetaIngredienteModel
        load_instance = True
        include_fk = True





class IngredienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IngredienteModel
        load_instance = True
        include_fk = False

class RecetaIngrediente2Schema(ma.SQLAlchemyAutoSchema):
    ingrediente = fields.Nested(IngredienteSchema)

    class Meta:
        model = RecetaIngredienteModel
        load_instance = True
        include_fk = True
        exclude = ("ingredientes_id", )  # Porque ya mandas el ingrediente anidado


receta_ingrediente_schema = RecetaIngredienteSchema()
recetas_ingrediente_schema = RecetaIngredienteSchema(many=True)


recetas_ingredientes_schemas=RecetasIngredientesSchema(many=True)
receta_ingrediente2=RecetaIngrediente2Schema(many=True)