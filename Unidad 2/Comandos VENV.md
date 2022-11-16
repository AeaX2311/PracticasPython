# Comandos VENV

    ## Inicializar entorno
        py -3 -m venv .venv

    ## Activar
        .venv\scripts\activate

    ## Instalar django
        pip install django

    ## Instalar flask
        pip install flask

# Django
    ## Crear app
        django-admin startproject <Nombre>

    ## Correr servidor
        python manage.py runserver

    ## Crear app desde servidpr
        python manage.py startapp <Nombre>

    ## Agregar pagina
        Se agrega a los setting, urls.py....

    ## Registrar modelos 
        En admin.py => admin.site.register()

    ## Mostrar listado de migraciones 
    [] - No ejecutadas..
        python manage.py showmigrations

    ## Ejecutar migracion
        python manage.py migrate

    ## Crea una tabla en la base de datos a partir de una clase en models
        python manage.py makemigrations

    ## Crear usuario para acceder a config
        python manage.py createsuperuser

# Flask
    ## Correr servidor
        flask run
