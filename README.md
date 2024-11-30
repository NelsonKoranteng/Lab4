Run the following command to create a new Django project:
django-admin startproject myproject
cd mydjangoproject
2. Create the App
python manage.py startapp mydjangoapp
Add your app to INSTALLED_APPS in settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    'mydjangoapp',
]
3. Set Up Templates
index.html
contacts.html
help.html
Updated TEMPLATES in settings.py to include the new templates directory:

python
Copy code
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
4. Updated Models
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
Run the migrations to update the database schema:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Update Views
Open contactsapp/views.py and create views for the app:
python
Copy code
from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'mydjangoapp/index.html')

def contacts(request):
    contact_list = Contact.objects.order_by('first_name')
    contact_dict = {'contacts': contact_list}
    return render(request, 'mydjangoapp/contacts.html', context=contact_dict)

def help(request):
    return render(request, 'mydjangoapp/help.html')
6. Set Up URLs
In myproject/urls.py, include the app's URLs:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contactsapp.urls')),
]
Create a new urls.py file in mydjangoapp:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('help/', views.help, name='help'),
]
7. Admin Interface
Register the Contact model in mydjangoapp/admin.py:

from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
Start the Django server:

python manage.py runserver
Access the admin interface at http://localhost:8000/admin/ and add some contacts.

8. Update HTML Templates
index.html: Add a greeting and links to the other pages.

html
Copy code
<h1>Welcome to the Contacts App</h1>
<p><a href="/contacts/">View Contacts</a></p>
<p><a href="/help/">Help Page</a></p>
contacts.html: Display the list of contacts.

html

<h1>Contacts</h1>
<ul>
    {% for contact in contacts %}
        <li>{{ contact.first_name }} {{ contact.last_name }} - {{ contact.email }} - {{ contact.phone }}</li>
    {% endfor %}
</ul>
help.html: Explain the functionality of the app.

html
{% load static %} <!-- Load static tag -->
<h1>Help Page</h1>
<p>This site allows you to view a list of contacts, manage them through the admin interface, and navigate to other pages using the links provided.</p>
9. Style the Pages with CSS
Created a static folder in the app directory and add a CSS file (e.g., styles.css).
Link the CSS file in your HTML templates:
html
Copy code
<link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
10. View the Pages
Go to:
Index Page: http://localhost:8000/
Help Page: http://localhost:8000/help/
Contacts Page: http://localhost:8000/contacts/
