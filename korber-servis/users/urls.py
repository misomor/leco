
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.login_user, name='login'),
    path('logut/',views.logout_user, name='logout'),

]
