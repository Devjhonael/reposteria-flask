from extends import db
from sqlalchemy import Column,Integer,String,orm,Enum as SqlEnum
from enum import Enum as PyEnum

class EnumPorcion(PyEnum):
    FAMILIAR='familiar'
    MEDIANO='mediano'
    PERSONAL='personal'

class RecetaModel(db.Model):
    __tablename__="recetas"
    recetaId=Column('id',Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    recetaNombre=Column('nombre',String(length=50),unique=True)
    recetaPorcion=Column('porcion',SqlEnum(EnumPorcion))

# en el padre creo un attributo virtual para que jale a Preparacio 
    # el atributo preparaciones se crea en la tabla receta entonces gracias a ellos desde mi recetay ese atributo podemos acceder a todas las preparaciones
    # y cuando de la tabla preparaciones quiera acceder a la tabla de recetas entonces usamoremos desde la tabla preparaciones ese atributos que permite acceder a todas las recetas backref= osea receta
    preparaciones=orm.relationship('PreparacionModel',backref='receta',lazy=True )
    recetas_ingredientes=orm.relationship('RecetaIngredienteModel',backref='receta_ingrediente',lazy=True)