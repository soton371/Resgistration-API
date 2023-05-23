# Resgistration-API
#1 create virtual environment:
python -m venv venv

#2 venv active:
venv/Scripts/activate

#3 install:
pip install django djangorestframework

#4 create project:
django-admin startproject name .

#5 to check:
python manage.py migrate  
python manage.py runserver

#6 configs:
setting.py,urls.py

#7 create app:
python manage.py startapp appname

#8 add urls.py file inside app
