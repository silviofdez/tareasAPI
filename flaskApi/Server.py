# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "tareasDb"
mongo = PyMongo(app, config_prefix='MONGO')

"""Api rest para tareas, con titulo y descricipio. Titulo es la clave
"""
class Tarea(Resource):
    """Consultas get
    """
    def get(self, titulo=None, descripcion=None):
        data = []

        if titulo:
            tareas_info = mongo.db.tareas.find_one({"titulo": titulo}, {"_id": 0})
            if tareas_info:
                return jsonify({"status": "ok", "data": tareas_info})
            else:
                return {"response": "no hay datos para {}".format(titulo)}

        elif descripcion:
            cursor = mongo.db.tareas.find({"descripcion": descripcion}, {"_id": 0}).limit(10)
            data.append(tareas)

            return jsonify({"descripcion": descripcion, "response": data})

        else:
            cursor = mongo.db.tareas.find({}, {"_id": 0, "update_time": 0}).limit(10)

            for tareas in cursor:
                print tareas
                data.append(tareas)

            return jsonify({"response": data})

    """Inserciones - post
    """
    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            titulo = data.get('titulo')
            if titulo:
                if mongo.db.tareas.find_one({"titulo": titulo}):
                    return {"response": "esa tarea ya existe"}
                else:
                    mongo.db.tareas.insert(data)
            else:
                return {"response": "el titulo es obligatorio"}

        return redirect(url_for("tareas"))

    """Actualizacions - put
    """
    def put(self, titulo):
        data = request.get_json()
        mongo.db.tareas.update({'titulo': titulo}, {'$set': data})
        return {"response": "actualizado correctamente "}

    """Borrado - delete
    """
    def delete(self, titulo):
	print titulo
        mongo.db.tareas.remove({'titulo': titulo})
        return {"response": "borrado correctamente "}

"""Raiz
"""
class Index(Resource):
    def get(self):
        return redirect(url_for("tareas"))


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Tarea, "/tareas", endpoint="tareas")
api.add_resource(Tarea, "/tareas/<string:titulo>", endpoint="titulo")
api.add_resource(Tarea, "/tareas/descripcion/<string:descripcion>", endpoint="descripcion")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000')
