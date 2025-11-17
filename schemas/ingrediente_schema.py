from extends import ma
from models import IngredienteModel
from marshmallow import fields,validate
from utils.regex import patron_nombre

class IngredienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta: #para la configuracion del esquema
        model=IngredienteModel #modelo con que va trabajar
        load_instance=True #al usar schema.load(data) Marshmallow intentará construir y devolver una instancia del modelo SQLAlchemy (Usuario(...)) en vez de devolver solo un dict.
        include_fk=True #add las claves foraneas
        # exclude = ("ingredienteId",)#cuando usemos el dump que es para sacar los datos no va coger este dato si no lo va obviar

    ingredienteNombre=fields.String(required=True,validate=[
            validate.Regexp(
                patron_nombre,
                error="El nombre solo puede contener letras y espacios."
            ),
            validate.Length(min=2, max=50)
        ]
    )
ingrediente_schema=IngredienteSchema()
ingredientes_schema=IngredienteSchema(many=True)

# podemos o muchos esquemas x ejemplo si el get queremos recibir todos los atributos ypost solanente queremos mostrar todos menos 1 atributo entonces debemos crear otro esquema recuerda que el dump es el que puede excluir lo que desea mostrar