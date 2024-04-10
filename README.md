# Prueba Backend ODOO

Este repositorio se utiliza para llevar a cabo la prueba técnica del proceso de selección para el puesto de Desarrollador Backend ODOO.

La prueba está desarrollada utilizando las siguientes tecnologías/frameworks:

- Odoo 16
- Postgres 15
- Docker

## Instalación

Para montar el proyecto en tu máquina local, primero debes asegurarte de tener instalado docker,
para ello puedes ejecutar:

```bash
   docker --version

De no tenerlo instalado, no te preocupes, puedes encontrar toda la documentación para instalarlo en

https://docs.docker.com/get-docker/

Luego de asegurarte que tienes todo instalado, sigue los siguientes pasos:
   
1. En tu CMD, desde la carpeta que contenga el proyecto, asegurate que se encuentre el archivo docker-compose.yml y Dockerfile.
Contruye la imagen de Docker ejecutando el siguiente comando:
   ```bash
   docker-compose up -d --build

2. Inicializa la base de datos de ser necesario, descomentando la linea de estar comentada en docker-compose.yml
   ```bash
   command: sh -c "python3 -m debugpy --listen 0.0.0.0:8888 /usr/bin/odoo -i base"
   Puedes seguir teniendo esta linea descomentada, pero te sugerimos retirar los comandos -i base, ya que se te 
   inicializara nuevamente la base de datos al reiniciar Docker.

3. Luego de levantar correctamente Docker, dirigite a http://localhost:8069/web en tu navegador,
   este te llevara a la pagina principal de tu Odoo, ahí inicia sesion utilizando "admin" como usuario y password.

4. Dirigete al apartado de aplicaciones e instala el addons test_contacts para poder obtener todos los addons que vas a necesitar.

5. Y listo puedes comenzar a programar. Asegurate de tener disponible en el menu los apartados de Contactos(Contacts) y REST API
```

# Modificaciones

## Create docker network
```bash
   docker network create -d bridge test-network
```

## models/res_partner.py

* Se agregaron los atributos `x_coordinate`, `y_coordinate` y `gender`
* Se agrego el método `search_closes_partners` para obtener los partner que estan dentro de la distancia especificada.

## views/res_partner.xml

* Se muestran los atributos en la pestaña de **Información Extra** del modulo Contacts.

## Modificaciones en __manifest__.py
1. Se agrego `data/res_partner.xml` al `__manifest__.py` del modulo.
2. Se agrego `view/res_partner.xml` al `__manifest__.py` del modulo. 

## services/contact.py

* Se implemento el servicio `close_contact`.

## Consideraciones extras

Para ocupar la API, se necesita iniciar sesión dentro de la página web de odoo `localhost:8069`. De esta manera en el navegador se guardará la cookie de la sesión que será utilizada cuando se haga la consulta a traves de la Swager. 