from extends import db
from sqlalchemy import Column,Integer,String,orm,ForeignKey

class RecetaIngredienteModel(db.Model):
    __tablename__='recetas_ingredientes'
    recetaIngredienteId=Column('id',Integer ,primary_key=True,autoincrement=True,nullable=False,unique=True)
    cantidad=Column('cantidad',String(length=50),nullable=False)

    recetas_id=Column('recetas_id',Integer,ForeignKey('recetas.id',ondelete='RESTRICT'),nullable=False)
    ingredientes_id=Column('ingredientes_id',Integer,ForeignKey('ingredientes.id',ondelete='RESTRICT'),nullable=False)

    ingrediente = orm.relationship("IngredienteModel",backref="ingredientes")