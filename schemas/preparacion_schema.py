from extends import ma
from models import PreparacionModel

class PreparacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=PreparacionModel
        load_instance=True
        include_fk=True

preparacion_schema=PreparacionSchema()
preparaciones_schema=PreparacionSchema(many=True)