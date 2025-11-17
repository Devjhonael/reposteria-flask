from flask import request
from flask_restful import Resource
from extends import db
from models import IngredienteModel
from schemas import ingrediente_schema, ingredientes_schema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError


class IngredientesResource(Resource):
    def get(self):
        try:
            ingredientes = db.session.query(IngredienteModel).all()
            if len(ingredientes) == 0:
                raise Exception("No hay ingredientes")
            return {
                "content": ingredientes_schema.dump(ingredientes),
                "message": "lista de ingredientes"
            }, 200

        except Exception as err:
            return {
                "message": err.args[0]
            }, 500
        finally:
            db.session.close()

    def post(self):
        error = None
        try:
            ingrediente = ingrediente_schema.load(request.json)
            db.session.add(ingrediente)
            db.session.commit()
            return {
                "content": ingrediente_schema.dump(ingrediente),
                "message": "Creado Exitosamente"
            }, 201
        except ValidationError as err:
            error = err
            return {
                "message": err.messages,
            }, 500
        except IntegrityError as err:
            error = err.args[0]
            return {
                "message": "no se aceptan datos repetidos"
            }, 500
        except Exception as err:
            error = err
            return {
                "message": "Error Inesperado"
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()


class IngredienteResource(Resource):
    def get(self, id):
        try:
            ingrediente_encontrado = db.session.query(
                IngredienteModel).filter_by(ingredienteId=id).first()

            if ingrediente_encontrado is None:
                raise Exception('no existe el ingrediente')
            return {
                "content": ingrediente_schema.dump(ingrediente_encontrado),
                "message": "Ingrediente Encontrado"
            }, 200

        except Exception as err:
            return {
                "message": err.args[0]
            }, 500
        finally:
            db.session.close()

    def put(self, id):
        error = None
        try:
            ingrediente_encontrado = db.session.query(
                IngredienteModel).filter_by(ingredienteId=id).first()

            if ingrediente_encontrado is None:
                raise ValidationError("No existe ingrediente")

            if ingrediente_encontrado.ingredienteNombre == request.json.get('ingredienteNombre'):
                raise ValidationError("Ingrediente se repiten")
            data_actualizado = ingrediente_schema.load(
                request.json, instance=ingrediente_encontrado, partial=True)
            db.session.commit()

            return {
                "content": ingrediente_schema.dump(data_actualizado),
                "message": "Ingrediente Actualizado"
            }
        except IntegrityError as err:
            error = err.args[0]
            return {
                "message": "Ingrediente repetido"
            }
        except ValidationError as err:
            error = err
            return {
                "message": err.messages
            }
        except Exception as err:
            error = err.args[0]
            return {
                "message": error
            }
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()

    def delete(self, id):
        error = None
        try:
            ingrediente_encontrado = db.session.query(
                IngredienteModel).filter_by(ingredienteId=id).first()
            if ingrediente_encontrado is None:
                raise ValidationError("Ingrediente no Existe")
            db.session.delete(ingrediente_encontrado)
            db.session.commit()
            return {
                "message": "Eliminado"
            }, 204
        except ValidationError as err:
            error = err
            return {
                "message": err.messages
            }, 500
        except Exception as err:
            error = err
            return {
                "message": "Error Inesperado"
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()


class BuscarIngredienteResource(Resource):
    def get(self):

        try:
            buscar = ingrediente_schema.dump(request.args)
            lista_ingredientes = db.session.query(IngredienteModel).filter(
                IngredienteModel.ingredienteNombre.like('%{}%'.format(buscar['ingredienteNombre']))).all()
            if len(lista_ingredientes) == 0:
                raise ValidationError("No hay ingrediente en la lista")
            return {
                "content": ingredientes_schema.dump(lista_ingredientes),
                "message": "lista de coincidencia de ingredientes"
            }
        except ValidationError as err:
            return {
                "message":err.messages
            },500
        finally:
            db.session.close()
