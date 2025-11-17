# http://127.0.0.1:5000/api/docs/#/ingrediente/%2Fingrediente%2F%3Aid
# ahi esta mi documentacion

{
    # esto es .json por lo cual hay que cambiar True a true minuscula
  "swagger": "2.0",
  "info": {
    "description":"Mi primera Api usando base de datos",#add para la descr
    "version": "1.0",
    "title": "Api_reposteria",
    "contact": {
      "email":"mc.jhonael@gmail.com",#add campo email
      "name":"jhonatan dev" #add campo nombre
    }
  },
  "host": "127.0.0.1:5000",#host peladito sin /
  "basePath": "/",#ruta inicial
  "securityDefinitions": {},
  "schemes": [
    "https",
    "http"#add este protocolo mas
  ],
  "consumes": [
    "application/json" #que consume osea datos en json
  ],
  "produces": [
    "application/json" #que produce lo mismo
  ],
  "paths": {
    "/ingredientes": {
      "post": {
        "summary": "metodo para crear un ingrediente",#conciso directo de lo que hace
        "description":"como deber crear un ingrediente",#un poco mas amplio
        "tags": [#tags para agregar en bloques cada uno
          "ingrediente" 
        ],
        "operationId": "/ingredientes",
        "deprecated": False,#para True lo tacha y le dice k ya no funciona este endpoint
        "produces": [
          "application/json" #produce un json
        ],
        "parameters": [
          {
            "name": "Body",
            "in": "body",
            "required": True,#el dato tiene que ser obligatorio
            "description": "informacion para ingresar el nuevo ingrediente",
            "schema": {
              "$ref": "#/definitions/~1ingredientesrequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      },
      "get": {
        "summary": "/ingredientes",
        "tags": [
          "ingrediente"
        ],
        "operationId": "Get/ingredientes",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/ingrediente/{id}": { #hay que colocar id y luego decirle los parametros que necesitara y tipo de dato etc
      "get": {
        "summary": "/ingrediente/:id",
        "tags": [
          "ingrediente"
        ],
        "operationId": "/ingrediente/:id",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [{"name":"id","in":"path","required":True,"type":"integer", "format":"int64"}],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      },
      "put": {
        "summary": "/ingrediente/:id",
        "tags": [
          "ingrediente"
        ],
        "operationId": "Put/ingrediente/:id",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          { #para put recibe el id de los params y tbm del body
            "name": "id",
            "in": "path",
            "required": True,
            "type": "integer",
            "format": "int64"
          },
          {
            "name": "Body",
            "in": "body",
            "required": True,
            "description": "",
            "schema": {
              "$ref": "#/definitions/~1ingrediente~1%3Aidrequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      },
      "delete": {
        "summary": "/ingrediente/:id1",
        "tags": [
          "ingrediente"
        ],
        "operationId": "/ingrediente/:id1",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [{"name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "format": "int64"
                        }],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/buscar_ingrediente": {
      "get": {
        "summary": "/buscar_ingrediente",
        "tags": [
          "ingrediente"
        ],
        "operationId": "/buscar_ingrediente",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "ingredienteNombre",
            "in": "query",
            "required": True,
            "type": "string",
            "description": ""
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/recetas": {
      "post": {
        "summary": "/recetas",
        "tags": [
          "receta"
        ],
        "operationId": "/recetas",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "Body",
            "in": "body",
            "required": True,
            "description": "",
            "schema": {
              "$ref": "#/definitions/~1recetasrequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      },
      "get": {
        "summary": "/recetas",
        "tags": [
          "receta"
        ],
        "operationId": "Get/recetas",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/paginacion_receta": {
      "get": {
        "summary": "/paginacion_receta",
        "tags": [
          "receta"
        ],
        "operationId": "/paginacion_receta",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "required": True,
            "type": "integer",
            "format": "int32",
            "description": ""
          },
          {
            "name": "perPage",
            "in": "query",
            "required": True,
            "type": "integer",
            "format": "int32",
            "description": ""
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/receta/{id}": {
      "get": {
        "summary": "/receta/:id",
        "tags": [
          "receta"
        ],
        "operationId": "/receta/:id",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [{
            "name": "id",
            "in": "path",
            "required": True,
            "type": "integer",
            "format": "int64"
          },],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/receta_ingrediente": {
      "post": {
        "summary": "/receta_ingrediente",
        "tags": [
          "receta_ingrediente"
        ],
        "operationId": "/receta_ingrediente",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "Body",
            "in": "body",
            "required": True,
            "description": "",
            "schema": {
              "$ref": "#/definitions/~1receta_ingrediente_request"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/preparaciones": {
      "post": {
        "summary": "/preparaciones",
        "tags": [
          "preparacion"
        ],
        "operationId": "/preparaciones",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "Body",
            "in": "body",
            "required": True,
            "description": "",
            "schema": {
              "$ref": "#/definitions/~1preparacionesrequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    },
    "/preparacion/{id}": {
      "get": {
        "summary": "/preparacion/:id",
        "tags": [
          "preparacion"
        ],
        "operationId": "/preparacion/:id",
        "deprecated": False,
        "produces": [
          "application/json"
        ],
        "parameters": [{
            "name": "id",
            "in": "path",
            "required": True,
            "type": "integer",
            "format": "int64"
          },],
        "responses": {
          "200": {
            "description": "",
            "headers": {}
          }
        }
      }
    }
  },
  "definitions": {
    "/ingredientesrequest": {
      "title": "/ingredientesrequest",
      "example": {
        "ingredienteNombre": ""
      },
      "type": "object",
      "properties": {
        "ingredienteNombre": {
          "type": "string"
        }
      },
      "required": [
        "ingredienteNombre"
      ]
    },
    "/ingrediente/:idrequest": {
      "title": "/ingrediente/:idrequest",
      "example": {
        "ingredienteNombre": ""
      },
      "type": "object",
      "properties": {
        "ingredienteNombre": {
          "type": "string"
        }
      },
      "required": [
        "ingredienteNombre"
      ]
    },
    "/recetasrequest": {
      "title": "/recetasrequest",
      "example": {
        "recetaNombre": "",
        "recetaPorcion": "mediano"
      },
      "type": "object",
      "properties": {
        "recetaNombre": {
          "type": "string"
        },
        "recetaPorcion": {
          "type": "string"
        }
      },
      "required": [
        "recetaNombre",
        "recetaPorcion"
      ]
    },
    "/receta_ingrediente_request": {
      "title": "/receta_ingrediente_request",
      "example": {
        "recetas_id": 0,
        "ingredientes_id": [
          {
            "ingrediente_id": 0,
            "cantidad": ""
          },
        ]
      },
      "type": "object",
      "properties": {
        "recetas_id": {
          "type": "integer",
          "format": "int32"
        },
        "ingredientes_id": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IngredientesId"
          }
        }
      },
      "required": [
        "recetas_id",
        "ingredientes_id"
      ]
    },
    "IngredientesId": {
      "title": "IngredientesId",
      "example": {
        "ingrediente_id": 0,
        "cantidad": ""
      },
      "type": "object",
      "properties": {
        "ingrediente_id": {
          "type": "integer",
          "format": "int32"
        },
        "cantidad": {
          "type": "string"
        }
      },
      "required": [
        "ingrediente_id",
        "cantidad"
      ]
    },
    "/preparacionesrequest": {
      "title": "/preparacionesrequest",
      "example": {
        "preparacionOrden": 0,
        "preparacionDescripcion": "",
        "recetas_id": 0
      },
      "type": "object",
      "properties": {
        "preparacionOrden": {
          "type": "integer",
          "format": "int32"
        },
        "preparacionDescripcion": {
          "type": "string"
        },
        "recetas_id": {
          "type": "integer",
          "format": "int32"
        }
      },
      "required": [
        "preparacionOrden",
        "preparacionDescripcion",
        "recetas_id"
      ]
    }
  },
  "tags": [
    {
      "name": "ingrediente"
    },
    {
      "name": "receta"
    },
    {
      "name": "receta_ingrediente"
    },
    {
      "name": "preparacion"
    }
  ]
}