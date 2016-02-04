FROM	ubuntu:trusty

# curl se instala para poder comprobar cuando terminar arrancar mongo - build*essential y python-dev para solucionar warnings con pip 
RUN apt-get update && apt-get install -y \
	python-pip \
	mongodb \
	curl \
	build-essential python-dev


# creamos directorio para la aplicacion
RUN mkdir -p /usr/src/tareasApi
WORKDIR /usr/src/tareasApi
RUN cd /usr/src/tareasApi

# creamos directorio de datos para mongo
RUN mkdir -p /usr/src/tareasApi/data

# creamos entorno virtual de python
RUN pip install virtualenv
RUN virtualenv /usr/src/tareasApi/venv
# ponemos el . en lugar de source (es para bash, no sh(
RUN . /usr/src/tareasApi/venv/bin/activate

# instalamos paquenes que necesitamos
COPY paquetes.txt /usr/src/tareasApi/paquetes.txt
RUN pip install -r paquetes.txt

# copiamos la aplicacion
COPY . /usr/src/tareasApi

# damos permisos script que inicia mongo, espera a que arranque y despues inicia nuestra api
RUN chmod 711 /usr/src/tareasApi/run.sh

EXPOSE 3000
CMD ["/usr/src/tareasApi/run.sh"]
