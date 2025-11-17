from extends import db
from sqlalchemy import Column,Integer,Text,ForeignKey

class PreparacionModel(db.Model):
    __tablename__='preparaciones'
    preparacionId=Column('id',Integer ,primary_key=True,autoincrement=True,nullable=False,unique=True)
    preparacionOrden=Column('orden',Integer,default=1)
    preparacionDescripcion=Column('descripcion',Text)
    
    recetas_id=Column('recetas_id',Integer,ForeignKey('recetas.id',ondelete='RESTRICT'))