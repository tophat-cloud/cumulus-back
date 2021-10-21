<p align="center">
  <p align="center">
    <a href="https://cumulus.tophat.cloud" target="_blank">
      <img src="https://jinui.s3.ap-northeast-2.amazonaws.com/tophat/logo.png" alt="Cumulus" height="72">
    </a>
  </p>
</p>

# Contributing
Welcome and Thanks your suggestion! we ready for accept grateful idea. Just throw your idea in the form of pull requests on GitHub. Let's contribute and be a cumulus family!

## Versioning & Branch
- We adopt [calvar](https://calver.org) as versioning.
- We adopt Git Flow branch strategy.

## Environment
    Ubuntu 20.04
    Python 3.8.10
    PostgreSQL 13

## Setup

### Install requirements
    pip install -r requirements.txt

### Create database 
    python manage.py makemigrations
    python manage.py migrate

### Create super user
    python manage.py createsuperuser

### Run on development
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
