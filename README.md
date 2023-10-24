# Streamlit_app_docker
Este es un ejemplo básico para ejecutar Streamlit-apps en contenedores
Docker.Para ejecutar el contenedor que se muestra en este tutorial se
asume que Docker ya esta instalado.

Sin embargo a continuación te dejo el enlace para la descarga de [Docker](https://www.docker.com/)

## Estructura

El siguiente proyecto considera como archivos y elementos principales,el archivo **Dockerfile**,el archivo **requirements.txt** y **app_cloud_gcp_py.py**

El archivo Dockerfile sera con el que construiremos la imagen para luego desplegar en un contenedor,en cambio los otros archivos son necesarios para la ejecución de la Streamlit-app.

``` docker
- 📁 Streamlit_app_docker
  - 📄 README.md
  - 📄 Dockerfile
  - 📄 app_cloud_gcp_py.py
  - 📄 requirements.txt
  - 🖼️ docker_1.png
  - 💹 trip_austin.csv        
  - 📄 .gitignore
      
```

### Dockerfile

El archivo docker puede ser modificado segun el tipo de aplicación que
se utilice.En este caso si deseas seguir trabajando con Streamlit-apps,y
agregar otras features,puedes agregar las bibliotecas que vayas a utilizar en el **requirements.txt**.

``` docker
# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080


ENTRYPOINT ["streamlit", "run", "app_cloud_gcp_py.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

## Build

Para construir la imagen docker llamada **stream_app**,se usa la siguiente linea.

``` docker
docker build -t stream_app .
```

## Run

Una vez lista la imagen **stream_app**,ejecutamos la siguiente linea para ejecutar nuestra imagen dentro de un contenedor que tendra expuesto el puerto 8080.

``` docker
docker run -d -p 8080:8080 stream_app 
```
## Acceso al contenedor

Si todos los pasos anteriores se desarrollaron de forma correcta,el contenedor se debe estar ejecutando en la siguiente dirección.

[127.0.0.1:8080](http://127.0.0.1:8080)
