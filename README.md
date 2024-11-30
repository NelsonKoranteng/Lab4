Steps to Build the Django Contacts App
1. Start the Project
bash
Copy code
django-admin startproject mydjangoproject
cd mydjangoproject
python manage.py startapp mydjangoapp
Add mydjangoapp to INSTALLED_APPS in settings.py.
2. Set Up Templates
Create a templates folder in the root directory.
Inside templates, create a mydjangoapp folder and add:
index.html
contacts.html
help.html
Update settings.py to include the templates directory:
python
Copy code
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
3. Define the Contact Model
In mydjangoapp/models.py:

python
Copy code
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
4. Create Views
In mydjangoapp/views.py:
python
Copy code
from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'mydjangoapp/index.html')

def contacts(request):
    contact_list = Contact.objects.order_by('first_name')
    return render(request, 'mydjangoapp/contacts.html', {'contacts': contact_list})

def help(request):
    return render(request, 'mydjangoapp/help.html')
5. Set Up URLs
In mydjangoproject/urls.py, include the app's URLs:

python
Copy code
from django.urls import path, include

urlpatterns = [
    path('', include('mydjangoapp.urls')),
]
Create urls.py in mydjangoapp:

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('help/', views.help, name='help'),
]
6. Register the Model in Admin
In mydjangoapp/admin.py:

python
Copy code
from .models import Contact
admin.site.register(Contact)
Run the Django server and add contacts via the admin interface:

bash
Copy code
python manage.py runserver
7. Update HTML Files
index.html:

html
Copy code
<h1>Welcome to My Django Project</h1>
<p><a href="/contacts/">View Contacts</a></p>
<p><a href="/help/">Help Page</a></p>
contacts.html:

html
Copy code
<h1>Contacts</h1>
<ul>
    {% for contact in contacts %}
        <li>{{ contact.first_name }} {{ contact.last_name }} - {{ contact.email }} - {{ contact.phone }}</li>
    {% endfor %}
</ul>
help.html:

html
Copy code
<h1>Help Page</h1>
<p>This is a simple contacts app built using Django.</p>
8. Style with CSS
Create a static folder in mydjangoapp and add a CSS file (e.g., styles.css).
Link the CSS file in HTML templates:
html
Copy code
<link rel="stylesheet" href="{% static 'styles.css' %}">
9. View the Pages
Access the pages:
Index Page: http://localhost:8000/
Contacts Page: http://localhost:8000/contacts/
Help Page: http://localhost:8000/help/
