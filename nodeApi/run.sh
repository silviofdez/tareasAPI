#!/bin/bash
#lanzamos en seugndo plano, datos configurados
mongod --dbpath ./data &

#esperamos a que termine de levantarse mongo, tarda por el preallocation, se podria desactivar, pero penaliza
while ! curl http://127.0.0.1:27017/
do
  echo "$(date) - esperando a MongoDB"
  sleep 1
done
echo "$(date) - MongoDB correctamente levantado"
#levantamos nuestra api
nodejs ./Server.js
