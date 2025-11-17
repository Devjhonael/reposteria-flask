from flask import request
from flask_restful import Resource
from extends import db
from models import RecetaModel, IngredienteModel
from schemas import recetas_schema, receta_schema, recetas_paginacion_schema, receta_paginacion_schema, preparaciones_schema,receta_ingrediente2
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from math import ceil


class RecetasResource(Resource):
    def get(self):
        try:
            recetas = db.session.query(RecetaModel).all()
            if len(recetas) == 0:
                raise ValidationError("No hay recetas")
            return {
                "content": recetas_schema.dump(recetas),
                "message": "Lista de recetas"
            }
        except ValidationError as err:
            return {
                "message": err.messages
            }
        finally:
            db.session.close()

    def post(self):
        error = None
        try:
            receta = receta_schema.load(request.json)
            db.session.add(receta)
            db.session.commit()
            return {
                "content": receta_schema.dump(receta),
                "message": "Creado Exitosamente"
            }, 201
        except ValidationError as err:
            error = err
            return {
                "message": err.messages,
            }, 500
        except IntegrityError as err:
            error = err
            return {
                "message": "no se aceptan recetas repetidos"
            }, 500
        except Exception as err:
            error = err.args[0]
            return {
                "message": error
            }, 500
        finally:
            if error is not None:
                db.session.rollback()
            db.session.close()

# tiene sentido escoger una receta y que esta me muestre todos sus ingredientes y preparacion


class RecetaResource(Resource):
    def get(self, id):
        try:
            # gracias a ello puedo tener una lista de preparaciones asociadas dentro de recetas (al parecer siempre funciona con el recetas filter_by)
            # si existe la receta puedo mandar las preparaciones y los ingrediente pero
            # las preparaciones se estan guardando en receta.preparaciones
            receta = db.session.query(
                RecetaModel).filter_by(recetaId=id).first()
            if receta is None:
                raise ValidationError("Receta no existe")
            # me trae todas los ingredientes que estan asociados a esa receta
            # print(receta.recetas_ingredientes)

            # esto es tan sabio que solamente me trae todas las preparaciones que estan asosciados a la receta que hemos buscado
            # print(receta.preparaciones)

            # print(receta.recetas_ingredientes[1].__dict__['ingredientes_id'])
            # como estoy en la tabla recetas_ingredientes entonces con ese id de ingredientes tengo que entrar a la tabla ingredientes y sacar todos los ingredientes en funcion a lo que tengo ojo de recetas_ingredientes donde esta el id
            ingrediente_modelo = []
            for ingrediente in receta.recetas_ingredientes:
                ingrediente_nuevo = db.session.query(IngredienteModel).filter_by(
                    ingredienteId=ingrediente.ingredientes_id).first()
                ingrediente_modelo.append(ingrediente_nuevo)

            return {
                "content": {
                    "receta": receta_schema.dump(receta),
                    "ingredientes": receta_ingrediente2.dump(receta.recetas_ingredientes),
                    "preparaciones": preparaciones_schema.dump(receta.preparaciones),
                },
                "message": "Receta Encontrada"
            }, 200

        except ValidationError as err:
            return {
                "message": err.messages
            }, 500
        except Exception as err:
            return {
                "message": err.args[0]
            }, 500
        finally:
            db.session.close()


class RecetaPaginacionResource(Resource):
    def get(self):
        try:
            data = receta_paginacion_schema.dump(request.args)

            print(data)
            page = data.get("page")
            perPage = data.get("perPage")
            limit = perPage
            offset = (page-1)*limit

            totalRecetas = db.session.query(
                RecetaModel).count()

            itemsPorPagina = perPage if totalRecetas >= perPage else None
            totalPaginas = ceil(totalRecetas/itemsPorPagina)
            if page > 1:
                paginaPrevia = page-1 if page <= totalPaginas else None
            else:
                paginaPrevia = None
            if totalPaginas > 1:
                paginaSiguiente = page+1 if page < totalPaginas else None
            else:
                paginaSiguiente = None

            receta_pagina = db.session.query(RecetaModel).limit(
                limit).offset(offset).all()

            return {
                "content": recetas_paginacion_schema.dump(receta_pagina),
                "paginacion": {
                    "total": totalRecetas,
                    "perPages": itemsPorPagina,
                    "paginaPrevia": paginaPrevia,
                    "paginaSiguiente": paginaSiguiente,
                    "totalPaginas": totalPaginas
                }
            }
        except Exception as err:
            return {
                "message": "Error inesperadoss"
            }, 500
        finally:
            db.session.close()
