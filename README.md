# wactest

Para lanzar el proyecto:
- Construir contenedor de Docker con ```docker build .```
- Lanzar imagenes de Docker con ```docker-compose up```
- Ingresar a la imagen web de Docker con ```docker-compose exec web /bin/bash```
- Crear el superusuario con  ```python manage.py createsuperuser ```
- Ingresar al admin en ```localhost:8000/admin```
- Probar con Postman los distintos servicios (Tutorial en https://youtu.be/EU8p4kXxmas)