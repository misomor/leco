

from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>/', views.category_documents, name='category_documents'),
    path('create_category/', views.create_category, name='create_category'),

]


