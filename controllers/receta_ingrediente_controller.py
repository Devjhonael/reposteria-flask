from flask import request
from flask_restful import Resource
from extends import db
from models import RecetaIngredienteModel, RecetaModel, IngredienteModel
from schemas import receta_ingrediente_schema
from marshmallow import ValidationError

class RecetaIngredienteResource(Resource):
    def post(self):
        error = None
        try:
            receta_ingrediente=receta_ingrediente_schema.load(request.json)
            
            receta_encontrada=db.session.query(RecetaModel).filter_by(recetaId=receta_ingrediente.recetas_id).first()

            if receta_encontrada is None:
                raise ValidationError("no existe receta")
            
            for ingrediente in receta_ingrediente.ingredientes_id:
                ingrediente_encontrado=db.session.query(IngredienteModel).filter_by(ingredienteId=ingrediente.get('ingrediente_id')).first()

                if ingrediente_encontrado is None:  
                    raise ValidationError("No se encuentra el ingrediente")

                nueva_receta_ingrediente=RecetaIngredienteModel(recetas_id=receta_encontrada.recetaId,ingredientes_id=ingrediente_encontrado.ingredienteId,cantidad=ingrediente.get('cantidad'))
                db.session.add(nueva_receta_ingrediente)
            db.session.commit()


            return {
                "message":"Agregado exitosamente"
            },201
        except ValidationError as err:
            error=err
            return {
                "message":err.messages
            },400
        except Exception as err:
            error=err
            return {
                "message":err.args[0]
            },500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()
