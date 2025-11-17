from flask import request
from flask_restful import Resource
from extends import db
from models import RecetaModel,PreparacionModel
from schemas import preparacion_schema
from marshmallow import ValidationError


class PreparacionesResource(Resource):
    def post(self):
        error = None
        try:
            preparacion = preparacion_schema.load(request.json)
            buscar_receta = db.session.query(RecetaModel).filter_by(
                recetaId=preparacion.recetas_id).first()
            if buscar_receta is None:
                raise ValidationError("Receta no existe")
            db.session.add(preparacion)
            db.session.commit()
            return {
                "content": preparacion_schema.dump(preparacion),
                "message": "Preparacion registrada exitosamente"
            }, 201
        except ValidationError as err:
            error = err
            return {
                "message": err.messages
            }, 500
        except Exception as err:
            error = err
            return {
                "message": err.args[0]
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()


#? es no es tan recomendable por que preparacion y me diga la receta no ayuda mucho es mejor hacer que la busquede una receta me diga todas sus preparaciones no crees?
class PreparacionResource(Resource):
    def get(self,id):
        preparacion=db.session.query(PreparacionModel).filter_by(preparacionId=id).first()
        print(preparacion.receta)
        try:
            return {
                "content":"",
                "message":"Preparacion ID"
            }
        except ValidationError as err:
            return {
                "message":err.messages
            },500
        finally:
            db.session.close()
