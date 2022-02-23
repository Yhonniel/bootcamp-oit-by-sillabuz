# DJANGO Comands

### Requirement

- Python 3.*
- pip
- virtualenv

### Create project

- ```$ virtualenv venv```
- Windows ```$ .\venv\Scripts\activate```
- Linux ```$ source venv/bin/activate ```
- ```$ django-admin  startproject mysite```

``` 
mysite/
|    manage.py
|____mysite/
     |   __init__.py
     |   settings.py
     |   urls.py
     |   asgi.py
     |   wsgi.py
```

- ```$ python manage.py makemigrations```
- ```$ python manage.py migrate```
- ```$ python manage.py createsuperuser```
- ```$ python manage.py runserver``` 

> regresar al principio las migraciones de una aplicacion
- ```$ python manage.py migrate <app_name> zero``` 
 