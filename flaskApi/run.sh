#!/bin/bash
mongod --dbpath ./data &
#esperamos a que se levante mongo, tarda en el preallocation
while ! curl http://127.0.0.1:27017/
do
  echo "$(date) - esperando a MongoDB"
  sleep 1
done
echo "$(date) - MongoDB correctamente levantado"
#levantamos api
python ./Server.py
