from extends import db
from sqlalchemy import Column,Integer,String

class IngredienteModel(db.Model):
    __tablename__="ingredientes"
    ingredienteId=Column('id',Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    ingredienteNombre=Column('nombre',String(length=50),unique=True)