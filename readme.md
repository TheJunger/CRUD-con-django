# TASKLIST

Este es un proyecto de tasklist básico desarrollado con HTML, CSS, JavaScript, Python, Django y SQLite3.

## Instalacion
1. Clona este repositorio en tu máquina local:

    `git clone https://github.com/tu_usuario/tasklist.git`
2. Accede al directorio del proyecto:

    `cd tasklist`

3. Crea y activa un entorno virtual (opcional pero recomendado):

    ` pip install virtualenv `

    ` virtualenv nombre_entorno_virtual  `

    ` .\nombre_entorno_virtual\Scripts\activate `

4. Instala 'Django':

    ` pip install django `

5. Ejecuta las migraciones de la base de datos:

    ` python manage.py migrate `

## USO

1. Inicia el servidor de desarrollo:

    ` python manage.py runserver `

2. Abre tu navegador web y visita http://localhost:8000/view_tasks para acceder a la aplicación de tasklist.

3. En la aplicación, puedes crear nuevas tareas, editar tareas existentes y eliminar tareas.