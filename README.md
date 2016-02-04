Se ha realizado version de la API tanto en javascript (nodejs) y python (flask)
Cada una se encuentra en su correspondiente directorio.
Se anexan los README de las distintas versiones.
JAVASCRIPT
API res para tareas desarrollada en JavaScrip usando node.js y MongoDB
Dockerizada en un solo contenedor (se podria haber hecho en dos, uno para la api y otro para MongoDB)
Para generar el docker ejecutar:
docker build -t <user>/tareas-node .
Para ejecutar el docker:
docker run -p 3000:3000 -d <user>/tareas-node
La imagen docker esta disponible para descargar en hub.docker.com
docker pull silviofdez/tareas-node
Para probar las distintas peticiones se puede usar un cliente REST como Postman y ejecutar las siguientes peticiones (sustituir la ip por la que proceda)
GET 192.168.106.133:3000/tareas
POST 192.168.106.133:3000/tareas
{
    "titulo" : "compra",
    "descripcion" : "pavo, atun"
}
GET 192.168.106.133:3001/tareas
respuesta:
{
  "error": false,
  "message": [
    {
      "descripcion": "pavo, atun",
      "titulo": "compra",
      "_id": "56b349bb9608b5943f660404",
      "__v": 0
    }
  ]
}
GET 192.168.106.133:3001/tareas/56b349bb9608b5943f660404
PUT 192.168.106.133:3001/tareas/56b349bb9608b5943f660404
{
    "descripcion" : "servilletas, aceite"
}
DELETE 192.168.106.133:3000/tareas/56b349bb9608b5943f660404
--------------------------------------------------------------------------------------
PYTHON
API resta para tareas desarrollada en Python usando Flask y MongoDB
Dockerizada en un solo contenedor *se podria haber hecho en dos, uno para la api y otro para MongoDB)
Para generar el docker ejecutar:
docker build -t <user>/tareas-python .
Para ejecutar el docker:
docker run -p 3000:3000 -d <user>/tareas-python
La imagen esta disponible en hub.docker.com
docker pull silviofdez/tareas-python
Para probar las distintas peticiones se puede usar un cliente REST como Postman y ejecutar las siguientes peticiones
GET 192.168.106.133:3000/tareas
POST 192.168.106.133:3000/tareas
{
    "titulo" : "compra",
    "descripcion" : "pavo, atun"
}
GET 192.168.106.133:3001/tareas/compra
PUT 192.168.106.133:3001/tareas/compra
{
    "descripcion" : "servilletas, aceite"
}
DELETE 192.168.106.133:3000/tareas/compra
