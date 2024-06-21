
SYP - Sobrevivir y Prosperar, es un proyecto personal, ya que tengo un canal de youtube con un amigo/socio, el canal es con tematica de supervivencia, consejos y guias.  

les dejo un link con el video en youtube para que puedan ver las funcionalidades https://www.youtube.com/watch?v=qjUkYrx0XgE

Para acceder a las funcionalidades de la web, necesitas loguearte, ya que la mayoria de los campos estan bloqueados, una vez que accediste desde la pagina principal, se habilitan todas las funcionalidades, ya sea listados, formularios o busqueda. tiene botones interactivos, imagenes que redirecciona a Youtube y el icono de instagram es funcional.

Este es el proyecto "SYP", un sistema que gestiona videos, interactua con los internautas a traves de las experiencias que pueden subir a la web, y tambien pueden buscar informacion de herramientas utiles para la supervivencia, el mismo fue desarrollado con Django. 

Tabla de Contenidos
1-Requisitos
2-Instalación
3-Configuración
4-Uso
5-Rutas Disponibles


1-Antes de empezar, asegúrate de tener instalado lo siguiente:

Python 3.8 o superior
Django 3.0 o superior
Git


2-Instalación
Clona el repositorio en tu máquina local:

bash
Copiar código

   git clone https://github.com/federicomertl/SYP.git


cd SYP

Aplica las migraciones a la base de datos:

bash
Copiar código

  python manage.py migrate


3-Configuración (yo no use un entorno virtual)
Asegúrate de tener un archivo .env en la raíz del proyecto con la configuración necesaria para tu entorno de desarrollo. 

ejecutar el servidor de desarrollo, utiliza el siguiente comando:

bash
Copiar código

  python manage.py runserver

estas son las dependencias que yo tengo instaladas

asgiref==3.8.1
certifi==2024.2.2
distlib==0.3.8
Django==5.0.6
filelock==3.14.0
pillow==10.3.0
pipenv==2023.12.1
platformdirs==4.2.2
setuptools==69.5.1
sqlparse==0.5.0
tzdata==2024.1
virtualenv==20.26.2

4-Luego, abre tu navegador y ve a http://127.0.0.1:8000/ para ver la aplicación en acción.


5-Rutas Disponibles

INICIO
NOSOTROS - Descripcion de mi
VIDEOS - Listado de videos con su link
EXPERIENCIAS - Listado de Experiencias de usuarios
LISTA DE HERRAMIENTAS - Listado de herramientas utiles para la supervivencia
BUSQUEDA DE VIDEOS - Busqueda de videos por número
CREAR HERRAMIENTAS - Esta funcionalidad solo esta habilitado para el Staff, podemos agregar nuevas herramientas
CARGAR NUEVOS VIDEOS - Esta funcionalidad solo esta habilitado para el Staff, podemos agregar nuevos videos
CUENTANOS TUS EXPERIENCIAS - El usuario puede contarnos sus experiencias
AVATAR - Podemos agregar un avatar a nuestro perfil
EDITAR PERFIL - Podemos editar el perfil, cambiar datos ya sea nombre de usuario o password


tambien cree un super usuario para que puedan corroborar la informacion desde el admin ingresando a
http://127.0.0.1:8000/admin

usuario: CristianoRonaldo
password: Elreydelamilanga




Quedo atento a sus comentarios

Saludos

Federicomertl

