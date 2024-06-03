SYP - Sobrevivir y Prosperar, es un proyecto personal, ya que tengo un canal de youtube con un amigo/socio de supervivencia, consejos y guias. La idea es ir agregando funcionalidades a la web. 
Por ahora esta hecha para que cumpla con la tercer pre entrega, pero la iré mejorando

desde la pagina principal, se puede acceder a todas las funcionalidades, ya sea listados, formularios o busqueda. tiene botones interactivos, imagenes que redirecciona a Youtube y el icono de instagram es funcional.

Sistema de Gestión de Videos
Este es el proyecto "SYP", un sistema de gestión de videos desarrollado con Django. El proyecto permite buscar videos por número y gestionar suscriptores, ademas los suscriptores pueden subir historias de supervivencia.

Tabla de Contenidos
-Requisitos
-Instalación
-Configuración
-Uso
-Rutas Disponibles

Antes de empezar, asegúrate de tener instalado lo siguiente:

Python 3.8 o superior
Django 3.0 o superior
Git

Instalación
Clona el repositorio en tu máquina local:

bash
Copiar código

   git clone https://github.com/federicomertl/SYP.git

cd SYP

Instala las dependencias necesarias:

bash
Copiar código

  pip install -r requirements.txt

Aplica las migraciones a la base de datos:

bash
Copiar código

  python manage.py migrate

(Opcional) Carga datos iniciales:

bash
Copiar código

  python manage.py loaddata initial_data.json

Configuración (yo no use un entorno virtual)
Asegúrate de tener un archivo .env en la raíz del proyecto con la configuración necesaria para tu entorno de desarrollo. Un ejemplo de archivo .env podría ser:

makefile
Copiar código
DEBUG=True
SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///db.sqlite3
Uso
Para ejecutar el servidor de desarrollo, utiliza el siguiente comando:

bash
Copiar código

  python manage.py runserver

Luego, abre tu navegador y ve a http://127.0.0.1:8000/ para ver la aplicación en acción.

Rutas Disponibles
Búsqueda de Videos
Ruta: /busqueda-video/
Método: GET
Descripción: Página para buscar videos por número.
Resultados de Búsqueda
Ruta: /buscar/
Método: GET
Descripción: Página que muestra los resultados de la búsqueda de videos.
Administración de Suscriptores
Ruta: /admin/
Método: GET
Descripción: Página de administración para gestionar suscriptores y otros modelos.

tambien cree un super usuario para que puedan corroborar la informacion desde el admin ingresando a
http://127.0.0.1:8000/admin

usuario: CristianoRonaldo
password: Elreydelamilanga

Quedo atento a sus comentarios

Saludos

Federicomertl
