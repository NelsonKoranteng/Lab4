from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'mydjanapp/index.html')

def contacts(request):
    contact_list = Contact.objects.order_by('first_name')
    context = {'contacts': contact_list}
    return render(request, 'mydjanapp/contacts.html', context)


def help(request):
    return render(request, 'mydjanapp/help.html')


# Create your views here.
