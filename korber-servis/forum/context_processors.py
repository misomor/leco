from django.conf import settings
from .models import Category, Document
from django.shortcuts import render


def navbar_menu(request):
    categories = Category.objects.all()
    return {'categories': categories}

def documents_category(request, ):
    documents = Document.objects.filter(file=1)
    return {'documents': documents}
