FROM	ubuntu:14.04

# curl se instala para poder comprobar cuando terminar arrancar mongo
RUN apt-get update && apt-get install -y \
	nodejs npm \
	mongodb \
	curl


# creamos directorio para la aplicacion
RUN mkdir -p /usr/src/tareasApi
WORKDIR /usr/src/tareasApi

# creamos directorio de datos para mongo
RUN mkdir -p /usr/src/tareasApi/data

# instalamos paquenes que necesitamos
COPY package.json /usr/src/tareasApi/package.json
RUN cd /usr/src/tareasApi; npm install

# copiamos la aplicacion
COPY . /usr/src/tareasApi

# damos permisos script que inicia mongo, espera a que arranque y despues inicia nuestra api
RUN chmod 711 /usr/src/tareasApi/run.sh

EXPOSE 3000
CMD ["/usr/src/tareasApi/run.sh"]
