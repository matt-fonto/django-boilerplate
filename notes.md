```python
pip install virtualenv # install virtualenv, which is a tool to create isolated Python environments
virtualenv env # create a virtual environment called env
source env/scripts/activate # activate the virtual environment
source env/scripts/deactivate # deactivate the virtual environment
pip install django # install django
django-admin startproject <project-name> # create a new project called...
python manage.py migrate # create the database
python manage.py makemigrations # create the migrations for the database, which are the changes to the database
python manage.py runserver # run the development server
python manage.py startapp <app-name> # create a new application called...
python manage.py createsuperuser # create a superuser for the admin panel
```

- Everytime you close the section, you'll need to activate the environment once again

## Django Template Tags

- Django template tags are used to transfer data from the view to the template
- The template tags are surrounded by curly braces
- The template tags are used to display data, perform loops, and perform logic

```html
{% if
<condition>
  %}
  <h1>True</h1>
  {% else %}
  <h1>False</h1>
  {% endif %}</condition
>
```

superuser.password = 123abc!!

## Django's ORM

Important concepts of Django's ORM:

- Models: Python classes that define the structure and behavior of database tables
- Database Migration: system that automates the process of creating and updating database schema
- Querying data: query API which will be used to perform actions on the database, such as:
  filter, exclude, order_by, limit
- Relationships: Django's ORM allows relationships between the models, such as one-to-one, one-to-many, many-to-many

## Django's Admin Panel

- The admin panel is a built-in feature of Django that allows you to perform CRUD operations on the database
- The admin panel is automatically generated based on the models
- To access the admin panel, you need to create a superuser
- To create a superuser, run the following command:

```python
python manage.py createsuperuser
```

- To access the admin panel, go to (http://127.0.0.1:8000/admin/)
