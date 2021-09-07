# Tophat-Cloud-Back
Django-based API Backend Server

## Environment
    Ubuntu 20.04
    Python 3.8.10
    PostgreSQL 13

## Install
    pip install -r requirements.txt

## Create database 
    python manage.py makemigrations
    python manage.py migrate

## Create super user
    python manage.py createsuperuser

## Run on development
    python manage.py runserver

## Secret
You have to write the Django secret key and database information in an .env file. 

Keep your secret from code and **DO NOT** push it on a public repository.

**.env example**
```
SECRET_KEY =        # write your secret_key
DATABASE_NAME =     # write your db_name
DATABASE_USER =     # write your db_user
DATABASE_PW =       # write your db_password
```

## Author
ChangHoon Sung

## License
MIT LICENSE
