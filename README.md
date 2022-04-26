
#### Prerequisite:
###### 1: python 3.8
# How to install:
###### Download or clone the reposatory. Goto project root folder.

```
C:\>git clone https://github.com/imkhaled404/banglanews.git

C:\>cd banglanews

C:\banglanews>virtualenv venv

C:\banglanews>cd venv

C:\banglanews\venv>scripts\activate.bat

(venv)C:\banglanews\venv>cd ..

(venv)C:\banglanews>pip freeze > requirements.txt

(venv)C:\banglanews>pip install -r requirements.txt

(venv)C:\banglanews>python manage.py migrate

(venv)C:\banglanews>python manage.py runserver
```

```
### It will start a local server on 'http://localhost:8000'
```

###### create a super user using,
```
(venv)C:\banglanews>python manage.py createsuperuser
```
###### then go to http://localhost:8000/admin to accesss your administrations to control your dynamic application.


###### It's ready to deploy in heroku.Before deploy in heroku, change the local database in settings.py according to:
###### You will find database settings like this.
```
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   
   }

}
```

###### You need to change it like below,

```
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
       
        'NAME': 'example_db',
        
        'USER': 'your user',
        
        'PASSWORD': 'your password',
        
        'HOST': 'localhost',
        
        'PORT': '2000',
        
    }

}
```
```
###### Congrats! everything is setup. Your project ready to deploy in heroku for live your project online.
Get any error, send me the scrrenshot at my inbox, i will try to give you the solution.

```
