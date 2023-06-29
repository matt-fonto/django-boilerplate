```python
pip install virtualenv # install virtualenv, which is a tool to create isolated Python environments
virtualenv env # create a virtual environment called env
source env/scripts/activate # activate the virtual environment
source env/scripts/deactivate # deactivate the virtual environment
pip install django # install django
django-admin startproject <project-name> # create a new project called...
python manage.py migrate # create the database
python manage.py runserver # run the development server
python manage.py startapp <app-name> # create a new application called...
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
